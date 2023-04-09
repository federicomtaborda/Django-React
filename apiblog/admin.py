from django.contrib import admin

from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'description',
        'category',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)