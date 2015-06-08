from django.db import models

class Songs(models.Model):
    """
    Complete Information of Songs that are already been downloaded
    """
    youtube_link = models.URLField(max_length=100, unique=True)
    local_link = models.URLField(max_length=300, default="")
    title = models.CharField(max_length=200, default="")
    uploader = models.CharField(max_length=50, default="", blank=True)
    view_count = models.PositiveIntegerField(default=0, null=True)
    like_count = models.PositiveIntegerField(default=0, null=True)
    unlike_count = models.PositiveIntegerField(default=0, null=True)
    download_count = models.PositiveIntegerField(default=0, null=True)


class UserHistory(models.Model):
    """
    User History
    """
    #user = models.ForeignKey('User')
    song = models.ForeignKey('Songs')
    datetime = models.DateTimeField(auto_now=True)