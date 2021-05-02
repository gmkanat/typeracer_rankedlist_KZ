from bs4 import BeautifulSoup
import requests
import time


for i in range(1, 32000, 2000):
    print(i, i + 2000)

html = requests.get(f'http://typeracerdata.com/leaders?min_races=500&min_texts=1&sort=wpm_textbests&rank_start=1&rank_end=5000')

soup = BeautifulSoup(html.text, 'lxml')
file = open("data.txt", "a",  encoding = "utf-8")
cnt = 1
links = soup.find_all('a')
for link in links:
    if "username" in link['href']:
        # print(link['href'])
        page = requests.get(f'http://typeracerdata.com/{link["href"]}')
        soup1 = BeautifulSoup(page.text, 'lxml')
        title = soup1.get_text()
        # print(cnt)
        # print(soup1)   
        print(cnt)
        cnt += 1 
        if "Kazakhstan" in title:
            trs = soup1.find_all('tr')   
            tr = trs[1].find('td')
            print(tr.get_text())
            file.write(f'http://typeracerdata.com/{link["href"]}---->{tr.get_text()}\n')
file.close()
time.sleep(864000)


