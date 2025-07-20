# utils/gemini_feedback.py
import google.generativeai as genai
import os

# Load Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_feedback(transcript, sentiment, fluency):
    prompt = f"""
    You are an AI interview coach. Analyze this interview response and provide:
    - Constructive feedback on tone, content, and clarity
    - Suggestions for improvement
    - Strengths to highlight

    --- TRANSCRIPT ---
    {transcript}

    --- SENTIMENT ---
    {sentiment}

    --- FLUENCY METRICS ---
    Words per Minute: {fluency['wpm']}
    Filler Word Count: {fluency['filler_count']} ({fluency['filler_ratio']*100:.2f}%)

    Reply in clear bullet points.
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini Feedback Error: {str(e)}"
