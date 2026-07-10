"""
提取PDF所有文字
"""
import fitz  # pymupdf

pdf_path = "input.pdf"
output_path = "output.txt"

doc = fitz.open(pdf_path)

all_text = []

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text("text")
    all_text.append(f"\n===== 第 {page_num + 1} 页 =====\n")
    all_text.append(text)

doc.close()

# 保存到 txt
with open(output_path, "w", encoding="utf-8") as f:
    f.write("".join(all_text))

print(f"提取完成，共 {len(doc)} 页，结果已保存至 {output_path}")