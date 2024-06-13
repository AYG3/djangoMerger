from django.shortcuts import render, HttpResponse
import PyPDF2
from .forms import pdfAcceptForm



def uploadPDF(request): 
    if request.method == 'POST':
        form = pdfAcceptForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('forms_file')
            saved_file_paths = []

            for file in files:
                if not str(file).endswith('.pdf'):
                    return HttpResponse('File is not a pdf file:  ' + str(file))
            
            #save files
            file_path = MEDIA_ROOT + file.name
            return render(request, 'core/index.html', {'form': form, 'files': files })
            # return HttpResponse('Form is valid' + str(file) + '   Second pdf file:   ' + str(files) + '\n The file lenght is:  ' + file_len)
    else:
        form = pdfAcceptForm()
        return render(request, 'core/index.html', {'form': form, 'files': [] })

def mergePDF(request):
    merger = PyPDF2.PdfMerger()

    # Loop through all files in the current directory
    for file in files:
        if file.endswith('.pdf'):
            # Open each PDF file and append it to the merger object
            with open(file, 'rb') as pdf_file:
                merger.append(pdf_file)

    # Write the merged PDF to a new file
        with open('Merged - ' + str(files[0]), 'wb') as output_file:
            output_file = merger.write(output_file)
    return render(request, 'core/index.py', {'output_file': output_file})




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