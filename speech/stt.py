import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_command(timeout=5, phrase_time_limit=5):
    """
    Listens to microphone and returns recognized text (lowercase).
    Returns None if nothing is detected.
    """
    try:
        with sr.Microphone() as source:
            print("🎤 Listening for command...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = recognizer.recognize_google(audio)
            return text.lower()
    except sr.WaitTimeoutError:
        return None
    except Exception as e:
        print("STT error:", e)
        return None
