import os
import PyPDF2
import img2pdf

pdfWriter = PyPDF2.PdfFileWriter()

# Create pdfs from images
for filename in os.listdir():
    if filename.endswith(".jpg"):
        with open(f"image_pages/{filename}.pdf", "wb") as f:
            f.write(img2pdf.convert([filename]))

# concat all pdfs
pdfs = []
for filename in os.listdir() + ['image_pages/' + f for f in os.listdir('image_pages')]:
    if filename.endswith(".pdf"):
        pdf = open(filename, "rb")
        pdfs.append(pdf)
        pdfReader = PyPDF2.PdfFileReader(pdf)
        for page_num in range(pdfReader.numPages):
            page = pdfReader.getPage(page_num)
            pdfWriter.addPage(page)

with open("output/output.pdf", "wb") as f:
    pdfWriter.write(f)

for pdf in pdfs:
    pdf.close()
