from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_prefix):
    with open(input_pdf, 'rb') as file:
        reader = PdfReader(file)
        
        # Loop through each page in the PDF
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            
            # Construct output filename
            output_filename = f"{output_prefix}_{i + 1}.pdf"
            
            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)
                print(f'Page {i + 1} saved as {output_filename}')