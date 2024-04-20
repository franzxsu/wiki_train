import PyPDF2

pdf_path = '26464371-pie-bible.pdf'
text_data = []
with open(pdf_path, 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text_data.append(page.extract_text())

txt_path = 'output.txt'
with open(txt_path, 'w', encoding='utf-8') as txtfile:
    for text in text_data:
        txtfile.write(text + '\n\n')