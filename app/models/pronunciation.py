from pydantic import BaseModel
from typing import List, Optional

class PronunciationRequest(BaseModel):
    audio: bytes
    target_phrase: str
    user_id: str

class PronunciationFeedback(BaseModel):
    score: float
    feedback: str
    areas_to_improve: List[str]

class PronunciationResponse(BaseModel):
    score: float
    feedback: str
    areas_to_improve: List[str]
    timestamp: Optional[str] = None
