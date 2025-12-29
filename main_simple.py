from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from datetime import datetime

import ollama

from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

app = FastAPI(title="AI Content Generation Platform")


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


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


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/history", response_class=HTMLResponse)
async def history_page(request: Request):
    return templates.TemplateResponse("history.html", {"request": request})


@app.post("/api/generate-ad")
async def generate_ad(req: AdRequest):
    try:
        if not client:
            # Try using Ollama locally if OpenAI key is missing
            try:
                response = ollama.chat(model='llama3.2', messages=[
                    {"role": "system", "content": f"You are a professional copywriter. Tone: {req.tone}"},
                    {"role": "user", "content": f"Write a compelling ad for '{req.product_name}'. Target: {req.target_audience}. Description: {req.description}"}
                ])
                return {"result": response['message']['content'], "mock": False, "id": 1, "content_type": "ad", "created_at": datetime.now().isoformat()}
            except Exception as e:
                print(f"Ollama Error: {e}")
            
            return {
                "result": f"**{req.product_name} - Experience the Future!**\n\nAre you a {req.target_audience} looking for innovation?\n{req.description}\n\n**Try {req.product_name} today!**",
                "mock": True,
                "id": 1,
                "content_type": "ad",
                "created_at": datetime.now().isoformat()
            }
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a professional copywriter. Tone: {req.tone}"},
                {"role": "user", "content": f"Write a compelling ad for '{req.product_name}'. Target: {req.target_audience}. Description: {req.description}"}
            ],
            temperature=req.temperature
        )
        return {
            "result": response.choices[0].message.content, 
            "mock": False,
            "id": 1,
            "content_type": "ad",
            "created_at": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-image")
async def generate_image(req: ImageRequest):
    try:
        if not client:
            return {
                "result": "https://picsum.photos/1024/1024", 
                "mock": True,
                "id": 1,
                "content_type": "image",
                "created_at": datetime.now().isoformat()
            }
        
        response = client.images.generate(
            prompt=req.prompt,
            n=1,
            size=req.size
        )
        return {
            "result": response.data[0].url, 
            "mock": False,
            "id": 1,
            "content_type": "image",
            "created_at": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-blog")
async def generate_blog(req: BlogRequest):
    try:
        word_counts = {"short": 300, "medium": 600, "long": 1000}
        target_words = word_counts.get(req.length, 600)
        
        if not client:
            # Try using Ollama locally
            try:
                response = ollama.chat(model='llama3.2', messages=[
                    {"role": "system", "content": f"You are a professional blog writer. Tone: {req.tone}"},
                    {"role": "user", "content": f"Write a {req.length} blog post (~{target_words} words) about '{req.topic}'. Keywords: {req.keywords}. Use markdown."}
                ])
                return {"result": response['message']['content'], "mock": False, "id": 1, "content_type": "blog", "created_at": datetime.now().isoformat()}
            except Exception as e:
                print(f"Ollama Error: {e}")

            return {
                "result": f"# {req.topic}\n\nThis is a {req.length} blog post.\n\n## Introduction\n{req.keywords}\n\n## Content\nLorem ipsum about {req.topic}...",
                "mock": True,
                "id": 1,
                "content_type": "blog",
                "created_at": datetime.now().isoformat()
            }
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a professional blog writer. Tone: {req.tone}"},
                {"role": "user", "content": f"Write a {req.length} blog post (~{target_words} words) about '{req.topic}'. Keywords: {req.keywords}. Use markdown."}
            ],
            temperature=req.temperature,
            max_tokens=target_words * 2
        )
        return {
            "result": response.choices[0].message.content, 
            "mock": False,
            "id": 1,
            "content_type": "blog",
            "created_at": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-social")
async def generate_social(req: SocialMediaRequest):
    try:
        if not client:
            # Try using Ollama locally
            try:
                hashtag_instruction = "Include relevant hashtags." if req.include_hashtags else "No hashtags."
                response = ollama.chat(model='llama3.2', messages=[
                    {"role": "system", "content": f"You are a social media expert. Tone: {req.tone} for {req.platform}."},
                    {"role": "user", "content": f"Write a {req.platform} post about '{req.topic}'. {hashtag_instruction} Use emojis."}
                ])
                return {"result": response['message']['content'], "mock": False, "id": 1, "content_type": "social", "created_at": datetime.now().isoformat()}
            except Exception as e:
                print(f"Ollama Error: {e}")

            hashtags = " #AI #Content" if req.include_hashtags else ""
            return {
                "result": f"🚀 {req.topic}\n\nThis is a {req.tone.lower()} post for {req.platform}.{hashtags}", 
                "mock": True,
                "id": 1,
                "content_type": "social",
                "created_at": datetime.now().isoformat()
            }
        
        hashtag_instruction = "Include relevant hashtags." if req.include_hashtags else "No hashtags."
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a social media expert. Tone: {req.tone} for {req.platform}."},
                {"role": "user", "content": f"Write a {req.platform} post about '{req.topic}'. {hashtag_instruction} Use emojis."}
            ],
            temperature=req.temperature,
            max_tokens=200
        )
        return {
            "result": response.choices[0].message.content, 
            "mock": False,
            "id": 1,
            "content_type": "social",
            "created_at": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/history")
async def get_history():
    return []  

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
