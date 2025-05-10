"""
جامع بيانات Google Business Profiles
يدعم جمع التعليقات والتقييمات والمنشورات مع مراعاة حدود الكوتا (Rate Limits).
"""
import json
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import logging

logger = logging.getLogger(__name__)

# مخرجات موحدة

def normalize_google_business_output(content, author, timestamp, media, metadata):
    return {
        "platform": "google_business",
        "content": content,
        "author": author,
        "timestamp": timestamp,
        "media": media,
        "metadata": metadata
    }

# دالة تجميع رئيسية (واجهة)
def collect_google_business_data(credentials, location_id, limit=50):
    """
    جمع تعليقات وتقييمات ومنشورات من Google Business Profile
    
    Args:
        credentials (dict): بيانات اعتماد OAuth2
        location_id (str): معرف الموقع
        limit (int): عدد العناصر المطلوب جمعها
    
    Returns:
        list: قائمة بالعناصر المجمعة
    """
    results = []
    
    try:
        # إنشاء اعتماد OAuth2
        creds = service_account.Credentials.from_service_account_info(credentials)
        
        # بناء خدمة Google My Business
        service = build('mybusinessbusinessinformation', 'v1', credentials=creds)
        
        # جمع التعليقات
        reviews = service.locations().reviews().list(
            parent=f'locations/{location_id}'
        ).execute()
        
        for review in reviews.get('reviews', [])[:limit]:
            try:
                normalized = normalize_google_business_output(
                    content=review.get('comment', ''),
                    author=review.get('reviewer', {}).get('displayName', 'unknown'),
                    timestamp=review.get('createTime', datetime.utcnow().isoformat()+"Z"),
                    media=None,
                    metadata={
                        "rating": review.get('starRating'),
                        "review_id": review.get('name'),
                        "location_id": location_id
                    }
                )
                results.append(normalized)
            except Exception as e:
                logger.error(f"خطأ في معالجة تعليق: {str(e)}")
        
        # جمع التقييمات
        ratings = service.locations().get(
            name=f'locations/{location_id}'
        ).execute()
        
        rating_data = {
            "average_rating": ratings.get('aggregateRating', {}).get('ratingValue'),
            "total_reviews": ratings.get('aggregateRating', {}).get('reviewCount')
        }
        
        normalized_rating = normalize_google_business_output(
            content=f"متوسط التقييم: {rating_data['average_rating']} من 5\nعدد التعليقات: {rating_data['total_reviews']}",
            author="Google Business",
            timestamp=datetime.utcnow().isoformat()+"Z",
            media=None,
            metadata={
                "type": "rating_summary",
                "location_id": location_id
            }
        )
        results.append(normalized_rating)
        
        # جمع المنشورات
        posts = service.locations().posts().list(
            parent=f'locations/{location_id}'
        ).execute()
        
        for post in posts.get('posts', [])[:limit]:
            try:
                normalized = normalize_google_business_output(
                    content=post.get('text', ''),
                    author="النشاط التجاري",
                    timestamp=post.get('createTime', datetime.utcnow().isoformat()+"Z"),
                    media=post.get('media', [{}])[0].get('url') if post.get('media') else None,
                    metadata={
                        "post_id": post.get('name'),
                        "location_id": location_id,
                        "type": "post"
                    }
                )
                results.append(normalized)
            except Exception as e:
                logger.error(f"خطأ في معالجة منشور: {str(e)}")
                
    except Exception as e:
        logger.error(f"خطأ في جمع بيانات Google Business: {str(e)}")
        return []
    finally:
        return results

# إرسال النتائج إلى كافكا (raw_social_data)
def send_to_kafka(data):
    """
    إرسال البيانات إلى Kafka
    
    Args:
        data (list): قائمة بالبيانات المجمعة
    """
    try:
        from kafka import KafkaProducer
        import json
        
        producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        
        for item in data:
            try:
                producer.send('raw_social_data', value=item)
                logger.info(f"تم إرسال بيانات إلى Kafka: {item['location_id']}")
            except Exception as e:
                logger.error(f"خطأ في إرسال إلى Kafka: {str(e)}")
        
        producer.flush()
    except Exception as e:
        logger.error(f"خطأ في إعداد Kafka: {str(e)}")