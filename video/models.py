from django.db import models
from users.models import CustomUser

class Video(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumbnail_url = models.URLField()
    video_url = models.URLField()
    likes = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    text = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    likes = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
