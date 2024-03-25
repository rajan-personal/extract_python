class AI:
    def __init__(self) -> None:
        pass

    def prompt(self, p):
        pass


# import logging
# from transformers import pipeline

# # Set the logging level to WARNING to suppress less severe messages
# logging.basicConfig(level=logging.WARNING)

# # Initialize the zero-shot classification pipeline
# classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# # Example usage
# sequence_to_classify = "one day I will see the world"
# candidate_labels = ['travel', 'cooking', 'dancing']
# result = classifier(sequence_to_classify, candidate_labels)
# print(result)