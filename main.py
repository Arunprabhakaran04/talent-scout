import streamlit as st
from models.groq_client import initialize_groq_client, generate_response
from services.candidate_info import collect_candidate_info, display_candidate_info
from services.question_generator import generate_questions

def main():
    client = initialize_groq_client()

    candidate_info = collect_candidate_info()
    if candidate_info:
        display_candidate_info(candidate_info)

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

    exit_keyword = st.text_input("Type 'exit' to end the conversation.")
    if exit_keyword.lower() == 'exit':
        st.write("Thank you for using TalentScout! We'll be in touch about the next steps.")
        st.stop()

if __name__ == "__main__":
    main()
