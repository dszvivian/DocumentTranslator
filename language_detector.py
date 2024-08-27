from langdetect import  detect



# What if given text is random and not what we expect
def detect_language(text:str):
    return detect(text)