from django.contrib import admin
# from __future__ import unicode_literals
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)