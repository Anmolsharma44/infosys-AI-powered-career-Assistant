import streamlit as st
import sys
import os

# Proper path resolution for local VS Code structure
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

from src.resume_parser.extract_text import extract_text_from_file
from src.resume_parser.parse_resume import parse_with_gemini
from src.db import save_candidate

st.set_page_config(page_title="AI Internship Assistant", layout="centered")

st.title("🚀 AI-Powered Internship & Career Assistant")
st.subheader("Milestone 1: Smart Resume Parser (OCR + Gemini + SQLite)")

api_key = st.text_input("Enter your Gemini API Key", type="password")
uploaded_file = st.file_uploader("Upload your Resume (PDF, PNG, JPG, JPEG)", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file and api_key:
    with st.spinner("Extracting text and parsing with AI (OCR enabled)..."):
        file_bytes = uploaded_file.read()
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        extracted_text = extract_text_from_file(file_bytes, file_extension)
        
        if not extracted_text.strip():
            st.error("Could not extract any text from the uploaded file.")
        else:
            st.info(f"Successfully extracted {len(extracted_text)} characters.")
            
            try:
                data = parse_with_gemini(extracted_text, api_key)
                st.success("Resume successfully parsed by Gemini AI!")
                st.json(data)
                
                save_candidate(data)
                st.success("Profile successfully saved to SQLite database (`candidate_database.db`)!")
                
            except Exception as e:
                st.error(f"An error occurred during parsing or saving: {e}")
else:
    st.info("Please enter your API key and upload a resume to get started.")