from django.urls import path

from . import views
app_name = 'core'


urlpatterns = [
    path('', views.uploadPDF, name='upload_pdf'),
    path('merged/', views.mergePDF, name='merge')
]
