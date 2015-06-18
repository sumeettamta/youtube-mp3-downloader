from django.contrib import admin

# Register your models here.
from .import models

admin.site.register(models.Songs)
admin.site.register(models.UserHistory)