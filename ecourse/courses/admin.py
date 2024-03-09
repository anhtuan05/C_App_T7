from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission
from django.utils.safestring import mark_safe

from .models import Category, Courses, Tag, Lesson


class CategoryAdmin (admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['name']

class CoursesAdmin (admin.ModelAdmin):
    list_display = ['id', 'name', 'desciption', 'image']
    readonly_fields = ['img']

    def img(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/styles.css',)
        }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Tag)
admin.site.register(Lesson)
admin.site.register(Permission)

