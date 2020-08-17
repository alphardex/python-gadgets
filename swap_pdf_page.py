"""
将pdf的第一页与最后一页互换
"""
import PyPDF2

PDF_PATH = 'output.pdf'
OUTPUT_PATH = 'output-swap.pdf'
PDF_START_PAGE = 1
PDF_END_PAGE = 48

pdf_reader = PyPDF2.PdfFileReader(open(PDF_PATH, 'rb'))
pdf_writer = PyPDF2.PdfFileWriter()
pages = list(range(PDF_START_PAGE-1, PDF_END_PAGE+1))
pages[0], pages[-1] = pages[-1], pages[0]
for page in pages[1:]:
    pdf_writer.addPage(pdf_reader.getPage(page))
    with open(OUTPUT_PATH, 'wb') as o:
        pdf_writer.write(o)
