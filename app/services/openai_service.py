from openai import OpenAI
from app.config import settings

# Initialize OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY else None

class OpenAIService:
    """Service for OpenAI API interactions"""
    
    @staticmethod
    async def generate_ad_copy(product_name: str, description: str, audience: str, tone: str, temperature: float = 0.7):
        """Generate marketing ad copy"""
        if not settings.OPENAI_API_KEY or not client:
            return f"""**{product_name} - The Future is Here!**

Are you a {audience} looking for innovation? Our {tone.lower()} solution delivers exactly what you need.

{description if description else "Experience the difference today."}

**Try {product_name} now!**
""", True
        
        try:
            response = client.chat.completions.create(
                model=settings.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": f"You are a professional copywriter. Write in a {tone} tone."},
                    {"role": "user", "content": f"Write a compelling ad for '{product_name}'. Target: {audience}. Description: {description}. Include headline, body, and call-to-action."}
                ],
                temperature=temperature,
                max_tokens=settings.DEFAULT_MAX_TOKENS
            )
            return response.choices[0].message.content, False
        except Exception as e:
            raise Exception(f"OpenAI API Error: {str(e)}")
    
    @staticmethod
    async def generate_image(prompt: str, size: str = "1024x1024"):
        """Generate image using DALL-E"""
        if not settings.OPENAI_API_KEY or not client:
            return "https://picsum.photos/1024/1024", True
        
        try:
            response = client.images.generate(
                prompt=prompt,
                n=1,
                size=size
            )
            return response.data[0].url, False
        except Exception as e:
            raise Exception(f"Image generation error: {str(e)}")
    
    @staticmethod
    async def generate_blog_post(topic: str, keywords: str, tone: str, length: str, temperature: float = 0.7):
        """Generate blog post"""
        word_counts = {"short": 300, "medium": 600, "long": 1000}
        target_words = word_counts.get(length, 600)
        
        if not settings.OPENAI_API_KEY or not client:
            return f"""# {topic}

This is a {length} blog post about {topic}.

## Introduction
{keywords if keywords else "Exploring this fascinating topic..."}

## Main Content
Lorem ipsum dolor sit amet, consectetur adipiscing elit. This would be a comprehensive article about {topic}.

## Conclusion
In conclusion, {topic} is an important subject worth exploring further.
""", True
        
        try:
            response = client.chat.completions.create(
                model=settings.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": f"You are a professional blog writer. Write in a {tone} tone."},
                    {"role": "user", "content": f"Write a {length} blog post (~{target_words} words) about '{topic}'. Include these keywords: {keywords}. Use markdown formatting with headers."}
                ],
                temperature=temperature,
                max_tokens=target_words * 2
            )
            return response.choices[0].message.content, False
        except Exception as e:
            raise Exception(f"Blog generation error: {str(e)}")
    
    @staticmethod
    async def generate_social_post(platform: str, topic: str, tone: str, include_hashtags: bool, temperature: float = 0.8):
        """Generate social media post"""
        char_limits = {
            "twitter": 280,
            "linkedin": 3000,
            "instagram": 2200,
            "facebook": 63206
        }
        limit = char_limits.get(platform.lower(), 280)
        
        if not settings.OPENAI_API_KEY or not client:
            hashtags = " #AI #Content #Marketing" if include_hashtags else ""
            return f"🚀 {topic}\n\nThis is a {tone.lower()} post for {platform}.{hashtags}", True
        
        try:
            hashtag_instruction = "Include relevant hashtags." if include_hashtags else "No hashtags."
            response = client.chat.completions.create(
                model=settings.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": f"You are a social media expert. Write in a {tone} tone for {platform}."},
                    {"role": "user", "content": f"Write a {platform} post about '{topic}'. Max {limit} characters. {hashtag_instruction} Use emojis appropriately."}
                ],
                temperature=temperature,
                max_tokens=200
            )
            return response.choices[0].message.content, False
        except Exception as e:
            raise Exception(f"Social post generation error: {str(e)}")
