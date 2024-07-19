from bs4 import BeautifulSoup as bs
import requests

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class Player:
    Name: str
    Position: str
    Birthdate_year: int
    Birthdate_month: int
    Birthdate_day: int
    Birthplace: str
    Nationality: str
    Height: int
    Weight: int
    Url: str

    def getPlayersNameAndPos(self, soup):
        playerInfoContainer = soup.find('div', class_='half-column-left')
        playerNameString = playerInfoContainer.find('h2')
        self.Name = "".join(playerNameString.find_all(string=True, recursive=False)).strip()
        playerPosition = "".join(playerNameString.find_all(string=True, recursive=True)).removeprefix(self.Name)
        self.Position = playerPosition.strip().split('#')[0].strip()

    def getPlayerInfo(self, soup):
        playerInfoContainer = soup.find('div', class_='half-column-left')
        playerInfo = playerInfoContainer.find_all('p')
        playerInfoArray = [row.text for row in playerInfo]
        birthdate = playerInfoArray[1].split(':')[1].split('(')[0]
        try:
            self.Birthdate_year = birthdate.split(',')[1].strip()
        except:
            self.Birthdate_year = 0
        try:
            self.Birthdate_month = months.index(birthdate[:4].strip()) + 1
        except:
            self.Birthdate_month = 0
        try:
            self.Birthdate_day = birthdate[4:].split(',')[0].strip()
        except:
            self.Birthdate_day = 0
        try:
            self.Birthplace = playerInfoArray[2].split(':')[1].strip()
        except:
            self.Birthplace = ''
        try:
            self.Nationality = playerInfoArray[3].split(':')[1].strip()
        except:
            self.Nationality = ''
        try:
            self.Height = playerInfoArray[4].split('\xa0\xa0\xa0\xa0')[0].split('(')[1].strip().removesuffix(')')
        except:
            self.Height = 0
        try:
            self.Weight = playerInfoArray[4].split('\xa0\xa0\xa0\xa0')[1].split('(')[1].strip().removesuffix(')')
        except:
            self.Weight = 0

    def printInfo(self):
        print('Name: ' + self.Name)
        print('Position: ' + self.Position)
        print(
            'Birthdate: ' + str(self.Birthdate_day) + '/' + str(self.Birthdate_month) + '/' + str(self.Birthdate_year))
        print('Birthplace: ' + self.Birthplace)
        print('Nationality: ' + self.Nationality)
        print('Height: ' + str(self.Height))
        print('Weight: ' + str(self.Weight))


def getSoup(parUrl):
    page = requests.get(parUrl)
    return bs(page.text, features="html.parser")


def GetPlayer(url):
    soup = getSoup(url)
    player = Player()
    Player.Url = url
    player.getPlayersNameAndPos(soup)
    player.getPlayerInfo(soup)
    return player
