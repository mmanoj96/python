import requests
from bs4 import BeautifulSoup
def news():
    url='https://indianexpress.com/article/world/russia-ukraine-war-live-updates-putin-nato-zelenskyy-biden-lviv-mariupol-kyiv-7838090/'
    resp=requests.get(url)
    if resp.status_code==200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")
   # print(resp.text)
    soup=BeautifulSoup(resp.text,'html.parser')
    l=soup.find("div",{"class":"articles"})
    #print(l)
    for i in l.findAll("p"):
         print(i.text)
    else:
         print("Error")
news()