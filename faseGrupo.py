from bs4 import BeautifulSoup
import requests

website = 'https://depor.com/mundial-x-depor/tabla-de-posiciones-mundial-qatar-2022-en-vivo-clasificacion-resultados-y-partidos-de-la-fase-de-grupos-de-la-copa-de-la-fifa-noticia/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

box = soup.find_all('tbody')
with open(f'faseDeGrupo.txt', 'w') as file:
    for grupos in box:
        text = ''
        for grupo in grupos:
            line = grupo.findAll('td')
            name = line[0].get_text()
            pj = line[1].get_text()
            pg = line[2].get_text()
            pe = line[3].get_text()
            pp = line[4].get_text()
            dg = line[5].get_text()
            pts = line[6].get_text()
            text = f'{name},{pj},{pg},{pe},{pp},{dg},{pts} \n'
            file.write(text)
            print(text)


