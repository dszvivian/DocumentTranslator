import io
import pymupdf
from PIL import Image
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

            # Process Images
            image_list = page.get_images(full=True)

            # for img_index, img in enumerate(image_list):

            #     # xref = img[0]
            #     # base_image = self.doc.extract_image(xref)

            #     print("    ------------------     ")


            #     xref = img[0]
            #     base_image = self.doc.extract_image(xref)
            #     image_bytes =  base_image["image"]


                
            #     # print(image_bytes)

            #     Image.open(io.BytesIO(image_bytes))


            #     print("    ------------------     ")
            #     break 



            

            # Gets the text blocks and all its meta data in a Dictionary
            for block in page.get_text("dict")["blocks"]:

                # Process the Image Block
                if block["type"] == 1:
                    image = Image.open(io.BytesIO(block["image"]))

                    try:

                        translated_image_bytes = self.translate_image(image)

                    except Exception as e:
                        print("Error while Translating image")
                        print("Replaced with Original Image")

                        translated_image_bytes = block["image"]


                    # Insert the modified Image
                    image_rect =  block["bbox"]
                    current_page.insert_image(
                        image_rect,
                        stream=translated_image_bytes
                        )




                # Process the Text Blocks
                if block["type"] == 0:  # type == 0 --> Textblock 1 -->Image Block ... etc....
                    for line in block["lines"]:
                        for span in line["spans"]:   # span is a contioguous sequence of characters with same font and style
                            original_text = span["text"]
                            font_size = span["size"]
                            color = span["color"]
                            origin = span["origin"]
                            font = span["font"]

                            try:
                                translated_text = self.translator.translate(
                                    original_text
                                )
                            except Exception as e:
                                print(f"Error translating text(ie: So replaced with original text)")
                                print(e)
                                translated_text = original_text


                            print(translated_text)


                            # todo: Fix font and color
                            current_page.insert_text(
                                origin,
                                translated_text,
                                # fontname=font,
                                fontsize=font_size
                                # color=color
                            )                    




    def save_new_doc(self):
        self.new_doc.save('test_translated.pdf')
