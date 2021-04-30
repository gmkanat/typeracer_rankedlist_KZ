from bs4 import BeautifulSoup
import requests

html = requests.get('http://typeracerdata.com/leaders')

soup = BeautifulSoup(html.text, 'lxml')


links = soup.find_all('a')
for link in links:
    if "username" in link['href']:
        print(link['href'])
        page = requests.get(f'http://typeracerdata.com/{link["href"]}')
        soup1 = BeautifulSoup(page.text, 'lxml')
        if "United States" in soup1:
            print(f'http://typeracerdata.com/{link["href"]}')