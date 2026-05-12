from datetime import datetime, timedelta
import time


today = datetime.today().strftime('%Y-%m-%d')
future_date = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
past_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')







