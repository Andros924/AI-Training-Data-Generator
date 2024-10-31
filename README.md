Project Description
The AI Training Dataset Generator is a Python-based web application designed to help users create AI training datasets from textual data, which can be entered directly or uploaded in PDF format. The application processes this data, structures it into a labeled JSON format, and offers it as a downloadable file for further training purposes.

This tool streamlines the process of dataset creation by automating text extraction and formatting, which makes it ideal for users looking to build and refine natural language processing (NLP) datasets without manual text processing.

Key Features
PDF & Text Input:

Users can upload PDF files or enter plain text directly through the web interface. PDF files are parsed to extract text content, which is then segmented for dataset generation.
Automated Dataset Generation:

The application splits text into manageable data entries (such as sentences) and organizes them in a JSON format, with each entry given a unique identifier.
The generated dataset is structured to facilitate training AI and NLP models, providing a ready-to-use JSON output.
Web Interface:

A simple yet effective web UI built with Flask and HTML/JavaScript.
Users can upload files, view the generated JSON output in real-time, and download the final JSON file.
JSON Export:

The final output, a structured JSON dataset, is downloadable for easy integration into ML model training pipelines.
Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript (for interactive UI)
PDF Processing: PyMuPDF (or pdfminer.six)
Data Formatting: JSON
