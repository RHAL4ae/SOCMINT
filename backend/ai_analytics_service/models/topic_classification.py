# Topic classification using multilingual models
from typing import Dict, List, Optional
import os
import re
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Initialize models lazily
_topic_classifier = None

# Define topic categories
TOPIC_CATEGORIES = [
    "cybercrime", "terrorism", "financial_crime", "politics", 
    "social_unrest", "drugs", "human_trafficking", "other"
]

# Simple keyword-based classification for fallback
TOPIC_KEYWORDS = {
    "cybercrime": ["hack", "cyber", "malware", "ransomware", "phishing", "اختراق", "قرصنة", "برمجيات خبيثة"],
    "terrorism": ["terror", "bomb", "attack", "extremist", "إرهاب", "متطرف", "هجوم", "تفجير"],
    "financial_crime": ["money", "laundering", "fraud", "corruption", "bribe", "غسيل أموال", "فساد", "رشوة", "احتيال"],
    "politics": ["government", "election", "political", "minister", "حكومة", "انتخابات", "سياسة", "وزير"],
    "social_unrest": ["protest", "riot", "unrest", "demonstration", "احتجاج", "مظاهرة", "اضطرابات"],
    "drugs": ["drug", "narcotic", "cocaine", "heroin", "مخدرات", "حشيش", "كوكايين", "هيروين"],
    "human_trafficking": ["trafficking", "smuggling", "migrant", "slave", "اتجار بالبشر", "تهريب", "مهاجرين", "عبودية"]
}

def detect_language(text):
    """Simple language detection to determine if text is primarily Arabic or not"""
    # Arabic Unicode range
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')
    arabic_chars = len(arabic_pattern.findall(text))
    return "arabic" if arabic_chars > len(text) * 0.3 else "other"

def get_topic_classifier():
    """Get or initialize the topic classifier"""
    global _topic_classifier
    if _topic_classifier is None:
        try:
            # For a production system, you would load a fine-tuned model here
            # This is a simplified implementation using zero-shot classification
            _topic_classifier = pipeline(
                "zero-shot-classification",
                model=os.getenv("TOPIC_MODEL", "facebook/bart-large-mnli")
            )
        except Exception as e:
            print(f"Error loading topic classification model: {e}")
            # Fallback to keyword-based classification
            _topic_classifier = None
    return _topic_classifier

def keyword_based_classification(text: str) -> str:
    """Fallback method using keyword matching for topic classification"""
    text = text.lower()
    scores = {}
    
    for topic, keywords in TOPIC_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword.lower() in text)
        scores[topic] = score
    
    # Get the topic with the highest score
    max_score = max(scores.values()) if scores else 0
    if max_score > 0:
        # Get all topics with the max score
        top_topics = [topic for topic, score in scores.items() if score == max_score]
        return top_topics[0]  # Return the first one if there are ties
    
    return "other"

def classify_topic(text: str) -> str:
    """Classify the topic of the text
    
    Args:
        text: The text to classify
        
    Returns:
        The predicted topic category
    """
    if not text or len(text.strip()) == 0:
        return "other"
    
    try:
        classifier = get_topic_classifier()
        if classifier:
            # Use zero-shot classification with our predefined categories
            result = classifier(text, TOPIC_CATEGORIES)
            return result['labels'][0]  # Return the highest confidence label
        else:
            # Fallback to keyword-based classification
            return keyword_based_classification(text)
    except Exception as e:
        print(f"Error in topic classification: {e}")
        # Fallback to keyword-based classification
        return keyword_based_classification(text)