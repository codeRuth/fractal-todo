from django.contrib import admin

# Register your models here.
from todoapi.models import Bucket, Todo

admin.site.register(Bucket)
admin.site.register(Todo)
