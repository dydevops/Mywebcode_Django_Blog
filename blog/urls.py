from django.urls import path
from . import views

urlpatterns = [
    path('', views.bolgHome, name='post'),
    path('search/', views.search, name='search'),
    path('category/<slug:category_slug>/', views.bolgHome, name='posts_by_category'),
    path('<slug:post_slug>/', views.blogPost, name='post_detail'),
    path('postComment', views.postComment, name="postComment"),
    # path('search/', views.search, name='search'),
    # path('services/', views.services, name='services'),
    # path('services/<slug:service_slug>/', views.service_detail, name='service_detail'),
    # path('clients/', views.clients, name='clients'),
    # path('testimonials/', views.testimonials, name='testimonials'),
    # path('transport/', views.transport, name='transport'),
    # path('mission-vision/', views.mission_vision, name='mission_vision'),
    # path('group-of-companies/', views.group_of_companies, name='group_of_companies'),
    # path('our-partners/', views.our_partners, name='partners'),

]