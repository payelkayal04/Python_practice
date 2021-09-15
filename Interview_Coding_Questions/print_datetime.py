from datetime import datetime
from datetime import date
current_datetime = datetime.now()
current_date = date.today()
current_time = current_date.strftime("%H:%M.%S")
print(current_datetime)
print(current_date)
print(current_time)
