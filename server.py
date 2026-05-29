"""
Flask application for emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def process_input():
    """Process user input and return emotion detection results."""
    user_input = request.args.get("textToAnalyze")
    detector_result = emotion_detector(user_input)
    if detector_result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    output = (
        f"For the given statement, the system response is "
        f"'anger': {detector_result['anger']}, "
        f"'disgust': {detector_result['disgust']}, "
        f"'fear': {detector_result['fear']}, "
        f"'joy': {detector_result['joy']} and "
        f"'sadness': {detector_result['sadness']}. "
        f"The dominant emotion is {detector_result['dominant_emotion']}."
    )
    return output


@app.route("/")
def landing_page():
    """Render the landing page."""
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    