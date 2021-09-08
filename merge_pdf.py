"""
合并pdf
"""
import PyPDF2

PDF_PATH_1 = '绿能册子（上）.pdf'
PDF_PATH_2 = '绿能册子（下）.pdf'
OUTPUT_PATH = 'output.pdf'
PDF_PATHS = [PDF_PATH_1, PDF_PATH_2]

pdf_writer = PyPDF2.PdfFileWriter()
for path in PDF_PATHS:
    pdf_reader = PyPDF2.PdfFileReader(path)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
    with open(OUTPUT_PATH, 'wb') as o:
        pdf_writer.write(o)
