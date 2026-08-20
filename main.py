import sys
import os
import cv2

# Ensure Python can find local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vision.detector import ObjectDetector
from vision.tracker import CentroidTracker
from knowledge.object_info import get_object_info
from speech.tts import speak
from utils.helpers import draw_bbox, limit_frame_size
from config import YOLO_MODEL_PATH, CONFIDENCE_THRESHOLD, TRACKER_MAX_DISAPPEARED, DEBUG

# ---------------------------
# Initialize Modules
# ---------------------------
detector = ObjectDetector(model_path=YOLO_MODEL_PATH, conf_threshold=CONFIDENCE_THRESHOLD)
tracker = CentroidTracker(max_disappeared=TRACKER_MAX_DISAPPEARED)
spoken_ids = set()  # Keep track of objects already spoken

# ---------------------------
# Start Webcam with HD Resolution
# ---------------------------
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Height

if not cap.isOpened():
    print("❌ Cannot open webcam")
    exit()

speak("Hello Ganesh, Jarvis AI is ready to detect objects.")

# ---------------------------
# Main Loop
# ---------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Resize frame for performance while keeping HD aspect ratio
    frame = limit_frame_size(frame, width=1280)

    # ---------------------------
    # Detect Objects
    # ---------------------------
    results = detector.detect(frame)  # [(label, (x1,y1,x2,y2), conf), ...]
    rects = [bbox for _, bbox, _ in results]

    # ---------------------------
    # Update Tracker
    # ---------------------------
    objects = tracker.update(rects)

    # ---------------------------
    # Draw Bounding Boxes & Speak
    # ---------------------------
    for idx, (label, bbox, conf) in enumerate(results):
        draw_bbox(frame, bbox, label, conf)

        # Speak only for new objects
        if idx not in spoken_ids:
            info = get_object_info(label)
            speak(f"I see a {label}. {info}")
            spoken_ids.add(idx)

        if DEBUG:
            print(f"Detected: {label}, Confidence: {conf:.2f}")

    # ---------------------------
    # Display Frame
    # ---------------------------
    cv2.imshow("Jarvis Vision AI - HD", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        speak("Goodbye Ganesh!")
        break

# ---------------------------
# Cleanup
# ---------------------------
cap.release()
cv2.destroyAllWindows()