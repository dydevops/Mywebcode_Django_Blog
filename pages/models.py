from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
#about model      
class About(models.Model):
    about_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    title_tag = models.CharField(max_length=255, default='MyWeCode')
    meta_description = models.CharField(max_length=255, default='MyWeCode')
    meta_keywords = models.CharField(max_length=255, default='MyWeCode')
    alt_tag = models.CharField(max_length=255, blank=True)
    content = RichTextUploadingField()
    page_banner = models.ImageField(upload_to='about/%Y/%m/%d/')
    about_image = models.ImageField(upload_to='about/%Y/%m/%d/')
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'
    
    def __str__(self):
        return self.about_title
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=100,blank=True)
    message = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.name