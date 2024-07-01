import pandas as pd
from torch.utils.data import Dataset

class PandasDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_length=512):
        self.dataframe = dataframe
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, index):
        text = self.dataframe.iloc[index]['text']

        # Tokenize text and handle padding/truncation
        inputs = self.tokenizer(
            text,
            return_tensors='pt',
            max_length=self.max_length,
            truncation=True,
            padding='max_length'
        )

        input_ids = inputs['input_ids'].squeeze()
        attention_mask = inputs['attention_mask'].squeeze()
        labels = input_ids.clone()  # Labels are the same as input_ids for language modeling

        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'labels': labels
        }