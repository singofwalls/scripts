from PyPDF2 import PdfFileWriter, PdfFileReader 

inputpdf = PdfFileReader(open("input.pdf", "rb"))

# Page ranges to add to output pdf
pages = "5-20, 22-37, 39-46, 48-55, 57-64, 66-71, 73-79"
pages = [range(*[int(l) for l in r.split("-")]) for r in pages.split(", ")]

output = PdfFileWriter()


def one_per_page():
    """Put one page on each page."""
    for r in pages:
        for p in r:
            output.addPage(inputpdf.getPage(p))

def two_by_two():
    """Put four pages on each page."""
    i = 0
    page = None
    for r in pages:
        for p in r:
            if i % 4 == 0:
                page = output.addBlankPage(inputpdf.getPage(0).mediaBox.getWidth(), inputpdf.getPage(0).mediaBox.getHeight())
                page.mergeScaledTranslatedPage(inputpdf.getPage(p), .5, 0, page.mediaBox.getHeight()/2)
            elif i % 4 == 1:
                page.mergeScaledTranslatedPage(inputpdf.getPage(p), .5, page.mediaBox.getWidth()/2, page.mediaBox.getHeight()/2)
            elif i % 4 == 2:
                page.mergeScaledTranslatedPage(inputpdf.getPage(p), .5, 0, 0)
            elif i % 4 == 3:
                page.mergeScaledTranslatedPage(inputpdf.getPage(p), .5, page.mediaBox.getWidth()/2, 0)
            i += 1


# one_per_page()
two_by_two()
with open("output.pdf", "wb") as outputStream:
    output.write(outputStream)
