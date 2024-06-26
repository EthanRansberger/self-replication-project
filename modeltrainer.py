from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from torch.utils.data import DataLoader

def train_model(dataset, model_name='gpt2', output_dir='./results', num_train_epochs=1, per_device_train_batch_size=4):
    # Initialize tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token  # Ensure the pad_token is set

    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=num_train_epochs,
        per_device_train_batch_size=per_device_train_batch_size,
        save_steps=10_000,
        save_total_limit=2,
        logging_dir=f'{output_dir}/logs',  # Optional: Add logging directory
        logging_steps=100,  # Adjust as needed
        evaluation_strategy="epoch",  # Evaluate at the end of each epoch
        logging_first_step=True,
        load_best_model_at_end=True,  # Load the best model from training
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
    )

    # Train the model
    trainer.train()

    # Save model and tokenizer
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

    return model, tokenizer
