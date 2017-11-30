from django.db import models


class Forum(models.Model):
    forum_name = models.CharField(max_length=200)
    forum_description = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Forum'

    def __str__(self):
        return self.forum_name


class ForumThread(models.Model):
    forum_post = models.ForeignKey(Forum)
    forum_content = models.TextField()
    created = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Forum Thread'

    def __str__(self):
        return self.forum_post.forum_name
