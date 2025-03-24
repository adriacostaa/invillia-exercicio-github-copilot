"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = { 
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Atividades Esportivas
    "Futebol": {
        "description": "Treinos de futebol",
        "schedule": "Segundas e Quartas, 15:00 - 17:00",
        "max_participants": 30,
        "participants": []
        },
    "Volei": {
        "description": "Treinos de volei",
        "schedule": "Terças e Quintas, 15:00 - 17:00",
        "max_participants": 30,
        "participants": []
        },
        # Atividades Culturais
    "Teatro": {
        "description": "Aulas de teatro",
        "schedule": "Terças e Quintas, 14:00 - 16:00",
        "max_participants": 20,
        "participants": []
        },
    "Dança": {
        "description": "Aulas de dança",
        "schedule": "Segundas e Quartas, 14:00 - 16:00",
        "max_participants": 20,
        "participants": []
    },
    # Atividades Intelectuais
    "Debate": {
        "description": "Aulas de debate",
        "schedule": "Quartas, 14:00 - 16:00",
        "max_participants": 20,
        "participants": []
        },
    "Clube do Livro": {
        "description": "Clube do livro",
        "schedule": "Sextas, 14:00 - 16:00",
        "max_participants": 20,
        "participants": []  
        }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

    #Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

