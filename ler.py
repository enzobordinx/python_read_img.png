import cv2
import pytesseract

#Set the path for the tesseract data
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#Read the image
image = cv2.imread("C:\imagemlindek\img.png")

#Run the OCR on the image
text = pytesseract.image_to_string(image)

#Print the text
print(text)
