import os
import time
import pdfread
import modeltrainer
import textgenerator
from dataset import PandasDataset
import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import utils
import nltk
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to enable or disable logging
def set_logging(enabled):
    if enabled:
        logging.disable(logging.NOTSET)
    else:
        logging.disable(logging.CRITICAL)

nltk.download('punkt')

def main(folder_path, dataset_path, context_split_regex, enable_logging=True):
    start_time = time.time()  # Start timing the entire process

    # Enable or disable logging based on input
    set_logging(enable_logging)

    # Log start of initialization
    logger.info("Starting initialization...")

    # Step 1: Extract text from PDFs
    pdf_paths = pdfread.get_pdf_paths(folder_path)
    raw_texts = pdfread.extract_text_from_pdfs(pdf_paths)
    logger.info(f"Extracted text from {len(pdf_paths)} PDFs.")

    # Step 2: Clean the extracted text and split by context
    cleaned_texts = [pdfread.clean_text(text) for text in raw_texts]
    split_texts = pdfread.split_text_by_context(cleaned_texts, context_split_regex)
    logger.info("Cleaned and split text.")

    # Load or initialize the dataset
    start_load_time = time.time()
    df = utils.load_dataset(dataset_path)
    df = utils.filter_empty_entries(df)
    df = utils.validate_entries(df)
    if df.empty:
        df = pd.DataFrame(columns=['text'])
        utils.save_dataset(df, dataset_path)
        logger.info(f"Initialized new dataset at {dataset_path}")
    end_load_time = time.time()
    logger.info(f"Dataset loaded in {end_load_time - start_load_time:.2f} seconds.")

    # Initialize tokenizer
    start_tokenizer_time = time.time()
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token
    end_tokenizer_time = time.time()
    logger.info(f"Tokenizer initialized in {end_tokenizer_time - start_tokenizer_time:.2f} seconds.")

    # Create a PandasDataset instance
    start_dataset_time = time.time()
    dataset = PandasDataset(df, tokenizer)
    end_dataset_time = time.time()
    logger.info(f"Dataset created in {end_dataset_time - start_dataset_time:.2f} seconds.")

    # Step 3: Train the language model (Optional if model is already trained)
    start_train_time = time.time()
    model, tokenizer = modeltrainer.train_model(dataset)
    end_train_time = time.time()
    logger.info(f"Model trained in {end_train_time - start_train_time:.2f} seconds.")

    # Log total execution time
    total_time = time.time() - start_time
    logger.info(f"Initialization completed in {total_time:.2f} seconds.")

    # Start conversation loop
    print("Initializing conversation... Type 'exit' to end.")
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Ending conversation...")
            break

        # Append new information to the dataset
        df = utils.append_to_dataset(df, user_input)
        df = utils.filter_empty_entries(df)
        df = utils.validate_entries(df)
        utils.save_dataset(df, dataset_path)

        # Generate and print response
        response = textgenerator.generate_text(model, tokenizer, user_input)
        print(f"Model: {response}")

if __name__ == "__main__":
    print("Initializing...")
    folder_path = 'C:/Users/Ethan/Documents/sample/'  # Replace with your folder containing PDFs
    dataset_path = 'C:/Users/Ethan/Documents/sample/dataset.csv'  # Path to your dataset
    context_split_regex = r'\n\n'  # Define your context split regex here
    main(folder_path, dataset_path, context_split_regex, enable_logging=True)
