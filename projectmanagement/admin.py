from django.contrib import admin
from .models import Project, Task

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','status','first_contributor','second_contributor','third_contributor','updated')
    list_filter = ('title','status','created','updated')
    search_fields = ('title','status',)
    ordering = ('status',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)