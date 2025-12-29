import json
from sqlalchemy.orm import Session
from app.database import ContentItem
from typing import List, Optional

class ContentService:
    """Service for content management"""
    
    @staticmethod
    def save_content(db: Session, content_type: str, prompt: str, result: str, metadata: dict = None) -> ContentItem:
        """Save generated content to database"""
        item = ContentItem(
            content_type=content_type,
            prompt=prompt,
            result=result,
            content_metadata=json.dumps(metadata or {})
        )
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    
    @staticmethod
    def get_history(db: Session, content_type: Optional[str] = None, limit: int = 50) -> List[ContentItem]:
        """Get content history"""
        query = db.query(ContentItem)
        if content_type:
            query = query.filter(ContentItem.content_type == content_type)
        return query.order_by(ContentItem.created_at.desc()).limit(limit).all()
    
    @staticmethod
    def get_item(db: Session, item_id: int) -> Optional[ContentItem]:
        """Get specific content item"""
        return db.query(ContentItem).filter(ContentItem.id == item_id).first()
    
    @staticmethod
    def delete_item(db: Session, item_id: int) -> bool:
        """Delete content item"""
        item = db.query(ContentItem).filter(ContentItem.id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
            return True
        return False
