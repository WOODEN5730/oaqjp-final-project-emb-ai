
"""Flask server for the Emotion Detection application."""

from flask import Flask, request, jsonify,render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """Process text and return emotion detection results."""

    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"error": "Please provide text to analyze."}), 400

    response = emotion_detector(text_to_analyze)

    return jsonify(response)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
