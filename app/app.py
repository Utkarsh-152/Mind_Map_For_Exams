from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from utils import get_gemini_response

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_mind_map():
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

if __name__ == '__main__':
    app.run(debug=True) 