import os

from bs4 import BeautifulSoup

import EnvVarReader

class_url = EnvVarReader.class_url

def find_group(pw):
    # create browser instance
    browser = pw.chromium.launch(headless=True)
    # create context
    # using context we can define page properties like viewport dimensions
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto(class_url)

    if page.is_visible("text=Préférences en matière de témoins"):
        page.click("text=Autoriser les témoins")

    page.click("text=Horaire - Hiver 2025")
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")
    cours = soup.find_all("div", {"role": "tabpanel", "class": "active"})
    child_list = []
    for i in cours:
        groupes = i.findAll("div", class_="groupe")
        for j in groupes:
            no_groupe = j.find("h3", class_="no_groupe").text
            nb_places = j.find("span", class_="places").text
            if nb_places.strip() != "Aucune place disponible":
                print(no_groupe.strip() + " : " + nb_places.strip())
                child_list.append(no_groupe.strip() + " : " + nb_places.strip())

    browser.close()
    return child_list