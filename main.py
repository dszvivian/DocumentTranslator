from document_creation import DocumentCreation
from document_processor import DocumentProcessor
    
path = "test.pdf"

doc = DocumentCreation(path)
doc.process_pages()
doc.save_new_doc()




