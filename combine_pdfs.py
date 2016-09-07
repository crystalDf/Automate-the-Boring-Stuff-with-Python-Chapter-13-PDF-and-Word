#! python3
# combine_pdfs.py - Combines all the PDFs in the current working directory
# into a single PDF.

import PyPDF2
import os

# Get all the PDF filenames.
pdf_files = []
for filename in os.listdir('./toBeCombined'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)
pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdf_files:
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Loop through all the pages (except the first) and add them.
    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

# Save the resulting PDF to a file.

