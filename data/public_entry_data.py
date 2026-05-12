from config import EMAIL_ADDRESS
import time
from datetime import datetime, timedelta

today = datetime.today().strftime('%Y-%m-%d')
future_date = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
past_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')


split_email = EMAIL_ADDRESS.split('@')
split_email.insert(1,f"+{int(time.time())}@")
email_address = "".join(split_email)


VALID_PUBLIC_PORTAL = [
    {
        "email_address":email_address,
        "mobile_number":9875487896,
        "firstName":"Random",
        "lastName":"Person",
        "address.addressLine1":"kathmandu, Nepal",
        "address.townCity":"Kathmandu",
        "address.postcode":257489,
        "equinePremisesNumber":25466335,
        "horses[0].horse.horseName":f"Random Horse_{int(time.time())}",
        "horses[0].horse.registrationNumber":369874512369,
        "horses[0].horse.performance.additionalPerformanceDetails":"Est exercitation aliqua eiusmod adipisicing cillum sunt ipsum proident fugiat laboris qui. Fugiat quis veniam aliqua officia aliqua qui do laborum Lorem.",
        "horses[0].horse.dateOfBirth": past_date,
        "Select year":2025,
        "horses[0].horse.performance.sjiPointsWon":5,
        "horses[0].horse.performance.eventingIrelandPoints":3,
        "horses[0].horse.performance.huntedWith":"Donald Trump",
        "horses[0].horse.performance.huntedHowManyOccasions":6,
        "horses[0].horse.performance.huntedHowManySeasons":5
    }
]