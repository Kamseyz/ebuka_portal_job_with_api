from django.contrib.auth.models import User as DefaultUser
from django.contrib import admin

try:
    admin.site.unregister(DefaultUser)
except admin.sites.NotRegistered:
    pass
