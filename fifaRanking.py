from bs4 import BeautifulSoup
import requests
import lxml

website = 'https://www.sportingnews.com/ar/futbol/news/campeon-mundial-qatar-2022-apuestas-ranking-fifa/vzgwsfhlgse4omfuv8ocjdtd'
result = requests.get(website, 'lxml')
content = result.text

soup = BeautifulSoup(content, features='lxml')

box = soup.find('tbody')
with open(f'fifaRanking.txt', 'w') as file:
    for team in box:
        td = team.findAll('td')
        n = td[0].get_text()
        name = td[1].get_text()
        score = td[2].get_text()
        text = f'{n},{name},{score} \n'
        file.write(text)
        print(n,name,score)



