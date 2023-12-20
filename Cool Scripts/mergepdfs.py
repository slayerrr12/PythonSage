"""
Merge two PDF files into one.
"""

import PyPDF2

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    # Open the PDFs in binary mode
    with open(pdf1_path, 'rb') as pdf1_file, open(pdf2_path, 'rb') as pdf2_file:
        # Create PDF reader objects
        pdf1_reader = PyPDF2.PdfReader(pdf1_file)
        pdf2_reader = PyPDF2.PdfReader(pdf2_file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add pages from the first PDF
        for page_num in range(len(pdf1_reader.pages)):
            page = pdf1_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Add pages from the second PDF
        for page_num in range(len(pdf2_reader.pages)):
            page = pdf2_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Write the merged PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

PDF2_PATH = r'C:\Users\hp\Desktop\Adobe Scan 31-Oct-2023.pdf'
PDF1_PATH = r'C:\Users\hp\Desktop\cd notes.pdf'
OUTPUT_PATH = r'C:\Users\hp\Desktop\Merged.pdf'

merge_pdfs(PDF1_PATH, PDF2_PATH, OUTPUT_PATH)
