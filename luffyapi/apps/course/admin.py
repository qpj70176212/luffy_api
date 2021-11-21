from django.contrib import admin

# Register your models here.
# # import xadmin
from . import models
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Teacher)
admin.site.register(models.CourseChapter)
admin.site.register(models.CourseSection)