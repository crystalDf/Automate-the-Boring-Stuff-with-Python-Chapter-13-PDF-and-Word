import PyPDF2

pdf_reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdf_reader.isEncrypted)

# pdf_reader.getPage(0)

print(pdf_reader.decrypt('rosebud'))
print(pdf_reader.getPage(0))
