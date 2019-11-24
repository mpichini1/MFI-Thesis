import PyPDF2
from PyPDF2 import PdfFileReader


input = PyPDF2.PdfFileReader('C:/Users/mpich/Desktop/MFI-Thesis/KIID/Balanced/LU0622328622.pdf')
if input.isEncrypted:
    input.decrypt('')

def get_pdf_title(pdf_file_path):

    
    return input.getDocumentInfo().title

title = get_pdf_title('C:/Users/mpich/Desktop/MFI-Thesis/KIID/Balanced/LU0622328622.pdf')

print(title)