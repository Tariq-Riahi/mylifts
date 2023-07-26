from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Feed)
admin.site.register(RecordPost)
admin.site.register(Comment)
