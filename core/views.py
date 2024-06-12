from django.shortcuts import render, HttpResponse

from .forms import pdfAcceptForm

def base(request):
    if request.method == 'POST':
        form = pdfAcceptForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['forms_file']
            files = request.FILES.getlist('forms_file')[-1]
        
            if not str(file).endswith('.pdf'):
                return HttpResponse('File is not a pdf file:  ' + str(file))
            
            return HttpResponse('Form is valid' + str(file) + '   Second pdf file:   ' + str(files))
    else:
        form = pdfAcceptForm()
    return render(request, 'core/index.html', {'form': form})