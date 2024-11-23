import time
import random
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import datetime
import traceback

def format_timestamp_to_str(timestamp: datetime.timedelta): # copypaste from a different project
    seconds = int(timestamp.total_seconds())
    minutes = int(seconds/60)
    hours = int(minutes/60)
    days = int(hours/24)
    weeks = int(days/7)

    seconds_new = int(int(seconds) - int(minutes*60))
    minutes_new = int(int(minutes) - int(hours*60))
    hours_new = int(int(hours) - int(days*24))
    days_new = int(int(days) - int(weeks*7))

    if seconds > 60:
        if minutes > 60:
            if hours > 24:
                if days > 7: response = f"{weeks} Weeks, {days_new} days, {hours_new} hours"
                else: response = f"{days} Days, {hours_new} hours"
            else: response = f"{hours} Hours, {minutes_new} minutes"
        else: response = f"{minutes} Minutes, {seconds_new} seconds"
    else: response = f"{seconds} Seconds"

    return response

def do_race(driver: uc.Chrome):
    found = False
    while not found:
        try:
            source_div = driver.find_element(By.CSS_SELECTOR, ".dash-copy")
            target_input = driver.find_element(By.CSS_SELECTOR, ".dash-copy-input")
            found = True
        except:
            pass

    time.sleep(5)

    try:
        text = source_div.text

        for char in text:
            if random.randint(1, 17) == 4 and char != " ":
                target_input.send_keys(random.choice("abcdefghijklmnopqrstuvwxyz")) # screwing up every so often just bcuz :3
                time.sleep(0.1)

            target_input.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15))
        time.sleep(random.randint(7, 13))
        target_input.send_keys(Keys.ENTER)
    except Exception as e:
        traceback.print_exception(e)

start = datetime.datetime.now()

driver = uc.Chrome()
driver.get("https://nitrotype.com/")

races = 0

while True:
    do_race(driver)
    races += 1
    os.system(f"title \"Races done: {races} | Running for: {format_timestamp_to_str(datetime.datetime.now() - start)}\"")
