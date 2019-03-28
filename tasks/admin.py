from django.contrib import admin

from .models import Task, TaskResult


admin.site.register(Task)
admin.site.register(TaskResult)
