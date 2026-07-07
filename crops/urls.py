from django.urls import path
from . import views
app_name = 'crops'
urlpatterns = [
    path('', views.crop_list, name='list'),
    path('<int:pk>/', views.crop_detail, name='detail'),
    path('my-crops/', views.my_crops, name='my_crops'),
    path('chat/', views.crop_chat, name='chat'),
]
