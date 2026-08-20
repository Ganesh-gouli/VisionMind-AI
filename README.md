# 🧠 VisionMind-AI (Jarvis Vision)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)](https://opencv.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF.svg)](https://docs.ultralytics.com/)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)

**VisionMind-AI** is an intelligent real-time Computer Vision system powered by **YOLOv8**, **OpenCV**, and **Text-to-Speech (TTS)** voice feedback. It detects objects via live video feed, tracks them using centroid tracking, announces new objects audibly, and dynamically retrieves real-world knowledge and facts about detected items via Wikipedia.

---

## ✨ Features

- 🎥 **Real-Time Object Detection**: Powered by Ultralytics **YOLOv8** for high-speed, accurate multi-object recognition.
- 🎯 **Centroid Object Tracking**: Tracks objects across consecutive video frames to prevent duplicate audio alerts.
- 🔊 **Asynchronous Text-to-Speech (TTS)**: Non-blocking multi-threaded voice output using `pyttsx3` for seamless audio announcements.
- 📚 **Dynamic Knowledge Integration**: Fetches real-time Wikipedia summaries for detected objects with intelligent offline fallbacks.
- 💻 **HD Webcam Stream & Visual Overlays**: Real-time bounding box rendering, confidence scores, and smooth HD frame scaling using OpenCV.
- 🔒 **Configurable & Safe**: Modular architecture with configurable confidence thresholds, tracking parameters, and environment variable support.

---

## 🛠️ Project Architecture

```
VisionMind-AI/
├── knowledge/          # Knowledge base & Wikipedia summary fetcher
│   ├── object_info.py  # Fact retrieval with offline fallbacks
│   └── __init__.py
├── speech/             # Text-to-Speech engine
│   ├── tts.py          # Asynchronous multi-threaded TTS worker
│   └── __init__.py
├── utils/              # Helper utilities
│   ├── helpers.py      # Bounding box rendering & frame resizing
│   └── __init__.py
├── vision/             # Computer Vision core modules
│   ├── detector.py     # YOLOv8 object detection wrapper
│   ├── tracker.py      # Centroid tracking module
│   └── __init__.py
├── config.py           # System settings & configuration
├── main.py             # Main entry point for live video stream
├── requirements.txt    # Python dependencies
├── yolov8n.pt          # YOLOv8 nano pre-trained model weights
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- **Python**: 3.9 or higher
- **Webcam**: System camera or external USB webcam

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ganesh-gouli/VisionMind-AI.git
   cd VisionMind-AI
   ```

2. **Create and Activate Virtual Environment**:
   - **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎯 Usage

Run the main application:

```bash
python main.py
```

### Controls:
- Press **`q`** while focusing on the video window to safely exit the application.

---

## ⚙️ Configuration

System parameters can be adjusted in [`config.py`](file:///d:/OLD%20projects/jarvis_vision/config.py):

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `YOLO_MODEL_PATH` | `"yolov8n.pt"` | Path to YOLO model weights |
| `CONFIDENCE_THRESHOLD` | `0.3` | Minimum confidence score for detection |
| `TRACKER_MAX_DISAPPEARED` | `50` | Frames before tracked object is forgotten |
| `TTS_RATE` | `170` | Speech speed for TTS output |
| `TTS_VOLUME` | `1.0` | Audio volume (0.0 to 1.0) |
| `DEBUG` | `True` | Enable console debug output |

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

Developed by **[Ganesh Gouli](https://github.com/Ganesh-gouli)**.
