from flask import Flask
import torch

def create_app():
    app = Flask(__name__)
    app.config['USE_GPU'] = torch.cuda.is_available()  # Use GPU if available
    return app

app = create_app()
