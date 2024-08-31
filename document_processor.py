import io
import pymupdf
from ocr_engine import OcrEngine
from translator import LanguageTranslator
from PIL import Image 


class DocumentProcessor:

    # def __init__(self,path) -> None:
    #     self.reader = PdfReader(path)
    #     self.n_pages = len(self.reader.pages)

    #     self.translator = LanguageTranslator() 
    #     self.ocr_engine = OcrEngine()       

    # def translate_page(self,page_number):
    #     page =  self.reader.pages[page_number]
    #     extracted_text = page.extract_text()

    #     if extracted_text == '':
    #         print("Empty String")
    #     else:
    #         return self.translator.translate(text=extracted_text)
        # return extracted_text
    
    # def translate_image(self,page_number):
    #     page =  self.reader.pages[page_number]

    #     for image_file_object in page.images:

    #         image_bytes = image_file_object.data 

    #         base_image = Image.open(io.BytesIO(image_bytes))
            
    #         image_text = self.ocr_engine.process_image(base_image)

    #         return self.translator.translate(image_text)


    def __init__(self,path):
        self.doc = pymupdf.open(path) 

    def translate_page(page): 
        pass

    def translate_image(page):
        pass


