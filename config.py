from dotenv import load_dotenv
import os

load_dotenv()  # loads the .env file

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
BASE_URL = os.getenv('BASE_URL')