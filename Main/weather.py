from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from random import randint
import time
import pandas as pd
import os
import os.path


### T O  -  D O ###

# 0 - ////////// degres Celsius
# 1 - ////////// recuperer les differents elements de la meteo pour 1 mois
# 2 - ////////// recuperer dans une boucle les 12 mois
# 3 - formater correctement les dates
# 4 - ////////// recuperer 2 ans
# 5 - recuperer plusieurs lieux
# 6 - Fusion des tableau
# 7 - /////////// sauvegarde csv

# fonction pour avoir les 12 mois





# fonction render permet de rendre la page avec l'execusion du javascript.
def render_page(url):
    #PATH = '/home/quentin/Documents/simplon/sunny_fanny_maya_quentin/Drivers/chromedriver'
    driver = webdriver.Firefox()
    driver.get(url)


    time.sleep(randint(0,1))

    # click pour passer en Celsius

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'wuSettings'))
    )
    element.click()

    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="wuSettings-quick"]/div/a[2]')))
    element2.click()

    # rendu de la page avec le js
    time.sleep(randint(4,6))
    render = driver.page_source

    driver.quit()
    return render

# Paris https://www.wunderground.com/calendar/fr/paris/LFPO
# Marseille https://www.wunderground.com/calendar/fr/marseille/LFML
# Lyon https://www.wunderground.com/calendar/fr/lyon/LFLL
# Toulouse https://www.wunderground.com/calendar/fr/toulouse/LFBO
# Cannes https://www.wunderground.com/calendar/fr/mandelieu-la-napoule/LFMD
# Strasbourg https://www.wunderground.com/calendar/fr/strasbourg/LFST
# Montpellier https://www.wunderground.com/calendar/fr/mauguio/LFMT
# La rochelle https://www.wunderground.com/calendar/fr/la-rochelle/LFBH
# Lille https://www.wunderground.com/calendar/fr/brebieres/LFQQ
# Nantes https://www.wunderground.com/calendar/fr/bouguenais/LFRS
# Metz/Nancy https://www.wunderground.com/calendar/fr/liehon/LFJL
# Luxembourg https://www.wunderground.com/calendar/fr/kuntzig/ELLX
# Caen https://www.wunderground.com/calendar/fr/lassay-les-chateaux/LFRK


stations = ['paris/LFPO','marseille/LFML', 'lyon/LFLL', 'toulouse/LFBO', 'mandelieu-la-napoule/LFMD', 'strasbourg/LFST', 'mauguio/LFMT', 'la-rochelle/LFBH', 'brebieres/LFQQ', 'bouguenais/LFRS', 'liehon/LFJL', 'kuntzig/ELLX', 'lassay-les-chateaux/LFRK']
#stations = ['bouguenais/LFRS']

for s in stations:

    current_day = []
    cloud = []
    temp_max = []
    temp_min = []

    for y in range(2019,2021):
        # 12 mois
        for m in range(1,13):
            my_url = "https://www.wunderground.com/calendar/fr/" + str(s) + "/date/"+ str(y) + "-" + str(m)

            render = render_page(my_url)

            soup = BeautifulSoup(render, "html.parser")

            all_day = soup.find_all('li', class_='current-month')

            # time_format = y + '' + m

            for items in all_day:

                # D A Y

                day_item = items.find('div', class_='date').text
                new_day_item = str(y) + '-' + str(m) + '-' + day_item
                current_day.append(new_day_item)

                # C L O U D

                if items.find('div', class_='phrase') != None:
                    cloud_item = items.find('div', class_='phrase').text
                else:
                    cloud_item = "Nan"

                cloud.append(cloud_item)

                # T E M P - M A X

                if items.find('span', class_='hi') != None:
                    temp_max_item = items.find('span', class_='hi').text
                else:
                    temp_max_item = "Nan"

                temp_max.append(temp_max_item)

                # T E M P - M I N

                if items.find('span', class_='low') != None:
                    temp_min_item = items.find('span', class_='low').text
                else:
                    temp_min_item = "Nan"

                temp_min.append(temp_min_item)

    s_data_weather = pd.DataFrame({
        'current_day': current_day,
        'cloud': cloud,
        'temp_max': temp_max,
        'temp_min': temp_min
    })

    outdir = '../render'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    s = s.replace("/", "_")
    s = s.replace("-", "_")
    file_name = f"{s}_data_weather"

    fullname = os.path.join(outdir, f"{file_name}.csv")

    s_data_weather.to_csv(fullname)
