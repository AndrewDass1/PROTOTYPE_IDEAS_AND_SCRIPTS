#!/usr/bin/env python3
import datetime, time
import give_a_date_and_time

inserted_year = give_a_date_and_time.dt_values()[0]
inserted_month = give_a_date_and_time.dt_values()[1]
inserted_day = give_a_date_and_time.dt_values()[2]
inserted_hour = give_a_date_and_time.dt_values()[3]
inserted_minute = give_a_date_and_time.dt_values()[4]
inserted_second = give_a_date_and_time.dt_values()[5]
inserted_time = datetime.datetime(inserted_year, inserted_month, inserted_day, inserted_hour, inserted_minute, inserted_second)

def timer():
    while True:
        if datetime.datetime.now() > inserted_time:
            break
        else:
            print("Time is still going...")
            print(time.sleep(5))
            print(timer())

    print("Program Finished")

print(timer())
