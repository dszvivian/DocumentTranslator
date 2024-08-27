from googletrans import Translator 


class LanguageTranslator:

    def __init__(self) -> None:
        self.translator =  Translator()

    
    def translate(self,text,target_language='en'):
        

        len_text = len(text)


        if len_text > 5000:
            

            mid =  len_text // 2

            first_half =  self.translate(text[0:mid])
            second_half =  self.translate(text[mid:])

            return  first_half + second_half


        else:
            return self.translator.translate(text,dest=target_language).text
            return GoogleTranslator(source='auto', target='de').translate(text)
