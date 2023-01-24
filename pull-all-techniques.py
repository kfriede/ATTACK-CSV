import requests
from bs4 import BeautifulSoup

res = requests.get('https://attack.mitre.org/techniques/enterprise/')

soup = BeautifulSoup(res.content, "html.parser")

file = open("mitre_listing.csv", "w")

file.write("id,description\n")

soup_sidenav = soup.find_all("div", class_="sidenav-head")
for item in soup_sidenav:
    header = item.find('a')['href'].split("/")
    description = item.text.strip()
    
    if header[1] == "tactics" and header[2].startswith("T"):
        file.write(header[2] + "," + description + "\n")
    elif header[1] == "techniques" and header[2].startswith("T"):
        id = header[2]

        if header[3] != "":
            id += "." + header[3]
        
        file.write(id + "," + description + "\n")

file.close()