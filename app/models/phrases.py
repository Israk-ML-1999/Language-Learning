from pydantic import BaseModel
from typing import List, Optional

class PhraseBase(BaseModel):
    text: str
    category: str
    difficulty_level: str
    language: str

class PhraseCreate(PhraseBase):
    user_id: str

class PhraseResponse(PhraseBase):
    id: int
    example_usage: Optional[str] = None
    ai_suggestions: Optional[List[str]] = None

class PhraseFilter(BaseModel):
    category: Optional[str] = None
    difficulty_level: Optional[str] = None
    language: Optional[str] = None
