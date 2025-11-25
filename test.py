from video_utils import extract_audio
from speech_to_text import audio_to_text
from summarizer import summarize_text
from flashcard_generator import generate_flashcards

# Step 1: Extract audio
audio_file = extract_audio("sample_videos/test_video.mp4")
print("Audio extracted:", audio_file)

# Step 2: Convert audio to text
transcript = audio_to_text(audio_file)
print("Transcript:", transcript[:500], "...")

# Step 3: Summarize transcript
summary = summarize_text(transcript)
print("Summary:", summary)

# Step 4: Generate flashcards
flashcards = generate_flashcards(summary)
for idx, card in enumerate(flashcards):
    print(f"Q{idx+1}: {card['question']}")
    print(f"A{idx+1}: {card['answer']}\n")
