import PyPDF2
f=open('path of pdf file.pdf', 'rb')
pdf_reader=PyPDF2.PdfFileReader(f)
print(pdf_reader.getXmpMetadata())
data=pdf_reader.getDocumentInfo()
print('----Metadata of the file---')
for metadata in data:
	print(metadata+ " : "+data[metadata])

