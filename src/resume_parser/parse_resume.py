import json
import google.generativeai as genai

def parse_with_gemini(text, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-4-hydrogen')
    
    prompt = f"""
    You are an expert AI Resume Parser. Analyze the resume text provided below and extract the information strictly into a valid JSON format:
    {{
      "full_name": "Candidate's full name",
      "email": "Email address",
      "phone": "Phone number",
      "skills": ["Skill 1", "Skill 2"],
      "education": [{{"degree": "Degree name", "institution": "College", "year": "Year"}}],
      "projects": [{{"title": "Project title", "description": "Description"}}]
    }}

    Resume Text:
    {text}
    """
    
    response = model.generate_content(prompt)
    cleaned = response.text.replace("```json", "").replace("```", "").strip()
    return json.loads(cleaned)