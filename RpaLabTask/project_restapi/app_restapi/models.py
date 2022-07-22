from datetime import datetime
from django.db import models

# Create your models here.
class AppPost(models.Model):
    video_title = models.CharField(max_length=100, default=None)
    video_desc = models.CharField(max_length=200, default=None)
    video_file = models.FileField(default=None, null=True)
    video_by = models.CharField(max_length=200, default=None)
    video_created_at = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "app_post"
    
    def __str__(self):
        return self.post_title