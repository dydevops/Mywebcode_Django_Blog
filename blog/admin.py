from django.contrib import admin
from .models import Post, Category,BlogComment
# Register your models here.

   
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['sno','category_name', 'slug', 'status', 'created_on' ]
    list_display_links = ('sno', 'category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}
    
    
class PostAdmin(admin.ModelAdmin):
    list_display = ['sno','title','author','category','status']
    list_display_links = ('sno', 'title',)
    prepopulated_fields = {'slug': ('title',)}    

class BlogCommentAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
