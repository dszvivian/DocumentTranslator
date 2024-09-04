import io
import pymupdf
from pdftranslator.ocr_engine import OcrEngine
from pdftranslator.translator import LanguageTranslator
from PIL import Image, ImageDraw, ImageFont


class DocumentProcessor:

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






        


