from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I will not lose", "it was the worst of times"]
print(sentiment_pipeline(data))
