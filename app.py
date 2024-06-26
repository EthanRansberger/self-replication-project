import os
import pdfread  # Assuming pdfread is your custom module for PDF handling
import modeltrainer  # Assuming modeltrainer contains train_model function
import textgenerator  # Assuming textgenerator contains generate_text function
from dataset import PandasDataset  # Import the PandasDataset class from your dataset module
import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def get_pdf_paths(folder_path):
    """Returns a list of all PDF file paths in the given folder."""
    pdf_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pdf')]
    return pdf_paths

def main(folder_path):
    # Step 1: Extract text from PDFs
    pdf_paths = get_pdf_paths(folder_path)
    raw_texts = pdfread.extract_text_from_pdfs(pdf_paths)
    
    # Step 2: Clean the extracted text
    cleaned_texts = [pdfread.clean_text(text) for text in raw_texts]
    print(cleaned_texts)

    # Convert the cleaned texts to a pandas DataFrame
    df = pd.DataFrame(cleaned_texts, columns=['text'])

    # Initialize tokenizer and set pad_token
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token  # Set pad_token to eos_token

    # Create a PandasDataset instance
    dataset = PandasDataset(df, tokenizer)

    # Step 3: Train the language model (Optional if model is already trained)
    model, tokenizer = modeltrainer.train_model(dataset)

    # Start conversation loop
    print("Initializing conversation... Type 'exit' to end.")
    while True:
        # Take user input
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Ending conversation...")
            break

        # Tokenize the input and generate model input
        input_ids = tokenizer.encode(user_input, return_tensors='pt')

        # Generate response from the model
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

        # Decode and print the response
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        print(f"Model: {response}")

if __name__ == "__main__":
    print("Initializing...")
    folder_path = 'C:/Users/Ethan/Documents/sample/'  # Replace with your folder containing PDFs
    main(folder_path)
