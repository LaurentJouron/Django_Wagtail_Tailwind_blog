from django.contrib import admin
from .models import ChatGroup
from .models import GroupMessage

admin.site.register(ChatGroup)
admin.site.register(GroupMessage)
