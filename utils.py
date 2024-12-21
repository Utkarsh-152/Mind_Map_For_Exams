# prompt/utils.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  

# Initialize the model
def initialize_genai():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

model = initialize_genai()

def get_gemini_response(standard, subject, chapter):
    prompt = f"""
    Create a detailed mind map for the subject "{subject}" for Standard "{standard}".
    Focus on the chapter "{chapter}". The Summary and Short notes should include:
    - Key concepts
    - Sub-topics
    - Short Notes
    - Formulas, Important Points to remember for Exams
    - Summary 
    - Provide the output in a structured Markdown format with:
    - Headings (## for main concepts, ### for sub-topics)
    - Bullet points for relationships and details
    """
    response = model.generate_content([prompt])
    return response.text
