# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install Tesseract and other dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 80 for the FastAPI app
EXPOSE 80

# Command to run the FastAPI server
CMD ["uvicorn", "servertess:app", "--host", "0.0.0.0", "--port", "80", "--reload"]