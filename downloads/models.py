from django.db import models
from User.models import User

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
    price = models.PositiveSmallIntegerField(default=5)
    thumbnail = models.CharField(max_length=120, default="")

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self):
        return self.title


class UserHistory(models.Model):
    """
    User History
    """
    user = models.ForeignKey(User, related_name="user_history")
    song = models.ForeignKey(Songs)
    datetime = models.DateTimeField(auto_now=True)

    # class Meta:
    #     abstract = True