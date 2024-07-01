import os
import re
import warnings
import fitz  # PyMuPDF
import pdfplumber
from nltk.tokenize import word_tokenize

# Suppress all UserWarnings from pdfplumber
warnings.filterwarnings('ignore', category=UserWarning)

def get_pdf_paths(folder_path):
    """
    Get all PDF file paths from the specified folder.

    Args:
    folder_path (str): Path to the folder containing PDF files.

    Returns:
    list: List of paths to PDF files.
    """
    pdf_paths = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_paths.append(os.path.join(folder_path, filename))
    return pdf_paths

def extract_text_from_pdfs(pdf_paths):
    """
    Extract text from a list of PDF file paths using both PyMuPDF and pdfplumber.

    Args:
    pdf_paths (list): List of paths to PDF files.

    Returns:
    list: List of extracted text from each PDF file.
    """
    texts = []
    for pdf_path in pdf_paths:
        text = ''
        # Try extracting text using pdfplumber
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    try:
                        text += page.extract_text() or ''
                    except Exception as e:
                        print(f"An error occurred while extracting text from page using pdfplumber: {e}")
        except Exception as e:
            print(f"An error occurred while processing file with pdfplumber {pdf_path}: {e}")
        
        # Fallback to PyMuPDF if pdfplumber fails or returns empty text
        if not text:
            try:
                doc = fitz.open(pdf_path)
                for page in doc:
                    text += page.get_text()
                doc.close()
            except Exception as e:
                print(f"An error occurred while processing file with PyMuPDF {pdf_path}: {e}")

        texts.append(text)
    return texts

def clean_text(text):
    """
    Clean the extracted text by removing extra whitespace and newlines, and tokenizing.

    Args:
    text (str): The text to be cleaned.

    Returns:
    str: The cleaned and tokenized text.
    """
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.strip()  # Remove leading and trailing whitespace
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    return ' '.join(tokens)

def split_text_by_context(texts, regex_pattern):
    """
    Split text by a given regex pattern.

    Args:
    texts (list): List of text strings.
    regex_pattern (str): Regex pattern to split text contexts.

    Returns:
    list: List of text strings split by the regex pattern.
    """
    split_texts = []
    for text in texts:
        sections = re.split(regex_pattern, text)
        sections = [section.strip() for section in sections if section.strip()]  # Remove empty sections
        split_texts.extend(sections)
    return split_texts

def main(folder_path, context_split_regex):
    """
    Main function to process PDF files: extract, clean, and split text.

    Args:
    folder_path (str): Path to the folder containing PDF files.
    context_split_regex (str): Regex pattern to split text contexts.

    Returns:
    list: List of text strings split by the regex pattern.
    """
    pdf_paths = get_pdf_paths(folder_path)
    texts = extract_text_from_pdfs(pdf_paths)
    cleaned_texts = [clean_text(text) for text in texts]
    split_texts = split_text_by_context(cleaned_texts, context_split_regex)
    return split_texts

if __name__ == "__main__":
    folder_path = 'path_to_your_pdf_folder'
    context_split_regex = r'\n\n'  # Example regex for splitting by double newlines
    split_texts = main(folder_path, context_split_regex)
    print(split_texts)
