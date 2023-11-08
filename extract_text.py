import moviepy.editor as mp
import speech_recognition as sr
from promptflow import tool

@tool
def transcribe_video():
    video_path = "video.MP4"
    audio_path = "audio.wav"

    recognizer = sr.Recognizer()
    
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_sphinx(audio)
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Speech recognition error; {e}"

if __name__ == "__main":
    transcribed_text = transcribe_video()

    print(transcribed_text)
