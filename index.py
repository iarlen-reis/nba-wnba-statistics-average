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

      player = {'name': player_name, 'stats': stats}

      self.players.append(player)
      
  def get_player_name(self, soup):
     title = soup.find('h1').text

     return title
    
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
  'https://www.rotowire.com/wnba/player/aja-wilson-481',
]

player = WebScraping(urls)

scrape = player.scrape_and_parse()

data = player.convert_to_json()

print(data)