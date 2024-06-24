import pdfread as pdfread
import modeltrainer as modeltrainer
import textgenerator as textgenerator





def main(pdf_paths, prompt):
    
    # Step 1: Extract text from PDFs
    raw_texts = pdfread.extract_text_from_pdfs(pdf_paths)
    context_split_regex = r'\n\n'
    split_texts = pdfread.split_text_by_context(raw_texts, context_split_regex)
    # Step 2: Clean the extracted text
    cleaned_texts = [pdfread.clean_text(text) for text in split_texts]
    print(cleaned_texts)

    
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