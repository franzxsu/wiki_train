import fitz

pdf_path = '26464371-pie-bible.pdf'
text_data = []
doc = fitz.open(pdf_path)
for page in doc:
    text_data.append(page.get_text())

txt_path = 'output.txt'
with open(txt_path, 'w', encoding='utf-8') as txtfile:
    for text in text_data:
        txtfile.write(text + '\n\n')