# Named Entity Recognition using AraBERT/mBERT
from typing import List, Dict
import os
import re
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

# Load models once at module level for efficiency
model_name = os.getenv("NER_MODEL", "aubmindlab/bert-base-arabertv02-ner")

# Initialize models lazily
_ner_pipeline = None

def get_ner_pipeline():
    global _ner_pipeline
    if _ner_pipeline is None:
        try:
            _ner_pipeline = pipeline(
                "ner",
                model=model_name,
                tokenizer=model_name,
                aggregation_strategy="simple"
            )
        except Exception as e:
            print(f"Error loading NER model: {e}")
            # Fallback to a simpler model if the main one fails
            _ner_pipeline = pipeline("ner", aggregation_strategy="simple")
    return _ner_pipeline

def detect_language(text):
    """Simple language detection to determine if text is primarily Arabic or not"""
    # Arabic Unicode range
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')
    arabic_chars = len(arabic_pattern.findall(text))
    return "arabic" if arabic_chars > len(text) * 0.3 else "other"

def normalize_entity_type(entity_type):
    """Normalize entity types to standard format (PERSON, LOCATION, ORGANIZATION)"""
    entity_type = entity_type.upper()
    
    if any(person_type in entity_type for person_type in ["PER", "PERSON", "NAME"]):
        return "PERSON"
    elif any(loc_type in entity_type for loc_type in ["LOC", "LOCATION", "GPE"]):
        return "LOCATION"
    elif any(org_type in entity_type for org_type in ["ORG", "ORGANIZATION"]):
        return "ORGANIZATION"
    else:
        return entity_type

def extract_entities(text: str) -> List[Dict]:
    """Extract named entities from text, supporting both Arabic and other languages
    
    Args:
        text: The text to analyze
        
    Returns:
        List of dictionaries with entity type and value
    """
    if not text or len(text.strip()) == 0:
        return []
    
    try:
        ner_pipeline = get_ner_pipeline()
        entities = ner_pipeline(text)
        
        # Process and normalize entities
        normalized_entities = []
        for entity in entities:
            entity_type = normalize_entity_type(entity.get('entity_group', entity.get('entity', '')))
            
            # Only include the entity types we're interested in
            if entity_type in ["PERSON", "LOCATION", "ORGANIZATION"]:
                normalized_entities.append({
                    "type": entity_type,
                    "value": entity.get('word', entity.get('string', ''))
                })
        
        # Remove duplicates while preserving order
        unique_entities = []
        seen = set()
        for entity in normalized_entities:
            key = (entity["type"], entity["value"])
            if key not in seen:
                seen.add(key)
                unique_entities.append(entity)
                
        return unique_entities
    except Exception as e:
        print(f"Error in entity extraction: {e}")
        return []