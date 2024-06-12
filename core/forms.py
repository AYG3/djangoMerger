from django import forms

from .models import PDFmodel

class pdfAcceptForm(forms.ModelForm):
    pdf = forms.FileField()