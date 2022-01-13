import requests
from bs4 import BeautifulSoup
import random

def wikiscraperecommendations(count, URL):
    
    count -= 1
    if count == 0:
        print("")
        print("Would you like 5 more recommendations?")
        clientinput = input("Type yes for more or anything else to quit: ")
        if clientinput == "yes":
            wikiscraperecommendations(7, URL)
        return

    response = requests.get(URL)

    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find(id="firstHeading")
    if title.text == "Main Page":
        print ("")
    else:
        print(title.text)

    links = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    newlink = 0

    for link in links:
		    if link['href'].find("/wiki/") == -1: 
		        continue

		    newlink = link
		    break

    URL = "https://en.wikipedia.org" + newlink['href']
    wikiscraperecommendations(count, URL)


if __name__ == "__main__":
    URL = "https://en.wikipedia.org/wiki/Main_Page"
    print("Here are 5 recommendations of good wikipedia articles: ")
    wikiscraperecommendations(7, URL)
