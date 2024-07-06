from transformers import pipeline
from functools import lru_cache

# Preload models
models = {
    "text-classification": {
        "bert_base": pipeline("text-classification", model="bert-base-uncased"),
        "bert_large": pipeline("text-classification", model="bert-large-uncased"),
        "roberta": pipeline("text-classification", model="roberta-base"),
        "distilbert": pipeline("text-classification", model="distilbert-base-uncased"),
    },
    "ner": {
        "bert_base": pipeline("ner", model="bert-base-uncased"),
    },
    "question-answering": {
        "bert_base": pipeline("question-answering", model="bert-base-uncased"),
    },
    "summarization": {
        "t5_small": pipeline("summarization", model="t5-small"),
        "t5_base": pipeline("summarization", model="t5-base"),
    }
}

def get_models(task: str):
    return models.get(task, None)

@lru_cache(maxsize=128)
def get_model_output(model, text):
    return model(text)

def evaluate_text(models, text):
    results = {}
    for model_name, model in models.items():
        results[model_name] = get_model_output(model, text)
    return results
