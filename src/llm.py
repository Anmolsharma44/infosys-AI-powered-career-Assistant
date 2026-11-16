import google.generativeai as genai

def configure_gemini(api_key):
    genai.configure(api_key=api_key)
    # Using your model specification
    return genai.GenerativeModel('gemini-4-hydrogen')