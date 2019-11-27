from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
import io 
import os
from pdfminer.converter import TextConverter
from Crypto.Cipher import AES
from Crypto import Random

output =[ 'Balanced', 'Equity', 'ETF','Flexible', 'Bond' ]

list1 = {}
for directory in output:
    list1[directory] = os.listdir('C:/Users/mpich/Desktop/MFI-Thesis/KIID/'+directory)

def pdfreading():
    tesi ={}
    for i in list1:
        for j in list1[i]:
            rsrcmgr = PDFResourceManager()
            retstr = io.StringIO()
            device = TextConverter(rsrcmgr, retstr)
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            pagenos = set()

            with open('C:/Users/mpich/Desktop/MFI-Thesis/KIID/'+i+'/'+j, 'rb') as fh:
                for page in PDFPage.get_pages(fh,
                                              pagenos,
                                              caching=True,
                                              password = password,
                                              check_extractable=False):
                    interpreter.process_page(page)
                    text = retstr.getvalue()
                    # close open handles
                    tesi[i,j] = text 
    device.close()
    retstr.close()
    
    
    return tesi
    
