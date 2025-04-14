from transformers import pipeline
classifier = pipeline("zero-shot-classification")
res = classifier(
    "This is an Job Application AI Agent",
    candidate_labels=["education", "politics", "business", "technology", "sports"],
)
print(res)