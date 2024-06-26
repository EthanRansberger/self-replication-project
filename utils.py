import pandas as pd

def load_dataset(path):
    try:
        return pd.read_csv(path)
    except pd.errors.ParserError:
        print(f"Error parsing {path}. Initializing new dataset.")
        return pd.DataFrame()

def save_dataset(df, path):
    df.to_csv(path, index=False)

def filter_empty_entries(df):
    return df.dropna(subset=['text'])

def append_to_dataset(df, text):
    new_data = {'text': [text]}
    return pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
