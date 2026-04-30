from dotenv import load_dotenv
import os
import time

load_dotenv()  # loads the .env file

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
BASE_URL = os.getenv('BASE_URL')


EMAIL_ADDRESS=os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD=os.getenv('EMAIL_PASSWORD')
CARD_NUMBER = os.getenv('CARD_NUMBER')
EXPIRY_MONTH = os.getenv('EXPIRY_MONTH')
EXPIRY_YEAR = os.getenv('EXPIRY_YEAR')
CVV = os.getenv('CVV')
