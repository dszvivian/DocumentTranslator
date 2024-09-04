from pdftranslator.document_creation import DocumentCreation


path = 'test.pdf'
doc_processor =  DocumentCreation(path)
doc_processor.process_pages()
doc_processor.save_new_doc(path='test_translated.pdf')