# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# tokenizer = AutoTokenizer.from_pretrained("DGurgurov/xlm-r_romanian_sentiment")
# model = AutoModelForSequenceClassification.from_pretrained("DGurgurov/xlm-r_romanian_sentiment")

from transformers import pipeline

sentiment_pipe = pipeline("sentiment-analysis", model="DGurgurov/xlm-r_romanian_sentiment")

result = sentiment_pipe("Autorităţile britanice au interzis scriitorului francez Renaud Camus să intre în Marea Britanie")
print(result)
# Output example: [{'label': 'NEGATIVE', 'score': 0.98}]
