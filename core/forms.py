from django import forms
from django.forms.widgets import ClearableFileInput

from .models import PDFmodel

# class pdfAcceptForm(forms.Form):
#     forms_file = forms.FileField(widget=forms.FileInput(attrs={
#         'class' : 'w-full py-4 px-6 rounded-xl border border-gray-400',
#         'multiple': True
#     }))

# class pdfAcceptForm(forms.Form): ...
class pdfAcceptForm(forms.Form):
    forms_file = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class' : 'w-full py-4 px-6 rounded-xl border border-gray-400',
    }))
