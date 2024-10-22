# Required libraries
from pdf2image import convert_from_path
from PIL import Image
import io
import os
import re
from google.cloud import vision
from google.oauth2 import service_account

pdf_files = int
OUTPUT_TXT = '.txt'  # Path to the output text file

# create the file if it does not exist
if not os.path.exists(OUTPUT_TXT):
    open(OUTPUT_TXT, 'w').close()

# Path to your service account key (JSON file) for Google Cloud Vision
credentials_path = "testing-project-438410-37afea7eac69.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Initialize Google Cloud Vision client
client = vision.ImageAnnotatorClient(credentials=credentials)

# Function to extract text from images using OCR
def ocr_image(image_path):
    # Loads the image into memory
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f'API error: {response.error.message}')
   
    # The first result in text_annotations is the entire text detected
    if texts:
        full_text = texts[0].description
        print(f'{image_path} completed')
        return full_text
    return ""

# Function to remove page numbers from text
def remove_page_numbers(text):
    cleaned_text = re.sub(r'\b(Page\s*)?\d+\b', '', text)
    return cleaned_text.strip()

# Function to extract the numeric page number from the filename
def extract_page_number(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group(0)) if match else -1  # Return the number found in the filename, or -1 if no number is found


for i in range(1, pdf_files+1):
    print(f'Processing PDF {i}...')
    
    # INPUT_PDF = '.pdf'  # Path to the input PDF file
    INPUT_PDF = f'{i}.pdf'

    # Convert the PDF to images
    images = convert_from_path(INPUT_PDF)

    # Save each cropped page as an image
    for j, image in enumerate(images):
        image.save(f'page_{j}.png', 'PNG')

    # Initialize a variable to hold all text
    all_text = ""

    # Run OCR on each page image and accumulate text
    # Sort the filenames based on the numeric value of page numbers
    for filename in sorted(os.listdir('.'), key=extract_page_number):
        if filename.endswith('.png'):
            # Perform OCR
            text = ocr_image(filename)
            cleaned_text = remove_page_numbers(text)
            all_text += cleaned_text + "\n\n"  # Add spacing between images
            
            # Delete the image file after processing
            os.remove(filename)
            print(f'{filename} deleted')

    # Save all the extracted text to a single .txt file - if not created, it will be created

    with open(OUTPUT_TXT, 'a') as f:
        f.write(all_text)

    print(f'PDF {i} completed')