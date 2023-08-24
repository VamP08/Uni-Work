import random
from datetime import datetime, timedelta

random_int_1 = random.randrange(0, 6)

random_int_2 = random.randrange(5, 10)

random_int_3 = random.randrange(0, 11, 3)

def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

random_date_result = random_date(start_date, end_date)

print("Random Integer between 0 and 5:", random_int_1)
print("Random Integer between 5 and 9:", random_int_2)
print("Random Integer between 0 and 10 with step 3:", random_int_3)
print("Random Date between {} and {}: {}".format(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), random_date_result.strftime("%Y-%m-%d")))
