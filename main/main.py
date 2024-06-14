import pdf_reader_writer
import os


inputFilePath = r"pdfSource"

def main():
    dir_list = os.listdir(inputFilePath)
    print("Files and directories in '", inputFilePath, "' :")
    print(dir_list)
    for i in range(0,len(dir_list)):
        pdf_reader_writer.split_pages2( r"pdfSource\{}".format(dir_list[i]),r"pdfOutput\page{}+{}.pdf".format(i+1,i+2))

if __name__ == "__main__":
    main()
