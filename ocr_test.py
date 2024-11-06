import pytesseract

text = pytesseract.image_to_string(cropped_box)
print("Extracted text:", text)
