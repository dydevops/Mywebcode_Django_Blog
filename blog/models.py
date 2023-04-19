from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account, UserProfile
from django.conf import settings
from django.utils.timezone import now
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,) 
    
class Category(models.Model):
    sno = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    category_image = models.ImageField(upload_to='category/%Y/%m/%d/', blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-created_on']
        
    def get_url(self):
            return reverse('posts_by_category', args=[self.slug])    
        
    def __str__(self):
        return self.category_name    

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    title_tag = models.CharField(max_length=255, default='Blog Post')
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    # category = models.ManyToManyField('Category', related_name='post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    # author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']
        
    # def category(self):
    #     return ','.join([str(p) for p in self.post_category.all()])
    
    def get_url(self):
         return reverse('post_detail', args=[self.slug])
     
    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment =  models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)    
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment[0:13] + ".... " + "by " + self.user.username
