#C:\Users\Admin\Desktop\skyhigh\blog\admin.py
from django.contrib import admin


from .models import Category, Tag, Post, Comment

admin.site.register(Category)
admin.site.register(Tag)

admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted', 'author', 'category')  # Add filtering options
    search_fields = ('title', 'content')  # Add search functionality
    filter_horizontal = ('tags',)  # Enable horizontal widget for many-to-many field

    # Optional: Enable CKEditor for the content field (if CKEditor is used)
    formfield_overrides = {
        Post._meta.get_field('content'): {'widget': admin.widgets.AdminTextareaWidget},
    }