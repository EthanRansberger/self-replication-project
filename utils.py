import pandas as pd

def append_to_dataset(df, new_data):
    new_row = {'text': new_data}
    df = df.append(new_row, ignore_index=True)
    return df

def save_dataset(df, path):
    df.to_csv(path, index=False)

def load_dataset(path):
    return pd.read_csv(path, error_bad_lines=False, warn_bad_lines=True)

def filter_empty_entries(df):
    df = df[df['text'].str.strip().astype(bool)]
    return df

def validate_entries(df):
    df = df[df['text'].apply(lambda x: isinstance(x, str))]
    return df
