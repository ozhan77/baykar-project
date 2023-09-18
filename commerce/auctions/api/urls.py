from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('ihas/', views.getIhas),
    path('ihas/<int:pk>/', views.getIha),
    path('ihas/<int:pk>/delete/', views.deleteIha, name='deleteIha'),
    path('ihas/<int:pk>/update/', views.updateIha, name='updateIha'),
]