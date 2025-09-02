from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.bloghome, name='bloghome'),
    path('create_blog/',views.create_blog, name='create_blog'),
    path('<int:blog_id>/blog_detials/',views.blog_detials, name='blog_detials'),
    path('<int:blog_id>/edit_blog/',views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete_blog/',views.delete_blog, name='delete_blog'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('<int:comment_id>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('dashboard/',views.dashboard, name = 'dashboard'),


    path('__reload__/', include('django_browser_reload.urls')),
]
