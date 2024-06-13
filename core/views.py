from django.shortcuts import render, HttpResponse

from .forms import pdfAcceptForm



def uploadPDF(request): 
    files = []
    if request.method == 'POST':
        form = pdfAcceptForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['forms_file']
            file_len = str(len(request.FILES.getlist('forms_file')))
            files = request.FILES.getlist('forms_file')
        
            if not str(file).endswith('.pdf'):
                return HttpResponse('File is not a pdf file:  ' + str(file))
            
            return render(request, 'core/index.html', {'form': form, 'files': files })
            # return HttpResponse('Form is valid' + str(file) + '   Second pdf file:   ' + str(files) + '\n The file lenght is:  ' + file_len)
    else:
        form = pdfAcceptForm()
        return render(request, 'core/index.html', {'form': form, 'files': files })

def mergePDF(request):
     
    return render(request, 'core/merge.py')




# def base(request):
#     context = {'form': None, 'files': []}  # Initialize context
#     if request.method == 'POST':
#         form = pdfAcceptForm(request.POST, request.FILES)
#         context['form'] = form  # Update form in context

#         if form.is_valid():
#             uploaded_files = request.FILES.getlist('forms_file')
#             valid_files = [file for file in uploaded_files if str(file).endswith('.pdf')]

#             if not valid_files:
#                 return HttpResponse('No valid PDF files uploaded.')

#             # Update files in context with the names of the uploaded PDF files
#             context['files'] = [str(file) for file in valid_files]

#             # You can add additional logic here if you need to process the files or save them

#             # Re-render the page with the updated context
#             return render(request, 'core/index.html', context)
#     else:
#         form = pdfAcceptForm()
#         context['form'] = form  # Update form in context

#     # Initial GET request or if the form is not valid, render the page with the initial or updated context
#     return render(request, 'core/index.html', context)