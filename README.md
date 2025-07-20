# Interview Analysis System (Web Version)

Upload or record your interview answers and get instant NLP-based feedback!

## Features
- Upload audio (.wav/.mp3/.m4a)
- Speech to text using Whisper
- Sentiment analysis using VADER
- Feedback and pie chart visualization

## Run Locally

```bash
git clone <repo>
cd interview_analysis
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py


---

## 🧪 How to Test Locally

1. Save a `.wav` or `.mp3` file with a sample response.
2. Run `python app.py`
3. Open `http://127.0.0.1:5000`
4. Upload the file and get results.

---

## 🔜 Next Steps?

You can now **pick one or more features** from the 🧠 Enhancements list (e.g., speech fluency, mock interview mode, PDF export, etc.), and I’ll scaffold or implement those next.

Would you like to:
- Add **in-browser recording** next?
- Implement **fluency analysis**?
- Start **session saving** or **PDF report export**?

Let me know what to build next!
