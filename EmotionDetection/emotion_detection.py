
from transformers import pipeline  # type: ignore[import-not-found]

# Load the emotion classification model
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)


def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores."""

    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    predictions = emotion_classifier(text_to_analyze)[0]

    scores = {
        item["label"]: item["score"]
        for item in predictions
    }

    emotions = ["anger", "disgust", "fear", "joy", "sadness"]

    result = {
        emotion: scores.get(emotion, 0.0)
        for emotion in emotions
    }

    result["dominant_emotion"] = max(
        result,
        key=result.get
    )

    return result
