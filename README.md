# Sentiment Analysis Service

## Overview
This service provides sentiment analysis of text data via a REST API. It's built using Flask and NLTK, with data stored in a MySQL database.

__NB: This repo was forked from https://github.com/Azure-Samples/containerapps-albumapi-python__ see here for more info on deploying into Azure App Service.

## Features
- Sentiment analysis of text data.
- Storing sentiment scores in a MySQL database.
- Retrieving sentiment data based on user UUID.
- Auto documenting of the API's using swagger _(/docs)_ or Redoc _(/redoc)_

### Understanding Sentiment Scores
The sentiment analysis returns several scores that represent different aspects of sentiment:

- **Positive Score (`pos`)**: Proportion of the text that falls into the positive category. Higher scores indicate more positive sentiments.
- **Neutral Score (`neu`)**: Proportion of the text that is neutral. High scores are often found in factual or objective statements.
- **Negative Score (`neg`)**: Proportion of the text that is negative. Higher scores indicate more negative sentiments.
- **Compound Score (`compound`)**: A normalized, weighted composite score of the positive, neutral, and negative scores. Ranges from -1 (extremely negative) to +1 (extremely positive). It provides an overall sentiment of the text.

## Usage

### Analyse Sentiments

- **Endpoint**: `POST /`
- **Payload**:
```json
{
 "text": "string"
}
```

You can call this via CURL or via postman or whatever service you like e.g.

```bash
$ curl -X POST {URL} \
-H "Content-Type: application/json" \
-d '{"text": "I love this new service! It works wonderfully."}'

{
  "sentiment": "positive",
  "sentiment_score": {
    "compound": 0.8553,
    "neg": 0.0,
    "neu": 0.373,
    "pos": 0.627
  },
  "text": "I love this new service! It works wonderfully."
}
```
