from django.db import models

# Create your models here.
class PDFmodel(models.Model):
    merged_name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

