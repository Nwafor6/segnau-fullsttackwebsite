from django.contrib import admin
from .models import Blog, Newsletter, Membership

# Register your models here.

admin.site.register(Blog)
admin.site.register(Newsletter)
admin.site.register(Membership)