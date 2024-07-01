import os
import pandas as pd
from dataset import PandasDataset  # Import the PandasDataset class
import errorhandling
import csvreader
import sqlitereader
import modeltrainer
import textgenerator
import utils

# Main function
@errorhandling.handle_errors
def main(dataset_path, csv_folder_path, context_split_regex, sqlite_folder_path):
    print("Initializing...")

    # Read CSV files from folder
    csv_texts = csvreader.read_csv_files(csv_folder_path)

    # Read SQLite files
    sqlite_texts = sqlitereader.read_sqlite_files(sqlite_folder_path)

    # Combine the texts from CSV and SQLite
    combined_texts = csv_texts + sqlite_texts

    # Check if we have any texts
    if not combined_texts:
        raise ValueError("No texts found in CSV or SQLite files.")

    # Create a DataFrame for the combined texts
    dataframe = pd.DataFrame(combined_texts, columns=['text'])

    # Filter out empty entries
    dataframe = utils.filter_empty_entries(dataframe)

    # Save the dataset to a CSV file
    utils.save_dataset(dataframe, dataset_path)

    # Load the dataset (in case it needs to be reloaded after modifications)
    dataframe = utils.load_dataset(dataset_path)

    # Initialize the tokenizer
    tokenizer = modeltrainer.load_tokenizer('gpt2')

    # Create a dataset and dataloader for training
    train_dataset = PandasDataset(dataframe, tokenizer, max_length=512)

    # Check if the dataset is empty
    if len(train_dataset) == 0:
        raise ValueError("The dataset is empty. Please check your data loading process.")

    train_dataloader = modeltrainer.create_dataloader(train_dataset, batch_size=4)

    # Set up the model
    model_name = 'gpt2'
    model = modeltrainer.load_model(model_name)

    # Train the model
    modeltrainer.train_model(
        model=model,
        tokenizer=tokenizer,
        dataloader=train_dataloader,
        num_train_epochs=1,
        per_device_train_batch_size=4
    )

    print("Model trained successfully!")

    # Interactive chat with the model
    print("\nYou can now talk to the model. Type 'exit' to end the conversation.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break

        # Generate a response from the model
        generated_text = textgenerator.generate_text(model, tokenizer, user_input)
        print(f"Model: {generated_text}")

        # Append the user's input and model's response to the dataset
        new_entry = f"You: {user_input}\nModel: {generated_text}"
        dataframe = utils.append_to_dataset(dataframe, new_entry)
        utils.save_dataset(dataframe, dataset_path)  # Save the updated dataset

    print("Conversation ended.")

# Call the main function with the appropriate arguments
if __name__ == "__main__":
    import argparse

    # Argument parsing
    parser = argparse.ArgumentParser(description="Run the text generation and training process.")
    parser.add_argument('--dataset_path', type=str, default='C:/Users/Ethan/Documents/sample/dataset.csv',
                        help='Path to save or load the dataset CSV file.')
    parser.add_argument('--csv_folder_path', type=str, default='C:/Users/Ethan/Documents/sample/csv/',
                        help='Path to the folder containing additional CSV files.')
    parser.add_argument('--context_split_regex', type=str, default=r'\n\n',
                        help='Regex pattern to split text contexts.')
    parser.add_argument('--sqlite_folder_path', type=str, default='C:/Users/Ethan/Documents/sample/sqlite/',
                        help='Path to the folder containing SQLite files.')

    args = parser.parse_args()

    main(
        dataset_path=args.dataset_path,
        csv_folder_path=args.csv_folder_path,
        context_split_regex=args.context_split_regex,
        sqlite_folder_path=args.sqlite_folder_path
    )
