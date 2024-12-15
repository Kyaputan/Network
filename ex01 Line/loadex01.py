import os
from dotenv import load_dotenv

def load_env_ex01():
    load_dotenv()
    token = os.getenv("token")
    return token



