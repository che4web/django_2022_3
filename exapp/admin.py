from django.contrib import admin
from exapp.models import Course,Exersise

# Register your models here.
class ExersizrInline(admin.TabularInline):
    model = Exersise

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','get_exersuse_count']
    inlines = [
        ExersizrInline
    ]
class ExersizrAdmin(admin.ModelAdmin):
    list_display = ['id','name','course']


admin.site.register(Course,CourseAdmin)
admin.site.register(Exersise,ExersizrAdmin)
