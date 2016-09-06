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

# TODO: Loop through all the PDF files.
# TODO: Loop through all the pages (except the first) and add them.
# TODO: Save the resulting PDF to a file.

