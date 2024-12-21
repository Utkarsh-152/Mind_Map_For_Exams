from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import requests
import markdown
from utils import get_gemini_response

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY is not set!")
else:
    print("GOOGLE_API_KEY loaded successfully:", api_key)

app = Flask(__name__)

# API route to generate mind map
@app.route('/api/generate', methods=['POST'])
def api_generate_mind_map():
    data = request.json
    standard = data.get('standard')
    subject = data.get('subject')
    chapter = data.get('chapter')

    if not standard or not subject or not chapter:
        return jsonify({"error": "Please provide Standard, Subject, and Chapter."}), 400

    try:
        mind_map = get_gemini_response(standard, subject, chapter)
        return jsonify({"mind_map": mind_map})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Web route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Web route to handle form submission and generate mind map
@app.route('/generate-mind-map', methods=['POST'])
def web_generate_mind_map():
    # Retrieve form data
    standard = request.form.get('standard')
    subject = request.form.get('subject')
    chapter = request.form.get('chapter')

    # Simulate an API call to the same app for generating the mind map
    response = requests.post(request.url_root + 'api/generate', json={
        'standard': standard,
        'subject': subject,
        'chapter': chapter
    })

    if response.status_code == 200:
        mind_map = response.json().get('mind_map')
        # Convert the mind map to HTML from Markdown
        mind_map_html = markdown.markdown(mind_map)
        return render_template('result.html', mind_map=mind_map_html)
    else:
        error = response.json().get('error', 'An error occurred')
        return render_template('result.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
