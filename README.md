# Soleil : le pire ennemi des réseaux sociaux ?

Par Maya Safa, Fanny Billet, Quentin Vautier

--- arborescence du dossier ---

- data/ dossier d'analyse des resultats 
- main/ dossier de scrpaing 
- render/ dossier pour le stockage des resultats du scraping 

------------------------------------------------------------

# Scrapping_reddit_weather
***
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

>Paris https://www.wunderground.com/calendar/fr/paris/LFPO  

>Marseille https://www.wunderground.com/calendar/fr/marseille/LFML  

>Lyon https://www.wunderground.com/calendar/fr/lyon/LFLL  

>Toulouse https://www.wunderground.com/calendar/fr/toulouse/LFBO  

>Cannes https://www.wunderground.com/calendar/fr/mandelieu-la-napoule/LFMD  

>Strasbourg https://www.wunderground.com/calendar/fr/strasbourg/LFST  

>Montpellier https://www.wunderground.com/calendar/fr/mauguio/LFMT  

>La rochelle https://www.wunderground.com/calendar/fr/la-rochelle/LFBH  

>Lille https://www.wunderground.com/calendar/fr/brebieres/LFQQ  

>Nantes https://www.wunderground.com/calendar/fr/bouguenais/LFRS  

>Metz/Nancy https://www.wunderground.com/calendar/fr/liehon/LFJL  

>Luxembourg https://www.wunderground.com/calendar/fr/kuntzig/ELLX  

>Caen https://www.wunderground.com/calendar/fr/lassay-les-chateaux/LFRK  


### Technologies
>Liste des technologies utilisées pour le scrapping
* [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Version 4.9.2. 
* [Selenium](https://www.selenium.dev/documentation/fr/): Version 3.141.59

#### Installation sur ubuntu
***
> Beautifulsoup sur ubuntu
 ``` pip install beautifulsoup4``` ou ```pip3 install beautifulsoup4```  
 
> Selenium sur ubuntu 
```pip install selenium```  ou ```pip3 install selenium```  

> Driver configuration(Chrome, Firefox) : lien https://github.com/SeleniumHQ/selenium 

-----------------------------------------------------------------------------

# 1 | S C R A P I N G 

## 1 - 1 R E D D I T

reddit_scrap_fanny_maya_quentin.py

## S U J E T : "Mercredi Tech"

Le script récupère tous les sujets sur toutes les pages (4 pages) utilisation du old.reddit au lieu du reddit actuel car c'est + facile à scrape

## S U B R E D D I T : r/jeuxvideo

 les infos ne sont pas à la même place que quand on fait une recherche par mot clé, donc il y a des choses à modifier dans le code

les données scarpé sont :

- La date
- Commentaires
- Les scores
- Les titres

## S U B R E D D I T : r/france

Pour r/france, les infos ne sont pas à la même place que quand on fait une recherche par mot clé, donc il y a des choses à modifier dans le code

Nous avons récupéré 950 articles pour r/jeuxvideo et 938 pour f/france, il doit possiblement y avoir une limite d'article visibles. Ceux pour r/france datent tous de 2021

## S U J E T : not working

## sujet : "ordi"

Pour le sujet "ordi" dans r/france, le même code arrive à récupérer les infos ( date, titre, nombre de points et commentaires), mais quand il clique sur suivant pour la dernière page, il n'y a apparemment plus de sujets et il y a comme texte 'apparemment il n'y a rien ici". Cela fait une IndexError car il n'y a plus de bouton prev/next, juste le texte cité. (8 pages

## sujet : "paris"

Pour le sujet "paris" dans r/france:

premier problème : à la 6eme page, ça fait une AttributeError: 'NoneType' object has no attribute 'a' (pour la fonction pour récupérer les titres) J'ai donc mis la fonction nb_titre en commentaire pour essayer d'executer sans les titres et voir si il arrive à récup les autres infos sur toutes les pages

deuxieme problème : on voit que ça s'arrête à la page 10 et qu'il n'y a plus de bouton "next", alors que le dernier sujet date d'à peine 1 mois. Les gens n'ont pas commencé à parler de Paris dans r/france qu'à partir d'il y a un mois, on suppose donc que quand on fait une recherche de mot clé, c'est limité à 10 pages max.

*** T O - D O ***

Trouver les solutions pour les sujets "ordis" et "paris" afin de renforcer l'efficacité du code et palier à + de problèmes possibles
Continuer à optimiser le code commencé pour r/france
Essayer de voir si on peut contourner la limite du nombre d'articles et de pages
Essayer de scraper le reddit actuel pour voir les différences avec old.reddit
(Faire des scripts universels qui fonctionnent pour toutes les pages)
rendre le code + sécurisé (pour éviter le ban) et + rapide à execute

## 1 - 2 W U N D E R G R O U N D 

weather.py

data_clean.py

## Le fichier weather :

Il permet de scraper les stations météo contenues dans une liste.

L’exécution du script ne supprimer pas les scraps précédent.

Le résultat du scraping sous le format csv et dans le dossier render.



## Les données scarpé sont :

le jour de l’année

la tendance de la météo de ce jour (nuageux, pluvieux ...)

Température max et température min 



## Clean weather :

Le script permet la fusion automatique des données de touts les fichiers du dossier rendez.

l’attribution est score global pour la météo en France

le résultat est exporté en csv dans le dossier data 


*** T O - D O ***

Parallélisation du scraping sur les différentes stations météo 

Scrape de la météo heure par heure du leve au couche du soleil dans le but d'avoir une analyse géographique précise.

Scraper les données des fichiers JSON 


# 2 | A N A L Y S E 

data_analyse.ipynb

Piste à explorer pour avoir une analyse plus pertinente

- Impact des saisons sur la consultation de contenues en ligne.

- Quel paramètre météorologique est en corrélation avec les sorties des utilisateurs

- L'utilisation des réseaux sociaux sur mobile et chez soi et à l'extérieur

