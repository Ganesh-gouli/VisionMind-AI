import wikipedia

# Offline fallback dictionary
FACTS = {
    "person": "A human being, capable of thought and action.",
    "car": "A road vehicle, typically with four wheels, powered by an engine.",
    "bottle": "A container used to hold liquids.",
    "laptop": "A portable computer that can be used anywhere.",
    "dog": "A domesticated animal, often kept as a pet.",
    "cat": "A small domesticated mammal with sharp claws.",
    "bicycle": "A vehicle with two wheels that is powered by pedaling.",
    "chair": "A piece of furniture designed to sit on.",
    "tvmonitor": "A device used to display visual content."
}

def get_object_info(obj_name):
    """
    Fetch a short description of the object.
    Tries Wikipedia first; falls back to offline dictionary.

    Args:
        obj_name (str): Name of the detected object.

    Returns:
        str: Description of the object.
    """
    obj_name = obj_name.lower()

    # Try Wikipedia
    try:
        summary = wikipedia.summary(obj_name, sentences=1)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return FACTS.get(obj_name, f"A {obj_name} is an object around you.")
    except wikipedia.exceptions.PageError:
        return FACTS.get(obj_name, f"A {obj_name} is an object around you.")
    except Exception:
        return FACTS.get(obj_name, f"A {obj_name} is an object around you.")
