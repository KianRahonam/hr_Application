loc = "C:Users/MANOHARA NAIK/OneDrive/Desktop/Offer Letter - Sameer Pasha.pdf"

import PyPDF2

def edit_pdf(input_path, output_path, new_text):
    # Open the PDF file in binary mode
    with open(input_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()

        # Iterate through all pages of the PDF
        for page_number in range(pdf_reader.numPages):
            # Get the current page
            page = pdf_reader.getPage(page_number)

            # Add new text to the page (you can customize this part)
            page.mergePage(new_text.getPage(page_number))

            # Add the modified page to the PDF writer
            pdf_writer.addPage(page)

        # Write the changes to the output PDF file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    # Specify the paths for your input and output PDF files
    input_pdf_path = loc
    output_pdf_path = "C:/Users/MANOHARA NAIK/OneDrive/Desktop/"

    # Create a PDF file containing the new text
    new_text = PyPDF2.PdfReader("C:/Users/MANOHARA NAIK/OneDrive/Desktop/Letter of Offer - Shrikant Balkrishna Chaurasiya.pdf")

    # Edit the PDF
    edit_pdf(input_pdf_path, output_pdf_path, new_text)

    print("PDF edited successfully.")
