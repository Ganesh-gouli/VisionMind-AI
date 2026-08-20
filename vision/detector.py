import cv2
from ultralytics import YOLO

class ObjectDetector:
    """
    ObjectDetector uses YOLOv8 for real-time object detection.
    """

    def __init__(self, model_path="yolov8n.pt", conf_threshold=0.35):
        """
        Args:
            model_path (str): Path to YOLOv8 model weights.
            conf_threshold (float): Minimum confidence for detection.
        """
        self.model = YOLO(model_path)  # Automatically downloads if not present
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        """
        Detect objects in a single frame.

        Args:
            frame (numpy.ndarray): Image frame from webcam or video.

        Returns:
            List of tuples: [(label, (x1, y1, x2, y2), confidence), ...]
        """
        results = self.model(frame, verbose=False)[0]
        detections = []

        if results.boxes is not None and len(results.boxes) > 0:
            for box in results.boxes:
                conf = float(box.conf[0])
                if conf < self.conf_threshold:
                    continue
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                detections.append((label, (x1, y1, x2, y2), conf))

        return detections
