import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class OcrEngine:

    def __init__(self,) -> None:
        pass 

    def process_image(self,image):
        return pytesseract.image_to_string(image)


    def processs_image_path(self):
        return pytesseract.image_to_string(self.path)
    
