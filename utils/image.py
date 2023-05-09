import pytesseract
from PIL import Image
import io
import base64


"""with open("C:/Users/Ala/Desktop/gptextra-backend/utils/image.png","rb") as f:
    img_bytes = f.read()

# Encode the image bytes as a base64 string
b64img = base64.b64encode(img_bytes).decode('utf-8')
"""

def image_to_text(b64img):
    # Decode the base64 string to bytes and create a PIL Image object

    img_data = base64.b64decode(b64img)
    img = Image.open(io.BytesIO(img_data))

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Convert the image to grayscale
    img = img.convert('L')

    # Use pytesseract to extract text from the image
    image_text = pytesseract.image_to_string(img)
    return image_text
    
