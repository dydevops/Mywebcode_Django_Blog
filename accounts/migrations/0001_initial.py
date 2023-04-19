# Generated by Django 4.0 on 2022-11-22 01:54

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_title', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='userprofile')),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('website_name', models.CharField(blank=True, max_length=255)),
                ('website_url', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True, max_length=100)),
                ('twitter_link', models.URLField(blank=True, max_length=100)),
                ('linkedin_link', models.URLField(blank=True, max_length=100)),
                ('github_link', models.URLField(blank=True, max_length=100)),
                ('youtube_link', models.URLField(blank=True, max_length=100)),
                ('instagram_link', models.URLField(blank=True, max_length=100)),
                ('address_line_1', models.CharField(blank=True, max_length=100)),
                ('address_line_2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
