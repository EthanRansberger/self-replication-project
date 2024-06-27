import pandas as pd

def load_dataset(dataset_path):
    """
    Load the dataset from a CSV file.
    
    Args:
        dataset_path (str): The path to the CSV file containing the dataset.
        
    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    return pd.read_csv(dataset_path)

def save_dataset(df, dataset_path):
    """
    Save the dataset to a CSV file.
    
    Args:
        df (pd.DataFrame): The dataset to save.
        dataset_path (str): The path to the CSV file where the dataset will be saved.
    """
    df.to_csv(dataset_path, index=False)

def filter_empty_entries(df):
    """
    Filter out empty entries from the DataFrame.
    
    Args:
        df (pd.DataFrame): The dataset to filter.
        
    Returns:
        pd.DataFrame: The filtered dataset.
    """
    return df.dropna(subset=['text'])

def append_to_dataset(df, text):
    """
    Append a new text entry to the dataset.
    
    Args:
        df (pd.DataFrame): The dataset to append to.
        text (str): The text entry to append.
        
    Returns:
        pd.DataFrame: The updated dataset.
    """
    new_entry = pd.DataFrame([[text]], columns=['text'])
    return pd.concat([df, new_entry], ignore_index=True)
