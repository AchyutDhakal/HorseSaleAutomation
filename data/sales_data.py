from datetime import datetime, timedelta
import time

future_date = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')

SALES_DATA = [
    {
        "event_name":f"Random_{int(time.time())}",
        "date":future_date,
        "max_lot":"30",
        "max_stables":"20",
        "entry_fee":"100"
    }
]
