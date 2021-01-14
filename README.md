# Soleil : le pire ennemi des réseaux sociaux ?

Par Maya Safa, Fanny Billet, Quentin Vautier

--- arborescence du dossier ---

- data/ dossier d'analyse des resultats 
- main/ dossier de scrpaing 
- render/ dossier pour le stockage des resultats du scraping 

------------------------------------------------------------

# Scrapping_reddit_weather
***
#Notre objectif est de développer un script pour corréler la visibilité des publications sur le réseau social Reddit avec les données météo du jour.

### Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)

## General Info
***
Notre objectif est de développer un script pour corréler la visibilité des publications sur le réseau social Reddit avec les données météo du jour.
Pour cela nous avons choisi de nous intéresser au Subreddit français: Mercredi Tech, un rendez-vous hebdomadaire
Nous avons récupéré les données de 13 stations différentes météos situées sur des aérodromes ou des aéroports,pour nous synonyme de fiabilité

Paris https://www.wunderground.com/calendar/fr/paris/LFPO
Marseille https://www.wunderground.com/calendar/fr/marseille/LFML
Lyon https://www.wunderground.com/calendar/fr/lyon/LFLL
Toulouse https://www.wunderground.com/calendar/fr/toulouse/LFBO
Cannes https://www.wunderground.com/calendar/fr/mandelieu-la-napoule/LFMD
Strasbourg https://www.wunderground.com/calendar/fr/strasbourg/LFST
Montpellier https://www.wunderground.com/calendar/fr/mauguio/LFMT
La rochelle https://www.wunderground.com/calendar/fr/la-rochelle/LFBH
Lille https://www.wunderground.com/calendar/fr/brebieres/LFQQ
Nantes https://www.wunderground.com/calendar/fr/bouguenais/LFRS
Metz/Nancy https://www.wunderground.com/calendar/fr/liehon/LFJL
Luxembourg https://www.wunderground.com/calendar/fr/kuntzig/ELLX
Caen https://www.wunderground.com/calendar/fr/lassay-les-chateaux/LFRK


------------------------------------------------------------

### Technologies
Liste des technologies utilisées pour le scrapping
* [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Version 4.9.2. 
* [Selenium](https://www.selenium.dev/documentation/fr/): Version 3.141.59

#### Installation sur ubuntu
***
 Beautifulsoup sur ubuntu
 ``` pip install beautifulsoup4``` ou ```pip3 install beautifulsoup4```
Selenium sur ubuntu 
``` pip install beautifulsoup4

# 1 | S C R A P I N G 

## 1 - 1 R E D D I T

reddit_scrap_fanny_maya_quentin.py

## 1 - 2 W U N D E R G R O U N D 

weather.py

# 2 | P R E P A R A T I O N - D E S - D O N N E E S 

data_clean.py

# 3 | A N A L Y S E 

data_analyse.ipynb
