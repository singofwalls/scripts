from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("input.pdf", "rb"))

pages = "5-20, 22-37, 39-46, 48-55, 57-64, 66-71, 73-79"
pages = [range(*[int(l) for l in r.split("-")]) for r in pages.split(", ")]

output = PdfFileWriter()
for r in pages:
    for p in r:
        output.addPage(inputpdf.getPage(p))

with open("output.pdf", "wb") as outputStream:
    output.write(outputStream)
