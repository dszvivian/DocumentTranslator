Goal: 

- To Translate Documents from One Langugae to another
- Preserving document formatting
- Exploring different Ways of effectively doing it



Approach that i currently used:

- Looping through all the pages
- Extracting Text and Translating it 
- Using OCR to extract text from Image and Translate the Text 
- And placing the text on original image



Used Libraries:

-  Used PyMuPdf --> For all pdf realated operations
-  LangDetect --> For language detection
-  Translation
         --> Used googletrans to translate  ( Just for quick experimentation)
         --> End Goal: Use OpenNMT to train a model from Scratch


- Lines and Watermark
- Symbol and Lines should be preserved 


Bugs Encountered:

- If entire pdf is a image it coudln't extract text (maybe tessaract problem)
- It failed to convert from english to kannada 
- It Translates image but it places text upon Original Text
- Even for a smalll Document it Takes Very long time
    - Reason:  For each block we are making a googletrans API call