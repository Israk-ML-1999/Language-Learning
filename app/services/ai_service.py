import openai
from app.core.config import settings
from typing import List, Dict, Any
import json

class AIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    async def evaluate_pronunciation(self, transcription: str, target_phrase: str) -> Dict[str, Any]:
        """
        Evaluate pronunciation using OpenAI's GPT model
        """
        prompt = f"""
        Evaluate the pronunciation accuracy between:
        Target phrase: "{target_phrase}"
        Transcribed audio: "{transcription}"
        
        Provide a detailed analysis with:
        1. Accuracy score (0-100)
        2. Specific feedback
        3. Areas to improve
        """

        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a language learning assistant specialized in pronunciation evaluation."},
                {"role": "user", "content": prompt}
            ]
        )

        # Process the AI response
        try:
            analysis = response.choices[0].message.content
            # Parse the analysis to extract score, feedback, and areas to improve
            # This is a simplified example - you might want to make this more robust
            return {
                "score": self._extract_score(analysis),
                "feedback": self._extract_feedback(analysis),
                "areas_to_improve": self._extract_areas(analysis)
            }
        except Exception as e:
            raise Exception(f"Error processing AI response: {str(e)}")

    async def generate_phrases(self, topic: str, difficulty: str, count: int = 5) -> List[str]:
        """
        Generate custom phrases based on topic and difficulty
        """
        prompt = f"""
        Generate {count} {difficulty} level phrases about {topic}.
        Each phrase should be natural and commonly used in conversations.
        """

        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a language learning content creator."},
                {"role": "user", "content": prompt}
            ]
        )

        phrases = response.choices[0].message.content.split('\n')
        return [phrase.strip() for phrase in phrases if phrase.strip()]

    def _extract_score(self, analysis: str) -> float:
        """Extract numerical score from AI analysis"""
        try:
            # Implement logic to extract score from the analysis text
            # This is a simplified version
            if "score" in analysis.lower():
                score_text = analysis.split("score")[1].split("\n")[0]
                return float(next(num for num in score_text.split() if num.replace('.', '').isdigit()))
            return 70.0  # Default score if parsing fails
        except:
            return 70.0

    def _extract_feedback(self, analysis: str) -> str:
        """Extract feedback from AI analysis"""
        try:
            # Implement logic to extract main feedback
            if "feedback" in analysis.lower():
                return analysis.split("feedback")[1].split("\n")[0].strip()
            return "Keep practicing!"
        except:
            return "Keep practicing!"

    def _extract_areas(self, analysis: str) -> List[str]:
        """Extract areas to improve from AI analysis"""
        try:
            # Implement logic to extract areas to improve
            areas = []
            if "areas to improve" in analysis.lower():
                areas_text = analysis.split("areas to improve")[1].split("\n")
                areas = [area.strip('- ').strip() for area in areas_text if area.strip('- ').strip()]
            return areas if areas else ["General pronunciation"]
        except:
            return ["General pronunciation"]
