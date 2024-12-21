# Multimodal Evaluation and Comparison System

## Project Overview
This project provides a backend system to evaluate and compare multiple language models on various natural language processing tasks. The system is implemented using FastAPI and integrates several pre-trained models from the Hugging Face Transformers library.

## Features
- Evaluate text classification, named entity recognition (NER), question answering, and text summarization tasks using multiple models.
- Caching mechanism to store model outputs and improve response times.
- Benchmarking feature to run models on provided datasets and return performance metrics.
- Health check endpoint to monitor the service status.
- Rate limiting to prevent abuse of the API.
- Optional authentication and user-uploaded model support.

## Setup Instructions

### Prerequisites
- Python 3.7+
- Git
- Redis (for caching and rate limiting)

### Installation
1. Clone the repository:
    ```bash
    git clone git@github.com:saurabh4269/multimodal-evaluation-and-comparison-system_backend.git
    cd multimodal-evaluation-and-comparison-system_backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

### Usage
- Access the API at `http://127.0.0.1:8000`.
- Use the `/evaluate` endpoint to evaluate text using different models.
- Use the `/benchmark` endpoint to run benchmarks on provided datasets.
- Use the `/health` endpoint to check the status of the service.

### Example API Requests

#### Evaluate Text
```bash
curl -X POST "http://127.0.0.1:8000/evaluate" -H "Content-Type: application/json" -d '{
    "text": "What is the capital of France?",
    "task": "question-answering"
}'
```
### Health Check
```bash
curl -X GET "http://127.0.0.1:8000/health"
```
