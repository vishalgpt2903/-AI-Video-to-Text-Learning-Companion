import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re

# Load environment variables
load_dotenv()

def generate_flashcards(summary_text):
    """AI-powered flashcard generation using Google Gemini"""
    if not summary_text or len(summary_text.strip()) == 0:
        return []
    
    # Check if API key is available
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key or api_key == 'your_gemini_api_key_here':
        # Fallback to rule-based generation
        return fallback_generate_flashcards(summary_text)
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""Create 5-6 educational flashcards from this summary. 
Generate varied question types (What is, How, Why, Explain, etc.).
Return ONLY a JSON array format with no additional text.

Summary: {summary_text}

Format: [{{"question": "What is...", "answer": "..."}}, {{"question": "How...", "answer": "..."}}]

JSON:"""
        
        response = model.generate_content(prompt)
        content = response.text.strip()
        
        # Try to parse JSON
        try:
            # Remove markdown code blocks if present
            if '```json' in content:
                content = content.split('```json')[1].split('```')[0].strip()
            elif '```' in content:
                content = content.split('```')[1].split('```')[0].strip()
            
            # Try to extract JSON array
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                content = json_match.group(0)
            
            flashcards = json.loads(content)
            return flashcards[:6]  # Limit to 6 cards
        except:
            # If parsing fails, fallback
            return fallback_generate_flashcards(summary_text)
        
    except Exception as e:
        # Fallback to rule-based if API fails
        return fallback_generate_flashcards(summary_text)

def fallback_generate_flashcards(summary_text):
    """Fallback rule-based flashcard generation"""
    sentences = summary_text.split(". ")
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    flashcards = []
    
    question_templates = [
        "What is {}?",
        "Explain {}.",
        "What does the video say about {}?",
        "According to the video, what is {}?",
        "How is {} described?"
    ]
    
    for idx, sentence in enumerate(sentences):
        if len(sentence) < 20:
            continue
            
        words = sentence.split()
        key_phrases = []
        
        if ' is ' in sentence.lower():
            topic = sentence.lower().split(' is ')[0].strip()
            key_phrases.append(topic)
        elif ' hai ' in sentence.lower():
            topic = sentence.lower().split(' hai ')[0].strip()
            key_phrases.append(topic)
        
        if not key_phrases:
            key_phrases.append(' '.join(words[:min(5, len(words))]))
        
        template = question_templates[idx % len(question_templates)]
        question = template.format(key_phrases[0])
        
        flashcards.append({
            "question": question,
            "answer": sentence
        })
    
    if len(sentences) > 0:
        flashcards.insert(0, {
            "question": "What is the main topic of this video?",
            "answer": sentences[0]
        })
    
    return flashcards[:6]
