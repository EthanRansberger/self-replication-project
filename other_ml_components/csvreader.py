import os
import pandas as pd

def read_csv_files(folder_path):
    """
    Read all CSV files in the specified folder and extract text from columns with potential names.
    
    Args:
        folder_path (str): The path to the folder containing CSV files.
        
    Returns:
        List[str]: A list of text entries extracted from the CSV files.
    """
    csv_texts = []
    potential_column_names = ['text', 'name', 'title']

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            if not os.path.exists(file_path):
                print(f"The file {file_path} does not exist.")
                continue

            try:
                df = pd.read_csv(file_path)

                # Check for potential text columns
                text_column = None
                for col in potential_column_names:
                    if col in df.columns:
                        text_column = col
                        break

                if text_column is None:
                    print(f"No suitable text column found in file {file_path}.")
                    continue

                # Extract text from the chosen column
                texts = df[text_column].dropna().tolist()
                csv_texts.extend(texts)

            except pd.errors.EmptyDataError:
                print(f"The file {file_path} is empty.")
            except pd.errors.ParserError:
                print(f"The file {file_path} could not be parsed.")
            except Exception as e:
                print(f"An error occurred while processing file {file_path}: {e}")

    return csv_texts
