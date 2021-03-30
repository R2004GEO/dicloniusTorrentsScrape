from bs4 import BeautifulSoup
import requests

url = "http://tracker.anime-club.ro/"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'lxml')

tables = soup.find_all("table")
tab1 = tables[0]

body = tab1.find_all("td")
head = body[0]

torrent_list_name = []
torrent_list_link = []

for item in head.find_all("tr"):
    for xi in item.find_all("a", href=True):
        torrent_list_name.append(xi.text)
        torrent_list_link.append(xi['href'])

for i in range(0, len(torrent_list_link)):
    tor = requests.get(torrent_list_link[i])
    print(f'Downloading {torrent_list_name[i]}.torrent...')
    open(f"torrents/{torrent_list_name[i]}.torrent", 'wb').write(tor.content)
