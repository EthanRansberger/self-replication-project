import os
import fitz  # PyMuPDF
import re
from nltk.tokenize import word_tokenize

def get_pdf_paths(folder_path):
    """Returns a list of all PDF file paths in the given folder."""
    pdf_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pdf')]
    return pdf_paths

def extract_text_from_pdfs(pdf_paths):
    texts = []
    for path in pdf_paths:
        doc = fitz.open(path)
        for page in doc:
            texts.append(page.get_text())
    return texts

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    return ' '.join(tokens)

def split_text_by_context(texts, context_split_regex):
    split_texts = []
    for text in texts:
        sections = re.split(context_split_regex, text)
        split_texts.extend(sections)
    return split_texts
