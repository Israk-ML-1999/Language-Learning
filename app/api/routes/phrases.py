from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.models.phrases import PhraseCreate, PhraseResponse, PhraseFilter
from app.services.ai_service import AIService
from app.core.config import settings

router = APIRouter()
ai_service = AIService()

@router.post("/create", response_model=PhraseResponse)
async def create_phrase(phrase: PhraseCreate):
    """
    Create a new custom phrase with AI-generated examples
    """
    try:
        # Generate AI suggestions for the phrase
        suggestions = await ai_service.generate_phrases(
            topic=phrase.category,
            difficulty=phrase.difficulty_level,
            count=3
        )
        
        response = PhraseResponse(
            id=1,  # This should come from database
            text=phrase.text,
            category=phrase.category,
            difficulty_level=phrase.difficulty_level,
            language=phrase.language,
            example_usage=suggestions[0] if suggestions else None,
            ai_suggestions=suggestions
        )
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/suggestions", response_model=List[str])
async def get_phrase_suggestions(
    topic: str,
    difficulty: str = "intermediate",
    count: int = 5
):
    """
    Get AI-generated phrase suggestions based on topic and difficulty
    """
    try:
        suggestions = await ai_service.generate_phrases(
            topic=topic,
            difficulty=difficulty,
            count=count
        )
        return suggestions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search", response_model=List[PhraseResponse])
async def search_phrases(filters: PhraseFilter = Depends()):
    """
    Search phrases based on category, difficulty level, and language
    """
    try:
        # TODO: Implement database integration
        # This is a placeholder response
        return [
            PhraseResponse(
                id=1,
                text="Example phrase",
                category=filters.category or "General",
                difficulty_level=filters.difficulty_level or "intermediate",
                language=filters.language or "English",
                example_usage="Example context",
                ai_suggestions=["Suggestion 1", "Suggestion 2"]
            )
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
