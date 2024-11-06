
import easyocr

def extract_text(image_path:str)->str:
    reader = easyocr.Reader(['en'])
    text = reader.readtext(image_path, detail=0) # detail=0 returns text only

    return text
    