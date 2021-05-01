from bs4 import BeautifulSoup
import requests

html = requests.get('http://typeracerdata.com/leaders')

soup = BeautifulSoup(html.text, 'lxml')
file = open("data.txt", "a",  encoding = "utf-8")
cnt = 0
links = soup.find_all('a')
for link in links:
    if "username" in link['href']:
        # print(link['href'])
        page = requests.get(f'http://typeracerdata.com/{link["href"]}')
        soup1 = BeautifulSoup(page.text, 'lxml')
        title = soup1.get_text()
        # print(cnt)
        # print(soup1)    
        if "United States" in title:
            trs = soup1.find_all('tr')   
            tr = trs[1].find('td')
            print(tr.get_text())
            file.write(f'http://typeracerdata.com/{link["href"]}---->{tr.get_text()}\n')
file.close()