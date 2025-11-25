import streamlit as st
import os
from dotenv import load_dotenv
from video_utils import extract_audio
from speech_to_text import audio_to_text
from summarizer import summarize_text
from flashcard_generator import generate_flashcards

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Video Learning Companion",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #667eea;
        color: white;
        border-radius: 5px;
        padding: 0.5rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #764ba2;
    }
    .flashcard {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #667eea;
    }
    .stat-box {
        background-color: #e8eaf6;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>🎥 AI Video-to-Text Learning Companion</h1>
        <p>Transform your videos into smart study materials instantly!</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🔧 Settings & Info")
    
    # API status
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key and api_key != 'your_gemini_api_key_here':
        st.success("✅ AI Mode Active")
        st.markdown("**Powered by:** Google Gemini")
    else:
        st.warning("⚠️ Basic Mode")
        st.info("💡 Add GEMINI_API_KEY to .env for AI features")
    
    st.markdown("---")
    
    # Instructions
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. **Upload** your video file
    2. **Wait** for processing
    3. **Review** transcript & summary
    4. **Study** with flashcards
    """)
    
    st.markdown("---")
    
    # Supported formats
    st.markdown("### 📹 Supported Formats")
    st.markdown("✅ MP4 • MOV • MKV")
    
    st.markdown("---")
    
    # Tips
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Use videos with **clear audio**
    - Keep videos **under 10 minutes**
    - Ensure **good internet** connection
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📤 Upload Your Video")
    uploaded_file = st.file_uploader(
        "Drag and drop or click to browse",
        type=["mp4", "mov", "mkv"],
        help="Select a video file to process"
    )

with col2:
    if uploaded_file:
        st.markdown("### 📊 File Info")
        file_size = len(uploaded_file.getvalue()) / (1024 * 1024)  # MB
        st.markdown(f"""
        <div class="stat-box">
            <h4>{uploaded_file.name}</h4>
            <p>Size: {file_size:.2f} MB</p>
        </div>
        """, unsafe_allow_html=True)

# Processing section
if uploaded_file is not None:
    # Create directory if it doesn't exist
    os.makedirs("sample_videos", exist_ok=True)
    
    video_path = "sample_videos/temp_video.mp4"
    audio_path = "sample_videos/audio.wav"
    
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())
    
    try:
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Step 1: Extract audio
        status_text.markdown("🎵 **Step 1/4:** Extracting audio...")
        progress_bar.progress(25)
        audio_file = extract_audio(video_path, audio_path)
        
        # Step 2: Convert to text
        status_text.markdown("🎤 **Step 2/4:** Converting speech to text...")
        progress_bar.progress(50)
        transcript = audio_to_text(audio_file)
        
        # Step 3: Summarize
        status_text.markdown("📝 **Step 3/4:** Generating AI summary...")
        progress_bar.progress(75)
        summary = summarize_text(transcript)
        
        # Step 4: Flashcards
        status_text.markdown("🎴 **Step 4/4:** Creating flashcards...")
        progress_bar.progress(100)
        flashcards = generate_flashcards(summary)
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        # Success message
        st.markdown("""
            <div class="success-box">
                ✅ <strong>Processing Complete!</strong> Your video has been successfully analyzed.
            </div>
        """, unsafe_allow_html=True)
        
        # Results in tabs
        tab1, tab2, tab3 = st.tabs(["📜 Transcript", "📊 Summary", "🎴 Flashcards"])
        
        with tab1:
            st.markdown("### 📜 Full Transcript")
            st.markdown("*Complete text extracted from your video*")
            st.text_area(
                "Transcript",
                transcript,
                height=300,
                label_visibility="collapsed"
            )
            
            # Word count
            word_count = len(transcript.split())
            st.caption(f"📊 Word count: {word_count} words")
        
        with tab2:
            st.markdown("### 📊 AI-Generated Summary")
            st.markdown("*Key points extracted by AI*")
            st.markdown(f"""
            <div style="background-color: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #667eea;">
                {summary}
            </div>
            """, unsafe_allow_html=True)
            
            # Summary stats
            summary_words = len(summary.split())
            compression = (1 - summary_words/word_count) * 100 if word_count > 0 else 0
            st.caption(f"📊 Summary: {summary_words} words | 🗜️ Compression: {compression:.1f}%")
        
        with tab3:
            st.markdown("### 🎴 Study Flashcards")
            st.markdown("*Generated questions for effective learning*")
            
            if flashcards:
                for idx, card in enumerate(flashcards, 1):
                    with st.expander(f"📌 Question {idx}", expanded=(idx==1)):
                        st.markdown(f"**Q:** {card['question']}")
                        st.markdown(f"**A:** {card['answer']}")
                        st.markdown("---")
                
                st.success(f"✨ Generated {len(flashcards)} flashcards for your study!")
            else:
                st.warning("⚠️ No flashcards could be generated. Try a video with more content.")
    
    except Exception as e:
        st.error(f"❌ **Error:** {str(e)}")
        st.info("💡 Try uploading a different video or check your internet connection.")
    
    finally:
        # Cleanup temporary files
        for file_path in [video_path, audio_path]:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except:
                    pass

else:
    # Welcome message when no file is uploaded
    st.markdown("""
        <div style="text-align: center; padding: 3rem; background-color: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
            <h3>👋 Welcome!</h3>
            <p style="font-size: 1.1rem; color: #666;">
                Upload a video to get started. We'll convert it into transcript, summary, and flashcards!
            </p>
            <br>
            <p style="color: #999;">
                🎯 Perfect for students, educators, and lifelong learners
            </p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>Made with ❤️ using Streamlit & Google Gemini AI</p>
        <p style="font-size: 0.9rem;">🔒 Your videos are processed locally and deleted after analysis</p>
    </div>
""", unsafe_allow_html=True)
