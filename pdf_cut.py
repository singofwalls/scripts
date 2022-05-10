from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("input.pdf", "rb"))

output = PdfFileWriter()
output.addPage(inputpdf.getPage(1))
with open("output.pdf", "wb") as outputStream:
    output.write(outputStream)
