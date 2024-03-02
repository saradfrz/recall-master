from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Accessing the variables
SECRET_KEY = os.getenv("SECRET_KEY")
