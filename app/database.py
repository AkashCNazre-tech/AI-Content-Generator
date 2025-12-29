from sqlalchemy import create_engine, String, Text
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from typing import Optional
from app.config import settings

class Base(DeclarativeBase):
    pass

class ContentItem(Base):
    """Database model for generated content"""
    __tablename__ = "content_items"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content_type: Mapped[str] = mapped_column(String(50))
    prompt: Mapped[str] = mapped_column(Text)
    result: Mapped[str] = mapped_column(Text)
    content_metadata: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
