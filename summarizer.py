import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def summarize_text(text):
    """AI-powered summarization using Google Gemini"""
    if not text or len(text.strip()) == 0:
        return "No text to summarize."
    
    # Check if API key is available
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key or api_key == 'your_gemini_api_key_here':
        # Fallback to rule-based summarization
        return fallback_summarize(text)
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""Summarize the following video transcript concisely in 3-4 clear sentences. 
Focus on the main points and key information:

{text}

Summary:"""
        
        response = model.generate_content(prompt)
        summary = response.text.strip()
        return summary
        
    except Exception as e:
        # Fallback to rule-based if API fails
        return fallback_summarize(text)

def fallback_summarize(text):
    """Fallback rule-based summarization"""
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    sentences = [s.strip() for s in sentences if len(s.strip()) > 15]
    
    if len(sentences) == 0:
        return text[:300]
    
    summary_sentences = []
    if len(sentences) > 0:
        summary_sentences.append(sentences[0])
    
    for i in range(2, len(sentences), 3):
        if len(summary_sentences) < 4:
            summary_sentences.append(sentences[i])
    
    if len(summary_sentences) < 2 and len(sentences) > 1:
        summary_sentences.append(sentences[len(sentences)//2])
    
    return '. '.join(summary_sentences) + '.'

