import pandas as pd

def filter_empty_entries(dataframe):
    """
    Filter out empty entries from the DataFrame.
    
    Args:
        dataframe (pd.DataFrame): The DataFrame to filter.
        
    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    if 'text' not in dataframe.columns:
        raise ValueError("The DataFrame must contain a 'text' column.")
    return dataframe[dataframe['text'].str.strip() != '']

def save_dataset(dataframe, path):
    """
    Save the DataFrame to a CSV file.
    
    Args:
        dataframe (pd.DataFrame): The DataFrame to save.
        path (str): The path to save the CSV file.
        
    Raises:
        ValueError: If the path is invalid or the DataFrame is empty.
    """
    if dataframe.empty:
        raise ValueError("The DataFrame is empty and cannot be saved.")
    dataframe.to_csv(path, index=False)

def load_dataset(path):
    """
    Load the DataFrame from a CSV file. If an error occurs, create a new DataFrame.

    Args:
        path (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded DataFrame, or an empty DataFrame if an error occurs.
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"The file at path '{path}' does not exist. Creating a new empty DataFrame.")
        df = pd.DataFrame(columns=['text'])  # Create an empty DataFrame with the expected column name
    except pd.errors.EmptyDataError:
        print(f"The file at path '{path}' is empty. Creating a new empty DataFrame.")
        df = pd.DataFrame(columns=['text'])  # Create an empty DataFrame with the expected column name
    except pd.errors.ParserError:
        print(f"The file at path '{path}' could not be parsed. Creating a new empty DataFrame.")
        df = pd.DataFrame(columns=['text'])  # Create an empty DataFrame with the expected column name

    return df


def append_to_dataset(dataframe, new_text):
    """
    Append a new text entry to the DataFrame.
    
    Args:
        dataframe (pd.DataFrame): The DataFrame to append to.
        new_text (str): The new text entry to add.
        
    Returns:
        pd.DataFrame: The updated DataFrame.
        
    Raises:
        ValueError: If the DataFrame does not have a 'text' column.
    """
    if 'text' not in dataframe.columns:
        raise ValueError("The DataFrame must contain a 'text' column.")
    new_entry = pd.DataFrame({'text': [new_text]})
    return pd.concat([dataframe, new_entry], ignore_index=True)
