from django.contrib import admin
from oauth2.models import FlowModel, CredentialsModel


admin.site.register(FlowModel)
admin.site.register(CredentialsModel)
