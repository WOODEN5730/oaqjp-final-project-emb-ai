
from EmotionDetection.emotion_detection import emotion_detector

tests = [
    "I am very happy today!",
    "I am extremely sad.",
    "I am afraid of the situation.",
    "I am angry about this."
]

for text in tests:
    print("\nInput:", text)

    try:
        result = emotion_detector(text)
        print("Result:", result)
    except Exception as error:
        print("Error:", error)
