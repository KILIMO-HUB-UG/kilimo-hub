from django.urls import path
from . import views
app_name = 'translation'
urlpatterns = [
    path('translate/', views.translate_view, name='translate'),
    path('languages/', views.language_options, name='languages'),
]
