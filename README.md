#This Python script uses the OpenCV and Pytesseract libraries to perform Optical Character Recognition (OCR) on an image. The script first sets the path for the #Tesseract data, then reads in an image using OpenCV's imread function. It then runs the OCR process on the image using Pytesseract's image_to_string method, and finally #prints out the extracted text. This script can be used for tasks such as extracting text from images of documents, receipts, or other sources where the text is not #easily copyable.


 _______  _______  _______  _______  _______  _______  _______  _______ 
|       ||       ||   _   ||       ||       ||       ||       ||       |
|  _____||    ___||  |_|  ||_     _||  _____||_     _||    ___||_     _|
| |_____ |   |___ |       |  |   |  | |_____   |   |  |   |___   |   |  
|_____  ||    ___||       |  |   |  |_____  |  |   |  |    ___|  |   |  
 _____| ||   |___ |   _   |  |   |   _____| |  |   |  |   |___   |   |  
|_______||_______||__| |__|  |___|  |_______|  |___|  |_______|  |___|  


OCR Image Text Extractor
This is a simple Python script that uses the OpenCV and Pytesseract libraries to extract text from an image.

Installation
Clone the repository to your local machine using git clone https://github.com/enzobordinx/ocr-image-text-extractor.git.
Install the required libraries using pip install opencv-python pytesseract.
Usage
Place the image you want to extract text from in the same directory as the script.
Update the path for Tesseract OCR by modifying pytesseract.pytesseract.tesseract_cmd to match the installation location of Tesseract OCR on your system.
Modify the path for the image you want to extract text from by modifying cv2.imread() to match the path to the image on your system.
Run the script using python ocr_image_text_extractor.py.
The extracted text will be printed to the console.
Dependencies
This script depends on the following Python libraries:

OpenCV
Pytesseract
Contributing
If you find any issues with the script or want to contribute, feel free to open a pull request or submit an issue in the repository.

License
This project is licensed under the MIT license.
