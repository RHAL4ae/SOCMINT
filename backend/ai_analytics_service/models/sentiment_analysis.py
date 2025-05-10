# Sentiment analysis using AraBERT/mBERT
from typing import Dict
import os
import re
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# Load models once at module level for efficiency
model_name = os.getenv("SENTIMENT_MODEL", "asafaya/bert-base-arabic-sentiment")

# Initialize models lazily
_sentiment_analyzer = None

def get_sentiment_analyzer():
    global _sentiment_analyzer
    if _sentiment_analyzer is None:
        try:
            _sentiment_analyzer = pipeline(
                "sentiment-analysis",
                model=model_name,
                tokenizer=model_name
            )
        except Exception as e:
            print(f"Error loading sentiment model: {e}")
            # Fallback to a simpler model if the main one fails
            _sentiment_analyzer = pipeline("sentiment-analysis")
    return _sentiment_analyzer

def detect_language(text):
    """Simple language detection to determine if text is primarily Arabic or not"""
    # Arabic Unicode range
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')
    arabic_chars = len(arabic_pattern.findall(text))
    return "arabic" if arabic_chars > len(text) * 0.3 else "other"

def analyze_sentiment(text: str) -> Dict:
    """Analyze sentiment of text, supporting both Arabic and other languages
    
    Args:
        text: The text to analyze
        
    Returns:
        Dict with sentiment label and confidence score
    """
    if not text or len(text.strip()) == 0:
        return {"label": "neutral", "confidence": 1.0}
    
    try:
        analyzer = get_sentiment_analyzer()
        result = analyzer(text)[0]
        
        # Normalize the output format
        label = result.get('label', '').lower()
        if 'positive' in label:
            normalized_label = 'positive'
        elif 'negative' in label:
            normalized_label = 'negative'
        else:
            normalized_label = 'neutral'
            
        return {
            "label": normalized_label,
            "confidence": result.get('score', 0.5)
        }
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        # Fallback to neutral sentiment
        return {"label": "neutral", "confidence": 0.5}