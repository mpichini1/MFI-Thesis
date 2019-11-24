import read_pdf
import re

text = read_pdf.pdfreading()
 
m = re.search("\w\w\d\d\d\d\d\d\d\d\d\d", text)

if m:
   
   print(m.group(0)) 


else:
    n = re.search("\w\w\d\d\w\w\w\w\w\w\d\d",text)

    print(n.group(0))

  


