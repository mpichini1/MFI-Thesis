from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
import io 
import os
from pdfminer.converter import TextConverter
resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle)
page_interpreter = PDFPageInterpreter(resource_manager, converter)


def pdfreading():

		
	with open('C:/Users/mpich/Desktop/MFI-Thesis/KIID/Bond/LU0154237225.pdf', 'rb') as fh:

		for page in PDFPage.get_pages(fh,
			caching=True,
			check_extractable=False):
			page_interpreter.process_page(page)

			text = fake_file_handle.getvalue()

	# close open handles
	converter.close()
	fake_file_handle.close()

	
	
	return text

print(pdfreading())

