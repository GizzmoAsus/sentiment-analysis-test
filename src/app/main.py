from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os

# Initialise NLTK
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

class SentimentRequest(BaseModel):
  text: str = Field(..., description="The text to analyse")

app = FastAPI()

@app.get('/')
async def index():
  return "Service is running!"

# API for sentiment analysis
@app.post('/')
async def analyze_sentiment(request: SentimentRequest):
  try:
    text = request.text.strip()

    # Perform sentiment analysis
    score = sia.polarity_scores(text)
    sentiment = 'positive' if score['compound'] > 0 else 'negative' if score['compound'] < 0 else 'neutral'

    return {'text': text, 'sentiment': sentiment, 'sentiment_score': score}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
