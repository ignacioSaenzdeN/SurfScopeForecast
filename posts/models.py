from django.db import models
from SurfScopeForecast.models import SurfingInfo
from django.utils.text import Truncator
from threads.models import Thread


class Post(models.Model):
    # Model to represent the post in a thread
    content = models.TextField()
    thread = models.ForeignKey(
        Thread, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    username = models.TextField(default="")
    creator = models.ForeignKey(
        SurfingInfo, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        # When we get a list of posts objects we will get it back in order of creattion
        ordering = ['created_at']

    def __str__(self):
        truncated_content = Truncator(self.content)
        # TOO delete print statement
        print(truncated_Content.chars(30))
        return truncated_Content.chars(30)
