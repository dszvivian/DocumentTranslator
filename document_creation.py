import pymupdf

from document_processor import DocumentProcessor



class DocumentCreation(DocumentProcessor):
    

    def __init__(self,path):
        super().__init__(path)
        self.new_doc =  pymupdf.open()

    def process_pages(self):

        for page in self.doc:

            self.new_doc.insert_page(-1,
                                  text = page.get_text(),
                                  width = 595,
                                  height = 842
                                  )
            

            

    def save_new_doc(self):
        self.new_doc.save('test_translated.pdf')



    

    

    
     

