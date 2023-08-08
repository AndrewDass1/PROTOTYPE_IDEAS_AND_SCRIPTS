#!/usr/bin/env python3
def dt_values():
    def the_year():
        while True:
            try:
                insert_year = int(input("Enter the year: "))

                if insert_year >= 0:
                    break
            except ValueError:
                print(the_year())

        return insert_year

    def the_month():
        while True:
            try:
                insert_month = int(input("Enter the month: "))

                if insert_month >= 1 and insert_month <= 12:
                    break
            except ValueError:
                print(the_month())

        return insert_month

    def the_day():
        while True:
            try:
                insert_day = int(input("Enter the day: "))

                if insert_day >= 1 and insert_day <= 31:
                    break
            except ValueError:
                print(the_day())

        return insert_day

    def the_hour():
        while True:
            try:
                insert_hour = int(input("Enter the hour: "))

                if insert_hour >= 0 and insert_hour <= 23:
                    break
            except ValueError:
                print(the_hour())

        return insert_hour

    def the_minute():
        while True:
            try:
                insert_minute = int(input("Enter the minute: "))

                if insert_minute >= 0 and insert_minute <= 59:
                    break
            except ValueError:
                print(the_minute())

        return insert_minute

    def the_seconds():
        while True:
            try:
                insert_seconds = int(input("Enter the amount of seconds: "))

                if insert_seconds >= 0 and insert_seconds <= 59:
                    break
            except ValueError:
                print(the_seconds())

        return insert_seconds

    return the_year(), the_month(), the_day(), the_hour(), the_minute(), the_seconds()

dt_values()
