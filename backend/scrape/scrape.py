import pdfplumber

pdf_path = '26464371-pie-bible.pdf'
text_data = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text_data.append(page.extract_text())

txt_path = 'output.txt'
with open(txt_path, 'w', encoding='utf-8') as txtfile:
    for text in text_data:
        txtfile.write(text + '\n\n')