from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def initialize_groq_client():
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")
    return Groq(api_key=groq_api_key)

def generate_response(prompt, model="llama-3.1-70b-versatile"):
    client = initialize_groq_client()
    try:
        response = client.chat.completions.create(
            messages=prompt,
            model=model
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"

# if __name__ == "__main__":
#     prompt = [{"role": "user", "content": "Explain the basics of Python programming in 50 words."}]
#     model_name = "llama-3.1-70b-versatile"
#     response = generate_response(prompt, model=model_name)
#     print(response)
