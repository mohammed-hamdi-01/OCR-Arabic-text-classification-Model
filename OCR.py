from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Update the path to where Tesseract is installed
# Load an image
image_path = 'C:\\Users\\Moham\\Downloads\\utopia.PNG'
img = Image.open(image_path)

# Specify language option
custom_config = r'--oem 3 --psm 6 -l ara'
text = pytesseract.image_to_string(img, config=custom_config)

print(text)
