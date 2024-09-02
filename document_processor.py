import io
import pymupdf
from ocr_engine import OcrEngine
from translator import LanguageTranslator
from PIL import Image, ImageDraw, ImageFont


class DocumentProcessor:

    # def __init__(self,path) -> None:
    #     self.reader = PdfReader(path)
    #     self.n_pages = len(self.reader.pages)

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
        self.translator = LanguageTranslator() 
        self.ocr_engine = OcrEngine()       


    def translate_page(page): 
        pass

    def translate_image(self,image):
        """
        returns translated Image Bytes
        """

        # Extract and Translate the text from image
        extracted_text = self.ocr_engine.process_image(image)

        # translated_text = extracted_text
        translated_text = self.translator.translate(extracted_text)

        # Create a New Image with the translated Text
        draw =  ImageDraw.Draw(image)
        font = ImageFont.load_default() 
        draw.text(
            (10,10),
            translated_text,
            font=font,
            fill=(255,0,0)  # Red Text for Visibility
            )
        
        # Convert image back to Bytes 
        img_bytes_arr = io.BytesIO()
        image.save(img_bytes_arr, format='PNG')
        img_bytes_arr = img_bytes_arr.getvalue()  # convert to Bytes

        return img_bytes_arr  






        


