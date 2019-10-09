from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_publish, name='publish-posts'),
    path('create/', views.create, name='create-publish'),
    path('<int:blog_id>/', views.blog_detail, name='detail-publish'),
    path('update/<int:blog_id>',views.blog_update, name='update-publish'),
    path('delete/<int:blog_id>', views.blog_delete, name='delete-publish'),
]