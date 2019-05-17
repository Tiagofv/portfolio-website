from django.contrib import admin
from .models import Projects, Developer, Work, Education
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'project_date')
    list_editable = ('is_published',)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'state', 'city', 'hire_date')
class WorkAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'occupation', 'until_today', 'hire_date', 'hire_end_date')
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id','school', 'course', 'begin_date', 'end_date', 'until_today')

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)