import pytesseract
from PIL import Image
from fastapi import FastAPI, File, UploadFile
import shutil

# Initialize FastAPI app
app = FastAPI()

# Explicitly set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    # Save the uploaded file
    with open("uploaded_image.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Load the image using PIL
    image = Image.open("uploaded_image.png")

    # Ensure the image is in RGB format (optional)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Return the extracted text
    return {"text": text}

# To run the server, use the command: uvicorn main:app --reload