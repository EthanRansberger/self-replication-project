def main(pdf_paths, prompt):
    # Step 1: Extract text from PDFs
    raw_texts = extract_text_from_pdfs(pdf_paths)
    
    # Step 2: Clean the extracted text
    cleaned_texts = [clean_text(text) for text in raw_texts]
    
    # Step 3: Train the language model
    model, tokenizer = train_model(cleaned_texts)
    
    # Step 4: Generate an essay
    essay = generate_text(model, tokenizer, prompt)
    
    return essay

if __name__ == "__main__":
    pdf_paths = ['path/to/pdf1.pdf', 'path/to/pdf2.pdf']
    prompt = "Write an essay on the impact of technology on society."
    essay = main(pdf_paths, prompt)
    print(essay)