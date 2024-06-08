import datetime

current_date = datetime.datetime.today().date()
print(f"current date is: {current_date}")

current_time = datetime.datetime.today().time()
print(f"current time is: {current_time}")

current_datetime = datetime.datetime.today()
print(f"current datetime is: {current_datetime}")

datetime_format = datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
print(f"current datetime_format is: {datetime_format}")

