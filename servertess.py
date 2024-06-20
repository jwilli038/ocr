from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pytesseract
from PIL import Image
from fastapi import File, UploadFile
import shutil

app = FastAPI()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Configure CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    try:
        file_location = "uploaded_image.png"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
        
        image = Image.open(file_location)

        if image.mode != 'RGB':
            image = image.convert('RGB')

        text = pytesseract.image_to_string(image)
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}
