import requests

#Store website in variable
website = requests.get("https://www.coinmarketcap.com")

import bs4

#Store web data
soup = bs4.BeautifulSoup(website.text,"lxml")

#Store element data
gas_var = soup.select("div>span>a")

#Print current gwei
print(f'Gas is Currently {gas_var[5].getText()}')
