from django.contrib import admin

from .models import AppUser, Bag, UploadSession, UploadedFile

admin.site.register(AppUser)
admin.site.register(Bag)
admin.site.register(UploadedFile)
admin.site.register(UploadSession)
