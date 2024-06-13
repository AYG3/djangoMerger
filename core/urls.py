from django.urls import path

from . import views

urlpatterns = [
    path('', views.uploadPDF, name='upload_pdf'),
    path('merge/', views.mergePDF, name='merge')
]
