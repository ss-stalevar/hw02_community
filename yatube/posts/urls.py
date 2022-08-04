from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_list, name='group_list'),
    path('create/', views.post_create, name='post_create'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:post_id>/', views.post_detail, name='post_detail'),
    path("<str:username>/<int:post_id>/edit/", views.post_edit, name="post_edit"),
]

#path('gropup_list/', include('posts.urls', namespace='posts')),
