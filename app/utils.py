
import google.generativeai as genai
import os

# Initialize the model
def initialize_genai():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    return genai.GenerativeModel("gemini-1.5-flash")

model = initialize_genai()

def get_gemini_response(standard, subject, chapter):
    prompt = f"""
    Create a detailed mind map for the subject **"{subject}"** for **Standard "{standard}"**. The mind map should focus on the chapter **"{chapter}"**. The output should be in a structured Markdown format with the following elements:

- **Key Concepts**: Identify and list the main ideas or topics in the chapter.
- **Sub-Topics**: Break down the key concepts into more specific sub-topics or sections.
- **Summary**: Provide a concise summary of the chapter, highlighting the main points and objectives.
- **Relationships**: Clearly describe the connections between the key concepts, sub-topics, and how they relate to each other. Use bullet points to express these relationships.

The Markdown format should include:
- **Headings**:
    - Use `##` for **Key Concepts**.
    - Use `###` for **Sub-topics** under each key concept.
    - Use `####` for detailed points or explanations under each sub-topic.
  
- **Bullet Points**:
    - Under each section, list relevant details, key terms, or concepts using bullet points.
    - For relationships, use arrows or connections to show how one concept or sub-topic links to another (e.g., `Key Concept A -> Sub-Topic B`).

The goal is to create a clear and structured visual representation of the chapter’s content, focusing on both the details and their interrelationships.

    """
    response = model.generate_content([prompt])
    return response.text
