import requests
from bs4 import BeautifulSoup

# Data acquisition
for i in range(1, 1000000, 100):
    step = i - 1
    URL = "https://hammurabi.itam.mx/F/DRJCJUM67Q8FYXA4V36E749U7DUSGA1NJ84F6T2A6YG51MH9TX-34832?func=short-jump&jump=000001"
    page = requests.get(URL)
    results = BeautifulSoup(page.content, "html.parser")
    # Remove the break if you need to go over all the pages
    break

# So the structure is the following: 
# The code is injected to plain javascript using PHP, then Jquery create the tables (<tr>s) and thats why if you search for tbody with class 'contenedor_tabla' 
# it would appear empty since it is injected after the page is loaded, the following is an example of how to extract the information contained in js
soup = results
data = soup.findAll("script")
relevant = []
for script in data:
    if len(script.contents) != 0:
        js = script.contents[0].strip();
        starts = js.startswith('var autor = ')
        if starts:
            relevant.append(js)
