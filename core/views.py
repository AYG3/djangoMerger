from django.shortcuts import render, HttpResponse

from .forms import pdfAcceptForm

def base(request):
    if request.method == 'POST':
        form = pdfAcceptForm(request.POST, request.FILES)

        if form.is_valid():
            
            
            return HttpResponse('Form is valid')
    else:
        form = pdfAcceptForm()
    return render(request, 'core/index.html', {'form': form})