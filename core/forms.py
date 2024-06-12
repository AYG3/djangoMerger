from django import forms

from .models import PDFmodel

class pdfAcceptForm(forms.ModelForm):
    forms_file = forms.FileField()