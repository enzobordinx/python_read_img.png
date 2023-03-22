import cv2
import pytesseract
import os
from PIL import Image

def preprocess_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return threshold_image

# Set the path for the Tesseract data
tesseract_path = os.path.join(os.environ.get("ProgramFiles"), "Tesseract-OCR", "tesseract.exe")

if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    print("Error: Tesseract-OCR not found. Please install Tesseract-OCR and try again.")
    exit(1)

# Read the image
image_path = r"C:\imagemlindek\img.png"

if os.path.exists(image_path):
    image = cv2.imread(image_path)
else:
    print("Error: Image not found. Please check the image path and try again.")
    exit(1)

# Preprocess the image
preprocessed_image = preprocess_image(image)

# Run the OCR on the image
text = pytesseract.image_to_string(preprocessed_image)

# Print the text
print(text)
