from dotenv import load_dotenv
from pathlib import Path
import os

# using .env file to grab private token
env_path = Path('.') / '..' / '.env'
load_dotenv(dotenv_path = env_path)

TOKEN = os.getenv("TOKEN")
PREFIX = "yeetus"
