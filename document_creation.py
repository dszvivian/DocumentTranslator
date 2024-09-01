import pymupdf

from document_processor import DocumentProcessor



class DocumentCreation(DocumentProcessor):
    

    def __init__(self,path):
        super().__init__(path)
        self.new_doc =  pymupdf.open()

    def process_pages(self):

        for page in self.doc:

            current_page = self.new_doc.new_page(-1,
                                  width = page.rect.width,
                                  height = page.rect.height
                                  )
            
            # Process the Text Blocks

            # Gets the text blocks and all its meta data in a Dictionary
            for block in page.get_text("dict")["blocks"]:
                if block["type"] == 0:  # type == 0 --> Textblock 1 -->Image Block ... etc....
                    for line in block["lines"]:
                        for span in line["spans"]:   # span is a contioguous sequence of characters with same font and style
                            original_text = span["text"]
                            font_size = span["size"]
                            color = span["color"]
                            origin = span["origin"]
                            font = span["font"]

                            print(f"font={font}  fsize={font_size}")

                            current_page.insert_text(
                                origin,
                                original_text,
                                # fontname=font,
                                fontsize=font_size
                                # color=color
                            )                    




    def save_new_doc(self):
        self.new_doc.save('test_translated.pdf')
