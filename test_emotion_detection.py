
"""Unit tests for the EmotionDetection package."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test emotion detection results."""

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        print("PASS: Joy test")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        print("PASS: Anger test")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        print("PASS: Disgust test")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        print("PASS: Sadness test")

    def test_fear(self):
        result = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(result['dominant_emotion'], 'fear')
        print("PASS: Fear test")


if __name__ == '__main__':
    unittest.main()
