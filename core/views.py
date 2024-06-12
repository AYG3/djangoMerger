from django.shortcuts import render

from .forms import pdfAcceptForm

def base(request):
    form = pdfAcceptForm(request.POST, request.FILES)
    return render(request, 'core/index.html', {'form': form})