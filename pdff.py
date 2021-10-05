from PyPDF2 import PdfFileMerger
#as we are dealing with files 
import os 
#var = os.getcwd() For extracting from enother folder
merger = PdfFileMerger()
for items in os.listdir():
  if items.endswith('.pdf'):
    merger.append(items)
merger.write("Final_pdf.pdf")
merger = PdfFileMerger()

merger.close()
