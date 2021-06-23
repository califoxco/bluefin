from django.urls import path, include

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home-detail/<slug>/', views.HomeDetailView.as_view(), name='home-detail'),
    path('home-json/<str:slug>/', views.homeJson, name='home-json'),

]
