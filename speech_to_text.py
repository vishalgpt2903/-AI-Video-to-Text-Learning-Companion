import speech_recognition as sr
import os

def audio_to_text(audio_path):
    """
    Convert audio to text using speech_recognition library with Google API.
    For longer videos, processes in chunks.
    """
    recognizer = sr.Recognizer()
    full_text = []
    
    try:
        with sr.AudioFile(audio_path) as source:
            # Get total duration
            audio_length = int(source.DURATION) if hasattr(source, 'DURATION') else 60
            
            # Process in 30-second chunks for better results
            chunk_duration = 30
            offset = 0
            
            while offset < audio_length:
                try:
                    # Record chunk
                    audio_chunk = recognizer.record(source, duration=min(chunk_duration, audio_length - offset))
                    
                    # Transcribe chunk
                    text = recognizer.recognize_google(audio_chunk, language='en-US')
                    if text:
                        full_text.append(text)
                    
                    offset += chunk_duration
                    
                except sr.UnknownValueError:
                    # Skip chunks that can't be understood
                    offset += chunk_duration
                    continue
                except sr.RequestError as e:
                    return f"API request error: {e}. Check your internet connection."
        
        if full_text:
            return " ".join(full_text)
        else:
            return "Could not transcribe audio. The video may not contain clear speech."
            
    except Exception as e:
        return f"Error: {str(e)}"
