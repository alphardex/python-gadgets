"""
将HTML转为word，注意把源码的编码设为utf-8
"""
from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()
new_parser.parse_html_file('1.html', '1.docx')