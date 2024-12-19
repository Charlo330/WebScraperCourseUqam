from time import sleep

from playwright.sync_api import sync_playwright
import EmailSender
import EnvVarReader
import pwFindContent

time_sleep = EnvVarReader.time_sleep
course_acronym = EnvVarReader.course_acronym

def parse_groups(groups_list):
    group_string = ""
    for i in groups_list:
        group_string += i + "\n"

    return group_string

with (sync_playwright() as pw):
    found = False
    counter = 0
    error_counter = 0

    print(f"~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~")
    while not found:
        try:
            groups = pwFindContent.find_group(pw)
            error_counter = 0
        except:
            error_counter += 1
            print(f"Error: {error_counter}", end='\r')
        counter += 1

        if groups:
            EmailSender.send_group(parse_groups(groups))
            found = True
        elif error_counter > 3:
            EmailSender.send_error("An error occurred, the bot will stop.")
            found = True
        else:
            print(f"Running for the course - {course_acronym}: {counter}", end='\r')
            sleep(time_sleep)