

Readme · MD
GymSync
AI-powered virtual fitness coach that uses real-time computer vision to track exercise form, count reps, and deliver spoken corrective feedback — no human trainer required.

Overview
GymSync captures live webcam video, extracts body pose landmarks using MediaPipe, and analyzes joint angles to identify exercises, count repetitions, and detect form errors in real time. When an issue is detected (e.g. insufficient squat depth, poor spinal alignment), the system generates natural-language coaching feedback via an LLM and speaks it back to the user through text-to-speech — giving the experience of a live coach correcting form mid-set.

Features
Real-time pose tracking via webcam (MediaPipe Pose, 33 landmarks)
Automatic rep counting per exercise using joint-angle state machines
Form-error detection against per-exercise angle thresholds
AI-generated, spoken corrective feedback (Groq LLM + gTTS)
Session logging and progress dashboard (pandas + Plotly)
Single-app architecture — no separate frontend/backend
Tech stack
Layer	Tool
App framework	Streamlit
Live video	streamlit-webrtc
Pose estimation	MediaPipe
Frame processing	OpenCV (headless)
AI feedback generation	Groq
Voice output	gTTS
Data logging	pandas
Dashboard	Plotly
Config/secrets	python-dotenv
Project structure
GymSync/
├── main.py
├── requirements.txt
└── service/
    ├── auth/          # login/session handling
    ├── coaching/       # Groq integration, feedback generation
    ├── config/         # env vars, thresholds, constants
    ├── persistence/     # saving/loading workout history
    ├── state/           # session_state defaults and management
    ├── tracking/         # pose analysis, angle calc, rep/form logic
    └── ui/               # Streamlit UI helpers, chart formatting
Setup
Clone the repo:
   git clone https://github.com/venkatshardul/AI_Gym-trainer.git
   cd AI_Gym-trainer
Create and activate a virtual environment:
   uv venv
   .venv\Scripts\activate
Install dependencies:
   uv pip install -r requirements.txt
Create a .env file in the project root with your Groq API key:
   GROQ_API_KEY=your_key_here
Run the app:
   streamlit run main.py
Status
Work in progress — final-year project. Core tracking and feedback loop under active development.

License
Academic project — not currently licensed for reuse.


