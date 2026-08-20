import cv2

def draw_bbox(frame, bbox, label="", conf=None, color=(0, 255, 0)):
    """
    Draw a bounding box with optional label and confidence on the frame.

    Args:
        frame (numpy.ndarray): Image frame
        bbox (tuple): (x1, y1, x2, y2)
        label (str): Object label
        conf (float): Confidence score (0-1)
        color (tuple): RGB color for the box
    """
    x1, y1, x2, y2 = bbox
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
    
    if label:
        text = f"{label}"
        if conf is not None:
            text += f" {conf*100:.1f}%"
        cv2.putText(frame, text, (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)


def limit_frame_size(frame, width=800):
    """
    Resize the frame to a maximum width while keeping aspect ratio.

    Args:
        frame (numpy.ndarray): Original frame
        width (int): Maximum width

    Returns:
        numpy.ndarray: Resized frame
    """
    h, w = frame.shape[:2]
    if w > width:
        ratio = width / w
        frame = cv2.resize(frame, (width, int(h * ratio)))
    return frame
