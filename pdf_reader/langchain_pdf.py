from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

pdf_file = "GPC_DM.pdf"

pdf_reader = PdfReader(pdf_file)

print(pdf_reader)

if __name__ == "__main__":
	text = ""
	for page in pdf_reader.pages:
		text += page.extract_text()
 
		text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
		chunks = text_splitter.split_text(text=text)

		print(chunks)
