from django.contrib import admin
from .models import Course, Member, Club

# Register your models here.

admin.site.register(Course)
admin.site.register(Member)
admin.site.register(Club)
