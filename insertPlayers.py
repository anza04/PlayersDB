import getPlayer as gp
import dbMgmt as db
from bs4 import BeautifulSoup as bs
import requests

for index in range(1, 116):
    page = requests.get('https://basketball.realgm.com/international/stats/2024/Averages/Qualified/All/player/All/asc/'+str(index))
    soup = bs(page.text, features="html.parser")

    #playerLinksTds = soup.find_all('td', class_='nowrap')

    anchors = [a for a in (td.find('a') for td in soup.findAll('td', class_='nowrap')) if a]

    for x in range(len(anchors)):
        try:
            hrefString = str(anchors.pop(x))
            playerUrl = 'https://basketball.realgm.com/'+hrefString.split('>')[0][9:len(hrefString)]
            playerUrl = playerUrl[:len(playerUrl)-1]
            player = gp.GetPlayer(playerUrl)
            print('Inserendo '+player.Name)
            insQuery = (
            'INSERT INTO `player` (`ID`, `Name`, `Position`, `Birthdate_year`, `Birthdate_month`, `Birthdate_day`, `Birthplace`, `Nationality`, `Height`, `Weight`, `Url`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
            )
            val = (player.Name, player.Position, player.Birthdate_year, player.Birthdate_month, player.Birthdate_day, player.Birthplace, player.Nationality, player.Height, player.Weight, player.Url)
            db.insertPlayer(insQuery, val, player.Url)
        except:
            print('index error, skip')



