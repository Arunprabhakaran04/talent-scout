from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from firebase_client import db 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# FastAPI app
app = FastAPI()

# Models
class User(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

@app.post("/register")
async def register_user(user: User):
    users_ref = db.collection("users")
    if users_ref.document(user.email).get().exists:
        raise HTTPException(status_code=400, detail="User already exists")
    users_ref.document(user.email).set(user.dict())
    return {"message": "User registered successfully"}

@app.post("/login")
async def login_user(login: Login):
    users_ref = db.collection("users")
    user = users_ref.document(login.email).get()
    if not user.exists or user.to_dict()["password"] != login.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    user_data = user.to_dict()
    return {"message": "Login successful", "user": {"name": user_data["name"], "email": login.email}}
