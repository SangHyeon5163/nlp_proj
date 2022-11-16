from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO 
from io import open 
from urllib.request import urlopen

def read_pdf_file(pdfFile): 
    rsrcmgr = PDFResourceManager()
    retstr = StringIO() 
    laparams = LAParams() 
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close() 

    content = retstr.getvalue() 
    retstr.close() 
    return content

pdf_file = open("data/cpu-gpu.pdf", "rb")
contents = read_pdf_file(pdf_file)
print(contents)
pdf_file.close()
