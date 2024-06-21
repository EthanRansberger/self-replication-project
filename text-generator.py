from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

def generate_text(model, tokenizer, prompt, max_length=500):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text
