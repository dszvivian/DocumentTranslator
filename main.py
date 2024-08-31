from document_creation import DocumentCreation
from document_processor import DocumentProcessor
    
path = "test.pdf"

doc = DocumentCreation(path)
doc.process_pages()
doc.save_new_doc()


# from document_processor import DocumentProcessor
# from translator import Translator

# reader =  DocumentProcessor('./Input_Test_PDF1.pdf')


# reader.extract_all_text()




