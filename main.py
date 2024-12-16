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
    counter += 1

    print(f"~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~")
    while not found:
        groups = pwFindContent.find_group(pw)
        counter += 1

        if groups:
            EmailSender.send(parse_groups(groups))
            found = True
        else:
            print(f"Running for the course - {course_acronym}: {counter}", end='\r')
            sleep(time_sleep)