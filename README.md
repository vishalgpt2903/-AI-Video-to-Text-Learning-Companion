# 🎥 AI Video-to-Text Learning Companion

> Transform your educational videos into smart study materials instantly!

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.51-red.svg)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-green.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

## 📖 Overview

An AI-powered web application that converts educational videos into:
- 📝 **Text Transcripts** - Full speech-to-text conversion
- 📊 **AI Summaries** - Concise, intelligent summaries
- 🎴 **Flashcards** - Auto-generated study questions

Perfect for students, educators, and lifelong learners who want to maximize their learning efficiency!

## ✨ Features

### 🎯 Core Features
- **Video Upload** - Support for MP4, MOV, MKV formats
- **Audio Extraction** - Automatic audio extraction from videos
- **Speech Recognition** - Google Speech API for accurate transcription
- **AI Summarization** - Powered by Google Gemini AI
- **Smart Flashcards** - Varied question types for effective learning

### 🎨 Modern UI
- **Beautiful Interface** - Clean, professional design with gradient headers
- **Responsive Layout** - Works perfectly on all screen sizes
- **Progress Tracking** - Real-time progress bars and status updates
- **Tabbed Interface** - Organized view of transcript, summary, and flashcards
- **Statistics Dashboard** - Word counts, compression rates, and analytics

### 🔒 Privacy & Security
- **Local Processing** - Videos processed on your machine
- **Auto Cleanup** - Temporary files deleted after processing
- **Secure API Keys** - Environment variables for sensitive data

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Internet connection (for speech recognition & AI)
- Google Gemini API key (free)

### Installation

1. **Clone or download this project**
   ```powershell
   cd "AI video to text summarize"
   ```

2. **Install dependencies** (Already installed)
   ```powershell
   pip install streamlit moviepy SpeechRecognition google-generativeai python-dotenv
   ```

3. **Get your FREE Gemini API key**
   - Visit: https://ai.google.dev/
   - Click "Get API Key"
   - Sign in with Google account
   - Create a new API key

4. **Configure API key**
   
   Create a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```powershell
   streamlit run main.py
   ```

6. **Open in browser**
   - Automatically opens at: http://localhost:8501
   - Or manually visit the URL shown in terminal

## 📱 How to Use

### Step 1: Upload Video
- Click "Browse files" or drag & drop
- Select MP4, MOV, or MKV file
- View file info in the sidebar

### Step 2: Processing
Watch the progress bar as your video is:
1. 🎵 Audio extracted
2. 🎤 Converted to text
3. 📝 Summarized by AI
4. 🎴 Flashcards generated

### Step 3: Review Results
Navigate through tabs:
- **📜 Transcript** - Full text with word count
- **📊 Summary** - AI-generated concise summary
- **🎴 Flashcards** - Expandable study questions

## 🎓 Example Use Cases

- **Students**: Convert lecture videos into study notes
- **Educators**: Create course materials from recorded sessions
- **Content Creators**: Generate transcripts for accessibility
- **Researchers**: Extract key points from presentations
- **Language Learners**: Practice with transcribed content

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit (Python web framework) |
| **Video Processing** | MoviePy |
| **Speech-to-Text** | Google Speech Recognition API |
| **AI Summarization** | Google Gemini 2.5 Flash |
| **Flashcard Generation** | Google Gemini 2.5 Flash |
| **Environment Management** | Python-dotenv |

## 📁 Project Structure

```
AI video to text summarize/
│
├── 📄 main.py                    # Streamlit web app with beautiful UI
├── 🎬 video_utils.py             # Video → Audio extraction
├── 🎤 speech_to_text.py          # Audio → Text transcription
├── 📝 summarizer.py              # Text → AI summary (Gemini)
├── 🎴 flashcard_generator.py     # Summary → Study flashcards
│
├── 🔑 .env                       # Your API keys (keep secret!)
├── 📋 .env.example               # Template for .env
│
├── 📖 README.md                  # This file
├── 📚 DOCUMENTATION.md           # Complete technical docs
│
├── 📂 sample_videos/             # Temporary storage (auto-created)
│   ├── temp_video.mp4           # Uploaded video (auto-deleted)
│   └── audio.wav                # Extracted audio (auto-deleted)
│
└── 🧪 test_video.py             # Testing utilities
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Google Gemini API Key (required for AI features)
GEMINI_API_KEY=your_api_key_here
```

### Modes of Operation

**🤖 AI Mode** (Recommended)
- Requires Gemini API key
- Intelligent summarization
- Smart flashcard questions
- Better understanding of context

**⚡ Basic Mode** (Fallback)
- No API key needed
- Rule-based summarization
- Template-based flashcards
- Still functional, less intelligent

## 📊 Performance

### Processing Times
- **1 min video**: ~30 seconds
- **5 min video**: ~2 minutes
- **10 min video**: ~4 minutes

### API Limits (Free Tier)
- **Google Speech Recognition**: Unlimited (fair use)
- **Google Gemini**: 60 requests/min, 1,500 requests/day

### Best Practices
- ✅ Use videos with clear audio
- ✅ Keep videos under 10 minutes for faster processing
- ✅ Ensure stable internet connection
- ✅ Use videos with spoken content (not just music)

## 🐛 Troubleshooting

### Common Issues

**"Could not transcribe audio"**
- Check if video has clear, audible speech
- Verify internet connection
- Try a different video

**"Basic Mode" instead of "AI Mode"**
- Verify `.env` file exists in project root
- Check API key is correct
- Restart the Streamlit app

**App won't start**
```powershell
# Reinstall dependencies
pip install --upgrade streamlit moviepy SpeechRecognition google-generativeai python-dotenv

# Run with full path
C:/Users/Priyanka/AppData/Local/Programs/Python/Python311/python.exe -m streamlit run main.py
```

**Slow processing**
- Use shorter videos (2-5 minutes optimal)
- Check internet speed
- Close other applications

## 🔐 Security & Privacy

### Data Privacy
- ✅ Videos processed **locally** on your machine
- ✅ Audio sent to Google APIs for processing
- ✅ Temporary files **automatically deleted**
- ✅ No data stored on servers

### API Key Security
- 🔒 Never commit `.env` file to Git
- 🔒 Keep API keys confidential
- 🔒 Monitor usage at https://aistudio.google.com/
- 🔒 Regenerate key if compromised

## 📈 Future Enhancements

Potential features for future versions:
- [ ] Multiple language support
- [ ] YouTube URL direct processing
- [ ] PDF export of transcripts
- [ ] Multiple choice questions
- [ ] User authentication & history
- [ ] Batch processing multiple videos
- [ ] Custom AI prompts
- [ ] Audio quality enhancement

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Streamlit** - For the amazing web framework
- **Google** - For Speech Recognition & Gemini AI APIs
- **MoviePy** - For video processing capabilities
- **Open Source Community** - For inspiration and support

## 📞 Support & Documentation

- **Quick Start**: This README
- **Full Documentation**: See [DOCUMENTATION.md](DOCUMENTATION.md)
- **API Issues**: Check https://ai.google.dev/
- **Streamlit Docs**: https://docs.streamlit.io/

## 🎉 Screenshots

### Main Interface
- Beautiful gradient header
- Clean file upload area
- Real-time processing status

### Results View
- Tabbed interface for easy navigation
- Statistics and analytics
- Expandable flashcards
- Professional styling

---

**Made with ❤️ using Python, Streamlit & Google Gemini AI**

*Transform your learning experience today!* 🚀

---

**Version**: 1.0  
**Last Updated**: November 25, 2025  
**Status**: ✅ Production Ready
