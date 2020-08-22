# BY this code you check covid-19 cases in india
import requests
from bs4 import BeautifulSoup
Url="https://www.worldometers.info/coronavirus/country/India/"
req=requests.get(Url)
bsObj=BeautifulSoup(req.text,"html.parser")
data = bsObj.find_all("div",class_="maincounter-number")
print("INdia 27 July COVID-19 Cases live update")
print("total cases",data[0].text.strip())
print("total Deaths",data[1].text.strip())
print("total Recovered",data[2].text.strip())
