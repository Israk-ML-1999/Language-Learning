import speech_recognition as sr
import numpy as np
from typing import List, Dict, Any
import sounddevice as sd
from scipy.io import wavfile
import io
import tempfile
import os

class PronunciationService:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    async def transcribe_audio(self, audio_data: bytes) -> str:
        """
        Transcribe audio data to text using speech recognition
        """
        try:
            # Create a temporary file to store the audio
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
                temp_audio.write(audio_data)
                temp_audio_path = temp_audio.name

            # Use speech recognition to transcribe
            with sr.AudioFile(temp_audio_path) as source:
                audio = self.recognizer.record(source)
                transcription = self.recognizer.recognize_google(audio)
                
            # Clean up temporary file
            os.remove(temp_audio_path)
            
            return transcription
        except Exception as e:
            raise Exception(f"Error transcribing audio: {str(e)}")

    async def get_user_history(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve user's pronunciation history
        This is a placeholder - implement database integration for actual storage
        """
        # TODO: Implement database integration
        return [
            {
                "score": 85.5,
                "feedback": "Good pronunciation, minor improvements needed",
                "areas_to_improve": ["Intonation", "Word stress"],
                "timestamp": "2023-06-04T10:00:00Z"
            }
        ]

    def analyze_audio_features(self, audio_data: bytes) -> Dict[str, Any]:
        """
        Analyze audio features like pitch, rhythm, and stress
        """
        try:
            # Convert bytes to numpy array
            audio_array = np.frombuffer(audio_data, dtype=np.float32)
            
            # Calculate basic audio features
            features = {
                "duration": len(audio_array) / 44100,  # Assuming 44.1kHz sample rate
                "average_amplitude": np.mean(np.abs(audio_array)),
                "max_amplitude": np.max(np.abs(audio_array)),
                "zero_crossings": np.sum(np.diff(np.signbit(audio_array)))
            }
            
            return features
        except Exception as e:
            raise Exception(f"Error analyzing audio features: {str(e)}")

    @staticmethod
    def save_recording(audio_data: bytes, file_path: str):
        """
        Save audio recording to file
        """
        try:
            # Convert bytes to numpy array and save as WAV
            audio_array = np.frombuffer(audio_data, dtype=np.float32)
            wavfile.write(file_path, 44100, audio_array)
        except Exception as e:
            raise Exception(f"Error saving audio recording: {str(e)}")
