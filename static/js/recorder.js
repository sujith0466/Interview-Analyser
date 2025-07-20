let recognition;
let finalTranscript = "";

const recordBtn = document.getElementById('record-btn');
const stopBtn = document.getElementById('stop-btn');
const preview = document.getElementById('audio-preview');
const loading = document.getElementById('loading');

recordBtn.addEventListener('click', () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
        alert("Speech recognition not supported in this browser.");
        return;
    }

    recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = true;  // show live interim results
    recognition.continuous = true;

    finalTranscript = "";
    preview.innerHTML = "<p>🎤 Listening... Speak now.</p>";
    loading.style.display = "none";

    recognition.onresult = (event) => {
        let interimTranscript = "";
        for (let i = event.resultIndex; i < event.results.length; i++) {
            const transcript = event.results[i][0].transcript;
            if (event.results[i].isFinal) {
                finalTranscript += transcript + " ";
            } else {
                interimTranscript += transcript;
            }
        }
        preview.innerHTML = `<strong>Transcript:</strong> ${finalTranscript}${interimTranscript}`;
    };

    recognition.onerror = (event) => {
        alert("Speech recognition error: " + event.error);
        recordBtn.disabled = false;
        stopBtn.disabled = true;
        loading.style.display = "none";
        preview.innerHTML = "";
    };

    recognition.start();
    recordBtn.disabled = true;
    stopBtn.disabled = false;
});

stopBtn.addEventListener('click', () => {
    if (recognition) recognition.stop();

    stopBtn.disabled = true;
    recordBtn.disabled = false;

    const trimmedTranscript = finalTranscript.trim();
    if (!trimmedTranscript) {
        alert("No transcript captured. Please try again.");
        preview.innerHTML = "";
        loading.style.display = "none";
        return;
    }

    loading.style.display = "block";

    // Create and submit form with transcript
    const form = document.createElement('form');
    form.method = "POST";
    form.action = "/analyze";

    const input = document.createElement('input');
    input.type = "hidden";
    input.name = "web_transcript";
    input.value = trimmedTranscript;

    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
});
