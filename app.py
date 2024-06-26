import os
import pdfread
import modeltrainer
import textgenerator
from dataset import PandasDataset
import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import utils
import nltk

nltk.download('punkt')

def main(folder_path, dataset_path, context_split_regex):
    # Step 1: Extract text from PDFs
    pdf_paths = pdfread.get_pdf_paths(folder_path)
    raw_texts = pdfread.extract_text_from_pdfs(pdf_paths)
    
    # Step 2: Clean the extracted text and split by context
    cleaned_texts = [pdfread.clean_text(text) for text in raw_texts]
    split_texts = pdfread.split_text_by_context(cleaned_texts, context_split_regex)

    # Load or initialize the dataset
    if os.path.exists(dataset_path):
        try:
            df = utils.load_dataset(dataset_path)
            df = utils.filter_empty_entries(df)
            df = utils.validate_entries(df)
        except pd.errors.ParserError:
            print(f"Error parsing {dataset_path}. Initializing new dataset.")
            df = pd.DataFrame(split_texts, columns=['text'])
            df = utils.filter_empty_entries(df)
            df = utils.validate_entries(df)
            utils.save_dataset(df, dataset_path)
    else:
        df = pd.DataFrame(split_texts, columns=['text'])
        df = utils.filter_empty_entries(df)
        df = utils.validate_entries(df)
        utils.save_dataset(df, dataset_path)

    # Initialize tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token

    # Create a PandasDataset instance
    dataset = PandasDataset(df, tokenizer)

    # Step 3: Train the language model (Optional if model is already trained)
    model, tokenizer = modeltrainer.train_model(dataset)

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
    main(folder_path, dataset_path, context_split_regex)
