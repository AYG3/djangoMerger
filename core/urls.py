from django.urls import path

from . import views
app_name = 'core'


urlpatterns = [
    path('', views.uploadPDF, name='upload_pdf'),
    path('merge/', views.mergePDF, name='merge')
]
