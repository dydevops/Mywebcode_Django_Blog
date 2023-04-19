from django.contrib import admin
from django.utils.html import format_html
from .models import About, Contact
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    # def has_add_permission(self, request, obj=None):
    #     return False
    # def has_delete_permission(self, request, obj=None):
    #     return False
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.about_image.url))
    thumbnail.short_description = 'Image'
    list_display = ['id', 'thumbnail', 'about_title', 'alt_tag', 'status']
    prepopulated_fields = {'slug': ('about_title',)}
    list_display_links = ('id', 'about_title', 'alt_tag')
    search_fields = ('about_title', 'id')
    list_filter = ('status',)
    list_per_page = 5 
    
class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    list_display = ('id', 'name', 'email', 'phone', 'subject', 'create_date')
    readonly_fields = ['id', 'name', 'email', 'phone', 'subject',  'message', 'create_date']
    list_display_links = ('id', 'name', 'phone', 'email' )
    search_fields = ('name', 'email',)
    list_per_page = 25    
    
       
admin.site.register(Contact, ContactAdmin)   
admin.site.register(About, AboutAdmin)      