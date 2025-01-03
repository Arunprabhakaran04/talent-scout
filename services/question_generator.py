from models.groq_client import initialize_groq_client

def generate_questions(tech_stack, model="llama-3.1-70b-versatile"):
    client = initialize_groq_client()

    prompt = [
        {
            "role": "user",
            "content": (
                "You are an intelligent assistant for a recruitment agency. "
                "Generate 3-5 technical questions based on the following tech stack: \n"
                f"{tech_stack}\n"
                "Questions should assess the candidate's proficiency and be concise."
                "The questions should range from beginner to advanced levels."
                "Generate only the relevant questions and not any further texts."
                "Do not include any additional notes, disclaimers, or explanations. Generate only the question relevant to the tech stack."
            )
        }
    ]

    try:
        response = client.chat.completions.create(
            messages=prompt,
            model=model
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating questions: {str(e)}"
