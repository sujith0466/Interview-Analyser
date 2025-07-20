from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

# Import your custom utility modules
from utils.stt import transcribe_audio  # Optional if audio upload ever returns
from utils.nlp_analysis import analyze_sentiment
from utils.charts import generate_sentiment_chart
from utils.fluency import analyze_fluency
from utils.gemini_feedback import get_gemini_feedback


# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)

# Home page (record + results in same index.html)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', transcript=None)

# POST route for handling transcript submission from browser
@app.route('/analyze', methods=['POST'])
def analyze():
    transcript = ""
    duration = 0

    # Only accepting web_transcript from JS
    if 'web_transcript' in request.form:
        transcript = request.form.get('web_transcript', '').strip()
        if not transcript:
            return "Empty transcript received", 400
        duration = len(transcript.split()) / 2.5  # Estimate duration
    else:
        return "No valid input provided", 400

    # Run NLP + Fluency + Gemini Feedback
    sentiment, scores = analyze_sentiment(transcript)
    chart_path = generate_sentiment_chart(scores)
    fluency = analyze_fluency(transcript, duration)
    gemini_feedback = get_gemini_feedback(transcript, sentiment, fluency)

    # Return results inside index.html
    return render_template('index.html',
                           transcript=transcript,
                           sentiment=sentiment,
                           chart_url=chart_path,
                           fluency=fluency,
                           gemini_feedback=gemini_feedback)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
