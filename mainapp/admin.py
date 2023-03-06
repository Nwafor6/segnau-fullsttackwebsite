from django.contrib import admin
from .models import Blog, Newsletter

# Register your models here.

admin.site.register(Blog)
admin.site.register(Newsletter)