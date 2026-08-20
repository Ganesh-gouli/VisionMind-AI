import os

YOLO_MODEL_PATH = "yolov8n.pt"
CONFIDENCE_THRESHOLD = 0.3
TRACKER_MAX_DISAPPEARED = 50
DEBUG = True

TTS_RATE = 170
TTS_VOLUME = 1.0

# Gemini API Key (Loaded from environment variable for security)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

