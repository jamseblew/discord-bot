from dotenv import load_dotenv
from pathlib import Path
import os

ROOT_PATH = Path(os.path.dirname(__file__)) / '..'

# using .env file to grab private token
env_path = ROOT_PATH / '.env'
load_dotenv(dotenv_path = env_path)

TOKEN = os.getenv("TOKEN")

OBJECTIVES = ["implement ricardo bot", "take over Kaizo", "money"]
PREFIX = "yeetus "
