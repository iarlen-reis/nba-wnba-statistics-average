from bs4 import BeautifulSoup
import requests
import json

class WebScraping:
  def __init__(self, urls):
    self.urls = urls
    self.players = []

  def scrape_and_parse(self):
    for url in self.urls:
      response = requests.get(url)

      soup = BeautifulSoup(response.text, 'html.parser')
      
      player_name = self.get_player_name(soup)
      stats = self.get_player_statistics(soup)
      team = self.get_player_team(soup)
      age = self.get_player_age(soup)
      position = self.get_player_position(soup)
      league = self.get_player_league(soup)
      height = self.get_player_height(soup)
      weight = self.get_player_weight(soup)

      player = {
        'information': {
          'name': player_name,
          'age': age,
          'height': height,
          'weight': weight,
          'position': position,
          'team': team,
          'league': league,
        },
        'current_average': stats,
      }

      self.players.append(player)

  def get_player_age(self, soup):
    player_info = soup.find('div', {'class': 'p-card__player-info'}).find_all('div')

    age = player_info[0].text[0:2]

    return age
      
  def get_player_name(self, soup):
     title = soup.find('h1').text

     return title

  def get_player_height(self, soup):
    player_info = soup.find('div', {'class': 'p-card__meta-data has-height-restricted'}).find_all('div')

    height = player_info[0].find('b').text

    return height

  def get_player_weight(self, soup):
    player_info = soup.find('div', {'class': 'p-card__meta-data has-height-restricted'}).find_all('div')

    weight = player_info[1].find('b').text

    return weight

  def get_player_position(self, soup):
    player_info = soup.find('div', {'class': 'p-card__player-info'}).find_all('div')

    position = player_info[0].find('span', {'class': 'hide-until-xl'}).text

    return position

  def get_player_league(self, soup):
    player_info = soup.find('div', {'class': 'p-card__player-info'}).find_all('div')

    league = player_info[1].find('span', {'class': 'p-card__level'}).text

    return league

  def get_player_team(self, soup):
    player_info = soup.find('div', {'class': 'p-card__player-info'}).find_all('div')

    team = player_info[1].find('a').text

    return team

  def get_player_statistics(self, soup):
      statistics_average = soup.find_all('div', {'class': 'p-card__stat'})

      stats = []

      for stat in range(5):
          stat_name = statistics_average[stat].find('div', {'class': 'p-card__stat-name'}).text
          stat_value = statistics_average[stat].find('div', {'class': 'p-card__stat-value'}).text

          stats.append({'name': stat_name, 'value': stat_value})

      return stats


  def convert_to_json(self):
    return json.dumps(self.players, indent=4)



# Adicione as urls de jogadores que deseja scrapear aqui
urls = [
  'https://www.rotowire.com/basketball/player/nikola-jokic-3612',
]

player = WebScraping(urls)

scrape = player.scrape_and_parse()

data = player.convert_to_json()

print(data)