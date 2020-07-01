"""
从pdf中提取一定页数
"""
import PyPDF2

PDF_PATH = '昆承英才  智惠常熟.pdf'
OUTPUT_PATH = 'output.pdf'
PDF_START_PAGE = 7
PDF_END_PAGE = 15

pdf_reader = PyPDF2.PdfFileReader(open(PDF_PATH, 'rb'))
pdf_writer = PyPDF2.PdfFileWriter()
for page in range(PDF_START_PAGE-1, PDF_END_PAGE):
    pdf_writer.addPage(pdf_reader.getPage(page))
    with open(OUTPUT_PATH, 'wb') as o:
        pdf_writer.write(o)
