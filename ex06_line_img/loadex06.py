import os
from dotenv import load_dotenv

def load_env_ex06():
    load_dotenv()
    token = os.getenv("token")
    return token



