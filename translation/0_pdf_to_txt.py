#from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO 
from io import open 
from urllib.request import urlopen

def read_pdf_file(pdfFile): 
    rsrcmgr = PDFResourceManager()
    retstr = StringIO() 
    laparams = LAParams() 
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    password = "" 
    maxpages = 0 
    caching = True
    pagenos=set()

    #process_pdf(rsrcmgr, device, pdfFile)
    interpreter = PDFPageInterpreter(rsrcmgr, device)


    #device.close() 
    
    for page in PDFPage.get_pages(pdf_file, pagenos, maxpages=maxpages, password=password, caching=caching,
            check_extractable=True): 
        interpreter.process_page(page)
    content = retstr.getvalue() 
    
    device.close()
    retstr.close() 
    return content

pdf_file = open("data/cpu-gpu.pdf", "rb")
contents = read_pdf_file(pdf_file)
print(contents)
pdf_file.close()
