import streamlit as st
import requests
from models.groq_client import initialize_groq_client, generate_response
from services.candidate_info import collect_candidate_info, display_candidate_info
from services.question_generator import generate_questions

BACKEND_URL = "http://127.0.0.1:8000"

def register_user():
    st.subheader("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        response = requests.post(f"{BACKEND_URL}/register", json={
            "name": name,
            "email": email,
            "password": password
        })
        if response.status_code == 201:
            st.success("Registration successful! You can now log in.")
        else:
            st.error(response.json().get("detail", "Registration failed"))

def login_user():
    st.subheader("Log In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        response = requests.post(f"{BACKEND_URL}/login", json={
            "email": email,
            "password": password
        })
        if response.status_code == 200:
            user = response.json()["user"]
            st.session_state.user_logged_in = True
            st.session_state.user = user
            st.success(f"Welcome back, {user['name']}!")
        else:
            st.error(response.json().get("detail", "Login failed"))

def main():
    st.set_page_config(page_title="TalentScout Hiring Assistant", layout="wide")

    # Check session state for user authentication
    if "user_logged_in" not in st.session_state:
        st.session_state.user_logged_in = False
        st.session_state.user = None

    if not st.session_state.user_logged_in:
        st.title("Welcome to TalentScout!")
        st.subheader("Your AI-Powered Hiring Assistant")
        st.write("Log in or register to get started.")

        auth_option = st.radio("Choose an option", ["Log In", "Register"])
        if auth_option == "Register":
            register_user()
        else:
            login_user()
    else:
        st.title("TalentScout Hiring Assistant")
        st.write(f"Welcome back, {st.session_state.user['name']}! Let's get started.")

        # Initialize Groq client
        client = initialize_groq_client()

        # Collect candidate information
        candidate_info = collect_candidate_info()
        if candidate_info:
            display_candidate_info(candidate_info)

            # Generate and display technical questions
            st.subheader("Technical Questions")
            if candidate_info['tech_stack'].strip():
                prompt = [
                    {"role": "user", "content": f"Generate technical questions for the following tech stack: {candidate_info['tech_stack']}"}
                ]
                model_name = "llama-3.1-70b-versatile"
                questions = generate_response(prompt, model=model_name)
                st.write(questions)
            else:
                st.write("Please provide a tech stack to generate technical questions.")

        # Logout option
        if st.button("Log Out"):
            st.session_state.user_logged_in = False
            st.session_state.user = None

if __name__ == "__main__":
    main()
