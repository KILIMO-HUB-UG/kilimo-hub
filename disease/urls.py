from django.urls import path
from . import views
app_name = 'disease'
urlpatterns = [
    path('', views.disease_list, name='list'),
    path('report/', views.report_disease, name='report'),
    path('result/<int:pk>/', views.report_result, name='report_result'),
]
