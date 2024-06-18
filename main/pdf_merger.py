from PyPDF2 import PdfWriter

def merge_Pages(mergeList,dst):
    merger = PdfWriter()
    outputFile = open(dst, 'w+b')
    for eachFile in mergeList:
        with open(r"pdfOutput\{}".format(eachFile), 'r+b') as sourceFile:
            merger.append(sourceFile)
    merger.write(outputFile)
    merger.close()