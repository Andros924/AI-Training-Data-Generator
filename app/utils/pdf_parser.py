import fitz  # PyMuPDF
from tqdm import tqdm

def parse_pdf(file, use_gpu=False):
    pdf_text = ""
    progress_updates = []
    
    # Load PDF and set up progress bar
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        page_count = len(doc)
        
        # Processing with progress tracking
        for page_num in tqdm(range(page_count), desc="Extracting Text", unit="page"):
            pdf_text += doc[page_num].get_text()
            progress_updates.append(page_num + 1)

    # Split text into sentences
    sentences = pdf_text.split('. ')
    return sentences, progress_updates