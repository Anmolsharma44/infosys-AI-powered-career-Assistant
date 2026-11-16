import sqlite3
import json
import os

DB_NAME = "candidate_database.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT, 
            email TEXT, 
            phone TEXT, 
            skills TEXT, 
            education TEXT, 
            projects TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_candidate(data):
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO candidates (full_name, email, phone, skills, education, projects) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data.get('full_name'), 
        data.get('email'), 
        data.get('phone'), 
        json.dumps(data.get('skills')), 
        json.dumps(data.get('education')), 
        json.dumps(data.get('projects'))
    ))
    conn.commit()
    conn.close()