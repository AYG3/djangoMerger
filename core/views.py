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
    merger = PyPDF2.PdfMerger()
    uploaded_files = request.session.get('uploaded_files', [])
    # Loop through all files in the current directory    
    for file_path in uploaded_files[0]:
        with open(file_path, 'rb') as pdf_file:
            merger.append(pdf_file)

    output_file_name = str(uploaded_files[0][0]) + '.pdf'
    output_file_path = f'media/uploads/' + output_file_name #attempt to change to'Merged -  first file name'

    print(end='n\n\n\n\n\n\n\n')
    print(f'Output file name = {output_file_name}')
    print(end='n\n\n\n\n\n\n\n')

    with open(output_file_path, 'wb') as output_file:
        merger.write(output_file)

    #clear session data
    del request.session['uploaded_files']

    output_file_url ='media/uploads/' + output_file_name

    # return HttpResponse('Files merged sucessfully')
    return render(request, 'core/index.py', { 'output_file_url': output_file_url })