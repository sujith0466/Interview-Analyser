import os
import wave
import speech_recognition as sr

def transcribe_audio(file_path):
    duration = get_audio_duration(file_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    try:
        transcript = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        transcript = "Could not understand the audio."
    except sr.RequestError as e:
        transcript = f"Web API unavailable or network issue: {e}"
    except Exception as e:
        transcript = f"Error during transcription: {e}"

    return transcript, duration

def get_audio_duration(path):
    try:
        with wave.open(path, 'rb') as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            return round(frames / float(rate), 2)
    except Exception:
        return 0
