OCR Setup with Tesseract and Python
This guide explains how to set up the environment, install Tesseract OCR, and run the Python script for OCR.

Prerequisites
Python 3.x
pip (Python package installer)
Step 1: Install Tesseract OCR
For Windows
Download Tesseract Installer:

Download the Tesseract installer from UB Mannheim's Tesseract repository.
Run the Installer:

Follow the installation instructions to complete the installation.
During installation, make note of the installation directory, typically C:\Program Files\Tesseract-OCR.
Add Tesseract to PATH:

Open the Start menu and search for "Environment Variables".
Click "Edit the system environment variables".
In the System Properties window, click the "Environment Variables" button.
In the Environment Variables window, under "System variables", find the Path variable, select it, and click "Edit".
Click "New" and add C:\Program Files\Tesseract-OCR.
Click "OK" to close all windows.
Verify Installation:

Open Command Prompt and type:
bash
Copy code
tesseract --version
You should see the version information of Tesseract OCR.
Step 2: Set Up Python Environment
Clone the Repository (or create your project directory):

bash
Copy code
git clone https://github.com/jwilli038/ocr.git
cd ocr
Create a Virtual Environment:

bash
Copy code
python -m venv .venv
Activate the Virtual Environment:

For Windows:

bash
Copy code
.venv\Scripts\activate
For macOS/Linux:

bash
Copy code
source .venv/bin/activate
Install Required Python Packages:

bash
Copy code
pip install pillow pytesseract
Step 3: Run the OCR Script
Create the Python Script:



python tesseract_ocr.py


This README provides detailed steps to set up the environment, install Tesseract OCR, and run the OCR script. Copy and paste this content into your README file. If you have any questions or encounter any issues, feel free to ask!
