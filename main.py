from document_processor import DocumentProcessor
from translator import Translator

reader =  DocumentProcessor('./Input_Test_PDF1.pdf')


reader.extract_all_text()
