# 🎥 AI Video-to-Text Learning Companion

Convert videos to text transcripts, AI-powered summaries, and educational flashcards!

## ✨ Features

- **Video to Audio Extraction** - Extract audio from MP4, MOV, MKV videos
- **Speech Recognition** - Convert audio to text using Google Speech API
- **AI Summarization** - Intelligent summaries using OpenAI GPT (optional)
- **Smart Flashcards** - AI-generated questions for learning (optional)

## 🚀 Setup Instructions

### 1. Install Dependencies
All packages are already installed. If you need to reinstall:
```powershell
pip install streamlit moviepy SpeechRecognition openai python-dotenv
```

### 2. Configure OpenAI API (Optional - for AI features)

**To enable full AI-powered features:**

1. Get an OpenAI API key from: https://platform.openai.com/api-keys

2. Create a `.env` file in this directory:
```powershell
Copy-Item .env.example .env
```

3. Edit `.env` and add your API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**Note:** Without the API key, the app still works with basic rule-based summarization and flashcards.

## 🎯 Running the Application

```powershell
streamlit run main.py
```

Or use the full Python path:
```powershell
C:/Users/Priyanka/AppData/Local/Programs/Python/Python311/python.exe -m streamlit run main.py
```

The app will open in your browser at http://localhost:8501

## 📝 How to Use

1. **Upload a Video** - Click "Browse files" and select your video (MP4, MOV, or MKV)
2. **Wait for Processing** - The app will:
   - Extract audio from video
   - Convert speech to text
   - Generate a summary
   - Create flashcards
3. **Review Results** - Read the transcript, summary, and study with flashcards!

## 🔧 Modes

### AI Mode (With OpenAI API Key)
- ✅ Intelligent GPT-powered summaries
- ✅ Smart, varied flashcard questions
- ✅ Better understanding of context

### Basic Mode (Without API Key)
- ✅ Rule-based extractive summaries
- ✅ Template-based flashcard generation
- ✅ Still functional, just less "intelligent"

## 📁 Project Structure

```
├── main.py                    # Streamlit web application
├── video_utils.py            # Video to audio extraction
├── speech_to_text.py         # Audio to text conversion
├── summarizer.py             # Text summarization (AI + fallback)
├── flashcard_generator.py    # Flashcard generation (AI + fallback)
├── .env                      # Your API keys (create this)
├── .env.example              # Template for .env
└── sample_videos/            # Temporary storage for uploads
```

## 🐛 Troubleshooting

**Issue: "Could not transcribe audio"**
- Ensure video has clear audio
- Try shorter videos (under 5 minutes work best)
- Check internet connection (for Google Speech API)

**Issue: "Basic Mode" shown in sidebar**
- Create `.env` file with valid OPENAI_API_KEY
- Restart the Streamlit app after adding the key

**Issue: MoviePy import errors**
- The correct import is already fixed in the code
- Uses: `from moviepy.video.io.VideoFileClip import VideoFileClip`

## 💡 Tips

- **Video Length**: Shorter videos (1-5 minutes) work best
- **Audio Quality**: Clear speech gives better transcription
- **Internet**: Required for speech recognition (Google API)
- **Cost**: OpenAI API has usage costs - monitor your usage at https://platform.openai.com/usage

## 🎓 Technologies Used

- **Streamlit** - Web interface
- **MoviePy** - Video processing
- **SpeechRecognition** - Audio to text
- **OpenAI GPT-3.5** - AI summarization & flashcards (optional)
- **Python-dotenv** - Environment management
