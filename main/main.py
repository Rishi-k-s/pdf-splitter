import pdf_splitter
# import main.pdf_merger as pdf_merger
import pdf_merger
import os


inputFilePath = r"pdfSource"
splittedFilePath = r"pdfOutput"

def main():
    dir_list = os.listdir(inputFilePath)
    splittedPdfList = os.listdir(splittedFilePath)

    print("Files and directories in '", inputFilePath, "' :")
    print(dir_list)
    print(splittedFilePath)

    for eachPdf in range(0,len(dir_list)):
        pdf_splitter.split_pages2( r"pdfSource\{}".format(dir_list[eachPdf]),r"pdfOutput\page{}+{}.pdf".format(eachPdf+1,eachPdf+2))
    # TODO: Make all the strings the same, like all words into a variable
    # for eachSplitPdf in splittedPdfList: 
    #     print(eachSplitPdf)
    #     pdf_merger.merge_Pages(r"pdfOutput\{}".format(eachSplitPdf),r"pdfMergeOutput\merged.pdf")
    #     print("FOrmat Compete")
    pdf_merger.merge_Pages(splittedPdfList,r"pdfMergeOutput\merged.pdf")

if __name__ == "__main__":
    main()
