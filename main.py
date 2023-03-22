import PyPDF2


file = open('source.pdf', 'rb') #The source that needs to be seperated

reader = PyPDF2.PdfFileReader(file)

for page_num in range(reader.getNumPages()):
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(reader.getPage(page_num))
    outputName = 'output_{}.pdf'.format(page_num+1)
    outputFile = open(outputName, 'wb')
    writer.write(outputFile)
    outputFile.close()

file.close()
