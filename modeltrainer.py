# modeltrainer.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from torch.utils.data import DataLoader

def train_model(dataset, model_name='gpt2'):
    # Initialize tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token  # Ensure the pad_token is set

    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Create a DataLoader from the dataset
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=1,
        per_device_train_batch_size=4,  # Adjust as per your GPU/CPU capabilities
        save_steps=10_000,
        save_total_limit=2,
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    # Train the model
    trainer.train()

    return model, tokenizer
