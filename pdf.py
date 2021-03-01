import os
import PyPDF2
import img2pdf
from pathlib import Path

pdfWriter = PyPDF2.PdfFileWriter()

# Create pdfs from images
for filename in os.listdir():
    if filename.endswith(".png"):
        with open(f"image_pages/{filename}.pdf", "wb") as f:
            f.write(img2pdf.convert([filename]))

# concat all pdfs
pdfs = []
files = os.listdir() + ['image_pages/' + f for f in os.listdir('image_pages')]
files = [f for f in files if os.path.splitext(f)[1] == ".pdf"]
files = sorted(files, key=lambda f: int(Path(f).name.split(".")[0]))
for filename in files:
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
