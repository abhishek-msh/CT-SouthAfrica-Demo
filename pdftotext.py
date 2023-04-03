"""
Convert PDF to text using PyMuPDF, and clean the text.
Note: This script is not perfect. It is just a demo.

We have to manually do some text preprocessing as per our requirements.
"""
# !pip install PyMuPDF

import fitz
import re


path_to_pdf = r"C:\Users\abhis\Desktop\Celebal\Jay\EducationBot_SouthAfrica\sa-demo-data\Science\sci2.pdf"
path_to_text = r"C:\Users\abhis\Desktop\Celebal\Jay\EducationBot_SouthAfrica\sa-demo-data\Science\sci2.txt"

# open the pdf file
with fitz.open(path_to_pdf) as doc:
    #save the text to file
    with open(path_to_text, 'w', encoding="Utf-8") as f:
        for page in doc:
            text = page.get_text()
            text = text.replace('1', 'a')
            text = text.replace('2', 'b')
            text = text.replace('3', 'c')
            text = text.replace('4', 'e')
            text = text.replace('5', 'f')
            text = text.replace('6', 'g')
            text = text.replace('7', 'h')
            text = text.replace('8', 'i')
            text = text.replace('9', 'j')
            f.write(text)


def read_text(path_to_text):
    """Read text from file and remove non-alphanumeric characters."""
    with open(path_to_text, 'r', encoding="utf-8") as f:
        text = f.read()
        text = re.sub(r'[^\w\s?\.]', '', text)
        return text
    

def clean_text(text):
    """Split text into sentences and format them."""
    sentences = text.split('.')
    result = []
    for sentence in sentences:
        if len(sentence.strip()) > 0:
            sentence = sentence.strip()
            if sentence[-1] not in ('?', '.'):
                sentence += '.'
            result.append(sentence)
    return '\n'.join(result)


def save_text(text, path_to_text):
    """Save cleaned text to file."""
    with open(path_to_text, 'w', encoding="utf-8") as f:
        f.write(text)


# clean the text and save to file
text = read_text(path_to_text)
text = clean_text(text)
save_text(text, path_to_text)

print("Done!")

