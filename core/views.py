from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os

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
            
                #save pdf files
                file_path = 'media/uploads/' + file.name
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                saved_file_paths.append(file_path)

            request.session['uploaded_files'] = [saved_file_paths]

            return render(request, 'core/index.html', {'form': form, 'files': files })
            # return HttpResponse('Form is valid' + str(file) + '   Second pdf file:   ' + str(files) + '\n The file lenght is:  ' + file_len)
    else:
        form = pdfAcceptForm()
        return render(request, 'core/index.html', {'form': form, 'files': [] })

def mergePDF(request):
    try:
        merger = PyPDF2.PdfMerger()
        uploaded_files = request.session.get('uploaded_files', [])
        
        if not uploaded_files:
            return HttpResponse('No files uploaded')

        for file_path in uploaded_files[0]:
            with open(file_path, 'rb') as pdf_file:
                merger.append(pdf_file)

        output_file_name = 'Merged-' + os.path.basename(uploaded_files[0][0])
        output_file_path = os.path.join('media', 'uploads', output_file_name)

        with open(output_file_path, 'wb') as output_file:
            merger.write(output_file)

        # Optionally, clear session data here or after download
        # del request.session['uploaded_files']

        # Redirect to a new URL to download the merged file or show a success message
        # return HttpResponseRedirect(reverse('your_download_view_name'))
        return HttpResponseRedirect('Files succesfully merged')
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}')