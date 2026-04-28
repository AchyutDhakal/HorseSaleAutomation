from dotenv import load_dotenv
import os
import time

load_dotenv()  # loads the .env file

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
BASE_URL = os.getenv('BASE_URL')

email=os.getenv('EMAIL_ADDRESS')
split_email = email.split('@')
split_email.insert(1,f"+{int(time.time())}@")

EMAIN_ADDRESS="".join(split_email)
EMAIL_PASSWORD=os.getenv('EMAIL_PASSWORD')
CARD_NUMBER = os.getenv('CARD_NUMBER')
EXPIRY_MONTH = os.getenv('EXPIRY_MONTH')
EXPIRY_YEAR = os.getenv('EXPIRY_YEAR')
CVV = os.getenv('CVV')
