"""
将pdf的一页切成2部分
"""
import PyPDF2

PDF_PATH = '昆承英才  智惠常熟.pdf'
OUTPUT_PATH = 'output.pdf'
PDF_START_PAGE = 1
PDF_END_PAGE = 9

pdf_reader = PyPDF2.PdfFileReader(open(PDF_PATH, 'rb'))
pdf_reader_2 = PyPDF2.PdfFileReader(open(PDF_PATH, 'rb'))
pdf_writer = PyPDF2.PdfFileWriter()
for page in range(PDF_START_PAGE-1, PDF_END_PAGE):
    origin_page = pdf_reader.getPage(page)
    origin_page_copy = pdf_reader_2.getPage(page)
    upperLeft = origin_page.mediaBox.getUpperLeft()
    upperRight = origin_page.mediaBox.getUpperRight()
    lowerLeft = origin_page.mediaBox.getLowerLeft()
    lowerRight = origin_page.mediaBox.getLowerRight()
    new_page_left_upperLeft = upperLeft
    new_page_left_lowerLeft = lowerLeft
    new_page_left_upperRight = tuple(a for a in upperRight)
    new_page_left_lowerRight = tuple(float(b / 2) for b in lowerRight)
    new_page_right_upperLeft = tuple(float(a / 2) for a in upperRight)
    new_page_right_lowerLeft = tuple(float(b / 2) for b in lowerRight)
    new_page_right_upperRight = upperRight
    new_page_right_lowerRight = lowerRight
    origin_page.cropBox.upperLeft = new_page_left_upperLeft
    origin_page.cropBox.lowerLeft = new_page_left_lowerLeft
    origin_page.cropBox.upperRight = new_page_left_upperRight
    origin_page.cropBox.lowerRight = new_page_left_lowerRight
    origin_page_copy.cropBox.upperLeft = new_page_right_upperLeft
    origin_page_copy.cropBox.lowerLeft = new_page_right_lowerLeft
    origin_page_copy.cropBox.upperRight = new_page_right_upperRight
    origin_page_copy.cropBox.lowerRight = new_page_right_lowerRight
    pdf_writer.addPage(origin_page)
    pdf_writer.addPage(origin_page_copy)

    with open(OUTPUT_PATH, 'wb') as o:
        pdf_writer.write(o)
