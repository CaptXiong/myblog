from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','body','excerpt')

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('blog','name','content','pub')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)
#admin.site.register(Comment,CommentAdmin)
