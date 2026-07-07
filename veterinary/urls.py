from django.urls import path
from . import views
app_name = 'veterinary'
urlpatterns = [
    path('', views.vet_home, name='home'),
    path('chat/', views.vet_chat, name='chat'),
]
