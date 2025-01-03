import streamlit as st

def collect_candidate_info():
    with st.form("candidate_info_form"):
        st.header("Candidate Information")
        full_name = st.text_input("Full Name", max_chars=50)
        email = st.text_input("Email Address", max_chars=50)
        phone = st.text_input("Phone Number", max_chars=15)
        experience = st.slider("Years of Experience", 0, 40, 0)
        position = st.text_input("Desired Position(s)", max_chars=50)
        location = st.text_input("Current Location", max_chars=50)
        tech_stack = st.text_area("Tech Stack", placeholder="e.g., Python, Django, React, PostgreSQL", height=100)

        submitted = st.form_submit_button("Submit")
        if submitted:
            return {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "experience": experience,
                "position": position,
                "location": location,
                "tech_stack": tech_stack,
            }
        return None

def display_candidate_info(candidate_info):
    st.subheader("Submitted Information")
    st.write(f"**Name:** {candidate_info['full_name']}")
    st.write(f"**Email:** {candidate_info['email']}")
    st.write(f"**Phone:** {candidate_info['phone']}")
    st.write(f"**Experience:** {candidate_info['experience']} years")
    st.write(f"**Desired Position:** {candidate_info['position']}")
    st.write(f"**Location:** {candidate_info['location']}")
    st.write(f"**Tech Stack:** {candidate_info['tech_stack']}")
