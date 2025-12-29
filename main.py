from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.config import settings
from app.database import init_db, get_db
from app.models import *
from app.services.openai_service import OpenAIService
from app.services.content_service import ContentService

app = FastAPI(title="AI Content Generation Platform", version="1.0.0")


init_db()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Landing page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Main dashboard"""
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/history", response_class=HTMLResponse)
async def history_page(request: Request):
    """Content history page"""
    return templates.TemplateResponse("history.html", {"request": request})

# API Endpoints
@app.post("/api/generate-ad", response_model=ContentResponse)
async def generate_ad(request: AdRequest, db: Session = Depends(get_db)):
    """Generate ad copy"""
    try:
        result, is_mock = await OpenAIService.generate_ad_copy(
            request.product_name,
            request.description,
            request.target_audience,
            request.tone,
            request.temperature
        )
        
      
        item = ContentService.save_content(
            db,
            content_type="ad",
            prompt=f"{request.product_name} - {request.target_audience}",
            result=result,
            metadata={"tone": request.tone, "description": request.description}
        )
        
        return ContentResponse(
            id=item.id,
            content_type="ad",
            result=result,
            mock=is_mock,
            created_at=item.created_at
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-image", response_model=ContentResponse)
async def generate_image(request: ImageRequest, db: Session = Depends(get_db)):
    """Generate image"""
    try:
        image_url, is_mock = await OpenAIService.generate_image(request.prompt, request.size)
        
       
        item = ContentService.save_content(
            db,
            content_type="image",
            prompt=request.prompt,
            result=image_url,
            metadata={"size": request.size}
        )
        
        return ContentResponse(
            id=item.id,
            content_type="image",
            result=image_url,
            mock=is_mock,
            created_at=item.created_at
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-blog", response_model=ContentResponse)
async def generate_blog(request: BlogRequest, db: Session = Depends(get_db)):
    """Generate blog post"""
    try:
        result, is_mock = await OpenAIService.generate_blog_post(
            request.topic,
            request.keywords,
            request.tone,
            request.length,
            request.temperature
        )
        
     
        item = ContentService.save_content(
            db,
            content_type="blog",
            prompt=request.topic,
            result=result,
            metadata={"keywords": request.keywords, "tone": request.tone, "length": request.length}
        )
        
        return ContentResponse(
            id=item.id,
            content_type="blog",
            result=result,
            mock=is_mock,
            created_at=item.created_at
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-social", response_model=ContentResponse)
async def generate_social(request: SocialMediaRequest, db: Session = Depends(get_db)):
    """Generate social media post"""
    try:
        result, is_mock = await OpenAIService.generate_social_post(
            request.platform,
            request.topic,
            request.tone,
            request.include_hashtags,
            request.temperature
        )
        
      
        item = ContentService.save_content(
            db,
            content_type="social",
            prompt=f"{request.platform}: {request.topic}",
            result=result,
            metadata={"platform": request.platform, "tone": request.tone}
        )
        
        return ContentResponse(
            id=item.id,
            content_type="social",
            result=result,
            mock=is_mock,
            created_at=item.created_at
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/history")
async def get_history(content_type: str = None, db: Session = Depends(get_db)):
    """Get content history"""
    items = ContentService.get_history(db, content_type)
    return [
        {
            "id": item.id,
            "content_type": item.content_type,
            "prompt": item.prompt,
            "result": item.result,
            "created_at": item.created_at.isoformat()
        }
        for item in items
    ]

@app.delete("/api/history/{item_id}")
async def delete_history_item(item_id: int, db: Session = Depends(get_db)):
    """Delete history item"""
    success = ContentService.delete_item(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"success": True}
