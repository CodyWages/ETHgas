# Import web scraping tools
import requests
import bs4

# Get url data
url = requests.get("https://www.coinmarketcap.com")

# Convert to lxml
soup = bs4.BeautifulSoup(url.text,"lxml")

# Store element data
gas_var = soup.select("div>span>a")

# Print current gwei
print(f'Gas is Currently {gas_var[5].getText()}')
