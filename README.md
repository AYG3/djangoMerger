# Simple Django PDF Merger

This project is a straightforward Django application designed to merge multiple PDF files into a single PDF document. It provides a user-friendly interface for uploading PDFs and then downloading the merged result.

## Features

- **PDF Upload**: Users can upload multiple PDF files.
- **Merge PDF**: With a single click, the selected PDFs are merged into one document.
- **Download**: Users can download the merged PDF file.

## Installation

To get this project up and running on your local machine, follow these steps:

1. Clone the Repository

```bash
git clone https://github.com/AYG3/djangomerger.git
cd djangoMerger

2. **Set up a virtual environment**

```bash

python -m venv env

# Activate the environment
# On Windows powershell
. .\env\Scripts\activate

# On Unix or MacOS
source env/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Migrations**

```bash
python manage.py migrate
```

5. **Start the Development Server**

```bash
python manage.py runserver
```

Now, navigate to `http://127.0.0.1:8000/` in your web browser to see the application in action.

## Usage

- Navigate to the home page.
- Use the "Upload PDF" button to upload the PDF files you want to merge.
- Click on "Merge" to merge the documents.
- Download the merged PDF.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

