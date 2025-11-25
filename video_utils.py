from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def extract_audio(video_path, audio_path="audio.wav"):
    try:
        video = VideoFileClip(video_path)
        if video.audio is None:
            raise ValueError("Video has no audio track")
        # Ensure WAV format with correct parameters for speech recognition
        video.audio.write_audiofile(audio_path, codec='pcm_s16le', fps=16000, nbytes=2, buffersize=2000)
        video.close()
        return audio_path
    except Exception as e:
        raise Exception(f"Error extracting audio: {str(e)}")

