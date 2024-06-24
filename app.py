import pdfreader as pdfreader
import modeltrainer as modeltrainer
import textgenerator as textgenerator

def main(pdf_paths, prompt):
    # Step 1: Extract text from PDFs
    raw_texts = pdfreader.extract_text_from_pdfs(pdf_paths)
    
    # Step 2: Clean the extracted text
    cleaned_texts = [pdfreader.clean_text(text) for text in raw_texts]
    
    # Step 3: Train the language model
    model, tokenizer = modeltrainer.train_model(cleaned_texts)
    
    # Step 4: Generate an essay
    essay = textgenerator.generate_text(model, tokenizer, prompt)
    
    return essay

if __name__ == "__main__":
    print("initializing")
    pdf_paths = ['C:/Users/Ethan/Documents/sample/pdf1.pdf', 'C:/Users/Ethan/Documents/sample/pdf2.pdf']
    prompt = "Write a brief paragraph synthesizing the two pdfs"
    essay = main(pdf_paths, prompt)
    print(essay)