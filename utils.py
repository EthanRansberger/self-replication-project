import pandas as pd

def load_dataset(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found. Initializing new dataset.")
        return pd.DataFrame()

def save_dataset(df, path):
    df.to_csv(path, index=False)

def filter_empty_entries(df):
    return df.dropna(subset=['text'])

def validate_entries(df):
    # You can add additional validation logic here if needed
    return df

def append_to_dataset(df, new_data):
    new_row = {'text': new_data}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df
