from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_mind_map', methods=['POST'])
def generate_mind_map():
    standard = request.form.get('standard')
    subject = request.form.get('subject')
    chapter = request.form.get('chapter')

    response = requests.post('http://127.0.0.1:5000/generate', json={
        'standard': standard,
        'subject': subject,
        'chapter': chapter
    })

    if response.status_code == 200:
        mind_map = response.json().get('mind_map')
        return render_template('result.html', mind_map=mind_map)
    else:
        error = response.json().get('error', 'An error occurred')
        return render_template('result.html', error=error)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
