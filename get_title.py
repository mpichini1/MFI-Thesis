import PyPDF2
from PyPDF2 import PdfFileReader
from pdfrw import PdfReader

input = PyPDF2.PdfFileReader('C:/Users/mpich/Desktop/MFI-Thesis/KIID/Bond/LU0441497293.pdf')
if input.isEncrypted:
    input.decrypt('')

def get_pdf_title(pdf_file_path):

    return PdfReader().Info.Title
    #return input.getDocumentInfo().title

title = get_pdf_title('C:/Users/mpich/Desktop/MFI-Thesis/KIID/Bond/LU0441497293.pdf')

print(title)