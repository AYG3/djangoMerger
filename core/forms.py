from django import forms

from .models import PDFmodel

class pdfAcceptForm(forms.ModelForm):
    class Meta:
        model: PDFmodel
        fields = ('pdf',)