
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from account.tokens import account_activation_token
from .forms import SignupForm
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have logged out')
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
        current_site = get_current_site(request)
        message = render_to_string('account/activate_email.html', {
            'user': User,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(User.pk)),
            'token': account_activation_token.make_token(User),
        })
        mail_subject = 'Activate your ecollege account.'
        to_email = User.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')

    else:
        new = SignupForm()

    return render(request, 'account/register.html', {'form': new})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')