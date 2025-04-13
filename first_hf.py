from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("Hello, I'm a Hugging Face model!")