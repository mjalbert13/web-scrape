import requests
import pandas
from bs4 import BeautifulSoup

base_url ="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,30,10):
    r = requests.get(base_url+str(page)+".html")
    print(base_url+str(page)+".html")