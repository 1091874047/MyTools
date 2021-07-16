from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('img_1.png'), lang='chi_sim')
print(text.strip().replace(" ",""))
