from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AdRequest(BaseModel):
    product_name: str
    description: str = ""
    target_audience: str
    tone: str
    temperature: Optional[float] = 0.7

class ImageRequest(BaseModel):
    prompt: str
    size: Optional[str] = "1024x1024"

class BlogRequest(BaseModel):
    topic: str
    keywords: str = ""
    tone: str = "Professional"
    length: str = "medium"  
    temperature: Optional[float] = 0.7

class SocialMediaRequest(BaseModel):
    platform: str  
    topic: str
    tone: str = "Casual"
    include_hashtags: bool = True
    temperature: Optional[float] = 0.8

class ContentResponse(BaseModel):
    id: Optional[int] = None
    content_type: str
    result: str
    mock: bool = False
    created_at: Optional[datetime] = None

class HistoryItem(BaseModel):
    id: int
    content_type: str
    prompt: str
    result: str
    created_at: datetime
    
    class Config:
        from_attributes = True
