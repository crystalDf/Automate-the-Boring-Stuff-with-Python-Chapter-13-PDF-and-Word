import PyPDF2

pdf1_file = open('meetingminutes.pdf', 'rb')
pdf2_file = open('meetingminutes2.pdf', 'rb')

pdf1_reader = PyPDF2.PdfFileReader(pdf1_file)
pdf2_reader = PyPDF2.PdfFileReader(pdf2_file)

pdf_combine_writer = PyPDF2.PdfFileWriter()


def write_page(pdf_reader, pdf_writer):
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)


write_page(pdf1_reader, pdf_combine_writer)
write_page(pdf2_reader, pdf_combine_writer)

pdf_output_file = open('combinedminutes.pdf', 'wb')
pdf_combine_writer.write(pdf_output_file)
pdf_output_file.close()
pdf1_file.close()
pdf2_file.close()
