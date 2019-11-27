import get_title
import re

text = get_title.pdfreading()

for i in text.values(): 

	m = re.search("\w\w\d\d\d\d\d\d\d\d\d\d", i)

	if m:
	   
	   print(m.group(0)) 

	else:
	    n = re.search("\w\w\d\d\w\w\w\w\w\w\d\d",i)

	    print(n.group(0))

  


