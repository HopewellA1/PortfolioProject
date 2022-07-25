from django.contrib import admin
from Portfolio.models import Project
from Blog.models import blog
# Register your models here.

admin.site.register(Project)
admin.site.register(blog)