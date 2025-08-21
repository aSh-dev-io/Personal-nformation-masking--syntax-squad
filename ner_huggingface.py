from transformers import pipeline

ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

def detect_names(text):
    results = ner_pipeline(text)
    names = [res["word"] for res in results if res["entity_group"] == "PER"]
    return names
