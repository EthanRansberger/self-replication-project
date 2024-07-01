from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text(model, tokenizer, prompt, max_length=500):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    if inputs.shape[-1] == 0:
        return "I didn't catch that. Could you please repeat?"

    outputs = model.generate(
        inputs,
        attention_mask=inputs.new_ones(inputs.shape),
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text
