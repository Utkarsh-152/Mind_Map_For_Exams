
import google.generativeai as genai
import os

# Initialize the model
def initialize_genai():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    return genai.GenerativeModel("gemini-1.5-flash")

model = initialize_genai()

def get_gemini_response(standard, subject, chapter):
    prompt = f"""
    Create a detailed mind map for the subject "{subject}" for Standard "{standard}".
    Focus on the chapter "{chapter}". The mind map should include:
    - Key concepts
    - Sub-topics
    - Relationships between them
    Provide the output in a structured Markdown format with:
    - Headings (## for main concepts, ### for sub-topics)
    - Bullet points for relationships and details
    """
    response = model.generate_content([prompt])
    return response.text
