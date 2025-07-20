import re

FILLER_WORDS = {'um', 'uh', 'like', 'you know', 'so', 'actually', 'basically'}

def analyze_fluency(transcript, duration_sec):
    words = transcript.split()
    word_count = len(words)
    wpm = (word_count / duration_sec) * 60 if duration_sec > 0 else 0

    filler_count = sum(1 for w in words if w.lower() in FILLER_WORDS)
    filler_ratio = filler_count / word_count if word_count > 0 else 0

    return {
        "word_count": word_count,
        "wpm": round(wpm, 2),
        "filler_count": filler_count,
        "filler_ratio": round(filler_ratio, 2)
    }
