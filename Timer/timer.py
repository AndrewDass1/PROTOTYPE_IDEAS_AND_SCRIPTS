import time

# This script asks for how many days, hours, minutes, and seconds a timer needs to run for

def timer_countdown():
    # Ask for how many days the timer will run for
    how_many_days = int(input("How many days is needed to run the timer: "))
    while how_many_days <= 0:
        print("Invalid response.")
        how_many_days = int(input("How many days is needed to run the timer: "))

    # Ask for how many hours the timer will run for
    how_many_hours = int(input("How many hours is needed to run the timer: "))
    while how_many_hours <= 0 or how_many_hours > 24:
        print("Invalid response.")
        how_many_hours = int(input("How many hours is needed to run the timer: "))

    # Ask for how many minutes the timer will run for
    how_many_minutes = int(input("How many minutes is needed to run the timer: "))
    while how_many_minutes <= 0 or how_many_minutes > 60:
        print("Invalid response.")
        how_many_minutes = int(input("How many minutes is needed to run the timer: "))

    # Ask for how many seconds the timer will run for
    how_many_seconds = int(input("How many seconds is needed to run the timer: "))
    while how_many_seconds <= 0 or how_many_seconds > 60:
        print("Invalid response.")
        hours_to_seconds = int(input("How many seconds is needed to run the timer: "))

    # Convert days, hours and minutes all to seconds
    days_to_seconds = how_many_days * 24 * 60 * 60
    hours_to_seconds = how_many_hours * 60 * 60
    minutes_to_seconds = how_many_minutes * 60

    # Add the given times together in seconds
    total_seconds = days_to_seconds + hours_to_seconds + minutes_to_seconds + how_many_seconds

    total_time = "The timer will run for " + str(how_many_days) + " days, " + str(how_many_hours) + " hours, " + str(how_many_minutes) + " minutes, " + str(how_many_seconds) + " seconds"
    print(total_time)

    countdown = time.sleep(total_seconds)

    timer_finished = "The timer stopped!"

    return countdown, print(timer_finished)

timer_countdown()
