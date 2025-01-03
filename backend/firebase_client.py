from firebase_admin import credentials, firestore, initialize_app, get_app, exceptions
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Firebase setup
def initialize_firebase():
    try:
        # Check if the default app is already initialized
        app = get_app()
    except exceptions.FirebaseError:
        # Initialize if no app exists
        cred_path = os.getenv("FIREBASE_CREDENTIALS", "D:/Projects/Talent_Scout/talentscout-7a28f-firebase-adminsdk-8rxh1-296f2e213d.json")
        cred = credentials.Certificate(cred_path)
        app = initialize_app(cred)
    return firestore.client()

# Firestore client
db = initialize_firebase()
