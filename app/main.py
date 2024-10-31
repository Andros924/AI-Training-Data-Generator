from flask import request, jsonify, render_template
from app import app
from app.utils.pdf_parser import parse_pdf
from app.utils.dataset_generator import generate_dataset
from tqdm import tqdm
import time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    start_time = time.time()
    
    # Get the file or text from the request
    file = request.files.get('file')
    text = request.form.get('text')

    # Use PDF if provided, else process text directly
    if file:
        sentences, progress_updates = parse_pdf(file, app.config['USE_GPU'])
    elif text:
        sentences = text.split('. ')  # Simple split for text input, without progress
        progress_updates = None
    else:
        return jsonify({"error": "No valid input provided"}), 400

    # Generate dataset and track progress
    dataset = generate_dataset(sentences, progress_updates)
    
    processing_time = round(time.time() - start_time, 2)
    return jsonify({"dataset": dataset, "processing_time": processing_time})
