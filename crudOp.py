from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 1. Define the structure for User Input
class Language(BaseModel):
    name: str

# 2. This is our "Database" (It starts empty!)
languages_db = []

# --- ENDPOINTS ---

@app.get("/")
def home():
    return {"message": "API is running successfully 🚀"}

@app.get("/languages")
def get_all_languages():
    """Returns everything users have added so far"""
    return languages_db

@app.post("/languages")
def add_language(user_input: Language):
    """Takes user input and saves it to our list"""
    
    # Create a dictionary from the input and add a dynamic ID
    new_entry = user_input.dict()
    new_entry["id"] = len(languages_db) + 1
    
    languages_db.append(new_entry)
    
    return {"message": "Language added successfully!", "data": new_entry}

@app.get("/languages/{lang_id}")
def get_one_language(lang_id: int):
    """Finds a specific language by ID"""
    for lang in languages_db:
        if lang["id"] == lang_id:
            return lang
    raise HTTPException(status_code=404, detail="Language not found")