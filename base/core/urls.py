from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('projects/ecommerce/', views.EcommerceView.as_view(), name='ecommerce'),
    # path('projects/drifter/', views.DrifterView.as_view(), name='drifter'),
    # path('projects/canvasdownloader/', views.CanvasDownloaderView.as_view(), name='canvasDownloader'),
    # path('resume/', views.pdf_view, name='resume'),

]
