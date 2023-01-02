"""Defines URL patters for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Page for selected post.
    path('post/<int:post_id>', views.post, name='post'),

    # Page for making new post.
    path('new_post/', views.new_post, name='new_post'),

    # Page for editing selected post.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]