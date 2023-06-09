# Welcome to Rezi!
#     ____             _ 
#    / __ \___  ____  (_)
#   / /_/ / _ \/_  / / / 
#  / _, _/  __/ / /_/ /  
# /_/ |_|\___/ /___/_/   
# Rezi was written in Python 3.8.10 on VSCode.
# Please visit the github at https://github.com/Wamy-Dev/ReziWebsite
# ==================================================================
# This is an modified version of Rezi that only does the scraper bit
# Completly removing the webserver from it so it can be read from a
# Machine
# ==================================================================

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from datetime import datetime
import requests
import meilisearch
from decouple import config
import requests
import os
import time
import json

# Input file
file = requests.get("https://raw.githubusercontent.com/Wamy-Dev/ReziWebsite/main/input.json")
with open("input.json", "w") as json_file:
	json.dump(file.json(), json_file, indent=4)

# All the scrapers available
from scraper.spiders.abandonware import AbandonwareSpider
from scraper.spiders.archive import ArchiveSpider
from scraper.spiders.fitgirlrepacks import FitgirlSpider
from scraper.spiders.gamesdrive import GamesdriveSpider
from scraper.spiders.gog import GogSpider
from scraper.spiders.madloader import MadloaderSpider
from scraper.spiders.nopaystation import NoPayStationSpider
from scraper.spiders.ovagames import OvaGamesSpider
from scraper.spiders.pokemonrom import PokemonromSpider
from scraper.spiders.scooterrepacks import ScooterRepacksSpider
from scraper.spiders.steamrip import SteamripSpider
from scraper.spiders.threedsroms import ThreeDSRomsSpider
from scraper.spiders.xcinsp import XciNspSpider
from scraper.spiders.playablearchive import ArchivePlayableSpider

# Scraper part. Scrapes everything from these sources
# and puts to an file called rezi.csv
if os.path.exists("rezi.csv"):
  os.remove("rezi.csv")
else:
  print("First run initiated.")
crawler = CrawlerProcess(get_project_settings())
crawler.crawl(AbandonwareSpider) # https://myabandonware.com
crawler.crawl(ArchiveSpider) # https://archive.org
crawler.crawl(FitgirlSpider) # https://fitgirl-repacks.site
crawler.crawl(GamesdriveSpider) # https://gamesdrive.net
crawler.crawl(GogSpider) # https://gog-games.com
crawler.crawl(MadloaderSpider) # https://madloader.com
crawler.crawl(NoPayStationSpider) # https://nopaystation.com
crawler.crawl(OvaGamesSpider) # https://ovagames.com
crawler.crawl(PokemonromSpider) # https://pokemonrom.net
crawler.crawl(ScooterRepacksSpider) # https://scooter-repacks.site
crawler.crawl(SteamripSpider) # https://steamrip.com
crawler.crawl(ThreeDSRomsSpider) # https://3dsroms.com
crawler.crawl(XciNspSpider) # https://xcinsp.com
crawler.crawl(ArchivePlayableSpider) # https://archive.org

# Starts this shit
crawler.start()