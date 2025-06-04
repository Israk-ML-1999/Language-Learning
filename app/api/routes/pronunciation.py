from fastapi import APIRouter, HTTPException, Depends
from app.services.ai_service import AIService
from app.services.pronunciation_service import PronunciationService
from app.models.pronunciation import PronunciationRequest, PronunciationResponse
from typing import List

router = APIRouter()
ai_service = AIService()
pronunciation_service = PronunciationService()

@router.post("/evaluate", response_model=PronunciationResponse)
async def evaluate_pronunciation(audio_data: PronunciationRequest):
    """
    Evaluate user's pronunciation and provide feedback
    """
    try:
        # Process audio and get transcription
        transcription = await pronunciation_service.transcribe_audio(audio_data.audio)
        
        # Get AI evaluation
        evaluation = await ai_service.evaluate_pronunciation(
            transcription,
            audio_data.target_phrase
        )
        
        return PronunciationResponse(
            score=evaluation.score,
            feedback=evaluation.feedback,
            areas_to_improve=evaluation.areas_to_improve
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history/{user_id}", response_model=List[PronunciationResponse])
async def get_pronunciation_history(user_id: str):
    """
    Get user's pronunciation history and progress
    """
    try:
        history = await pronunciation_service.get_user_history(user_id)
        return history
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
