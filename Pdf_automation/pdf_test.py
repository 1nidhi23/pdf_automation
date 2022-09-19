import PyPDF2
file = open("sample.pdf", "rb")
reader = PyPDF2.PdfFileReader(file)
print(reader.numPages)