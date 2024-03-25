import logging
from transformers import pipeline

logging.basicConfig(level=logging.WARNING)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class Model:
    def __init__(self) -> None:
        print("New model initiated")
        self.model = classifier

    def classify(self, prompt, options):
        result = self.model(prompt, options)
        return result['labels'][0]