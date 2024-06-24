from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

def train_model(texts, model_name='gpt2'):
    # Initialize tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token  # Set pad_token to eos_token or another suitable token
    
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Tokenize and prepare dataset
    inputs = tokenizer(texts, return_tensors='pt', max_length=512, truncation=True, padding=True)
    print(inputs)  # Add this line to check the contents of inputs just before trainer.train()
    print(len(inputs))
    # Ensure all necessary keys are present in inputs
    if 'input_ids' not in inputs:
        raise ValueError("Missing 'input_ids' in tokenizer outputs.")

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=1,
        per_device_train_batch_size=4,  # Adjust as per your GPU/CPU capabilities
        save_steps=10_000,
        save_total_limit=2,
    )

    # Ensure all required keys are present in the inputs
    train_dataset = {}
    for key in ['input_ids', 'attention_mask', 'token_type_ids']:
        if key in inputs:
            train_dataset[key] = inputs[key]

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )

    # Train the model
    trainer.train()

    return model, tokenizer
