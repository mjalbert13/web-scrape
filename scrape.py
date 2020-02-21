import requests
import pandas
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c,"html.parser")

divs = soup.find_all("div",{"class":"propertyRow"})

price = divs[0].find("h4",{"class":"propPrice"}).text.replace("\n",'').replace(" ","")

houseData= []

for item in divs:
    d={}
    d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n",'').replace(" ","")
    d["Street"]=item.find_all("span", {"class":"propAddressCollapse"})[0].text
    d["Address"]=item.find_all("span", {"class":"propAddressCollapse"})[1].text
    try:
        d["Bedrooms"]=item.find("span",{"class":"infoBed"}).find("b").text
    except:
        d["Bedrooms"]=None

    try:
        d["SqFt"]=item.find("span",{"class":"infoSqFt"}).find("b").text
    except:
        d["SqFt"]=None

    try:
        d["Full Bathrooms"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
    except:
        d["Full Bathrooms"]=None

    try:
        d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
    except:
        d["Half Baths"]=None

    for column_group in item.find_all("div",{"class":"columnGroup"}):
        for feature ,name in zip(column_group.find_all("span",{"class":"featureGroup"}), column_group.find_all("span",{"class":"featureName"})):
            if "Lot Size" in feature.text:
                d["Lot Size"]= name.text
    
    houseData.append(d)

df = pandas.DataFrame(houseData)
df.to_csv("Output.csv")
    
    
