import pyttsx3
import threading
from queue import Queue

engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

# Queue to hold all speech commands
tts_queue = Queue()

def tts_worker():
    while True:
        text = tts_queue.get()
        if text is None:  # Stop signal
            break
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("TTS error:", e)
        tts_queue.task_done()

# Start TTS worker thread
threading.Thread(target=tts_worker, daemon=True).start()

def speak(text):
    """
    Put text into queue to be spoken.
    """
    tts_queue.put(text)
