import os
import pdfplumber
import re
import warnings

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
    Extract text from a list of PDF file paths.

    Args:
    pdf_paths (list): List of paths to PDF files.

    Returns:
    list: List of extracted text from each PDF file.
    """
    texts = []
    for pdf_path in pdf_paths:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ''
                for page in pdf.pages:
                    try:
                        text += page.extract_text() or ''
                    except Exception as e:
                        print(f"An error occurred while extracting text from page: {e}")
                texts.append(text)
        except Exception as e:
            print(f"An error occurred while processing file {pdf_path}: {e}")
    return texts

def clean_text(text):
    """
    Clean the extracted text by removing extra whitespace and newlines.

    Args:
    text (str): The text to be cleaned.

    Returns:
    str: The cleaned text.
    """
    # Remove extra whitespace and newlines
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

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
        split_texts.extend(re.split(regex_pattern, text))
    return split_texts
