import csv
import re
from bs4 import BeautifulSoup
import requests

url = "https://afltables.com/afl/stats/2024.html#"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

tbody = soup.tbody
table_rows = tbody.contents

player_numbers = []

for row in table_rows:
    player_numbers.append(row.find(string=re.compile("[0-5][0-9]")))

names = soup.find_all(string=re.compile("[a-zA-Z], [a-zA-Z]"))[:-1]

names_list = []

for name in names:
    names_list.append(name)

games_played = []

for i in range(0, 39):
    games_played.append(table_rows[i].find_all(string=re.compile("[0-9]|[0-5][0-9]"))[1])

with open('2024 Adelaide AFL Players Results.csv', 'w') as csvf:
    writer = csv.writer(csvf, dialect='excel', quoting=csv.QUOTE_MINIMAL)
    i = 0
    writer.writerow(['Player #,' + 'Player Name,' + 'Games Played'])
    for i in range(0, 39):
        writer.writerow([player_numbers[i],  names_list[i],  games_played[i]])
        i += 1

