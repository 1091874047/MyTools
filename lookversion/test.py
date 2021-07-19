from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('20181215102103977.png'))
print(text.strip().replace(" ",""))
