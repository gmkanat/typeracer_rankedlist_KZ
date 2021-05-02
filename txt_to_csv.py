import csv


a = []
with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        k = line.find('>')
        t = line.find('=')
        l = line.find('---->')
        wp = line.find('wpm')
        wpm = float(line[k+1:wp])
        handle = line[t+1:l]
        url = 'https://data.typeracer.com/pit/profile?user=' + handle
        a.append([handle, wpm, url])
# print(a)
a.sort(key=lambda x:x[1])
a.reverse()
with open('rank.csv', 'w', newline='') as csvfile:
        fieldnames = ['Handle', 'WPM', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in a:
            writer.writerow({'Handle': i[0], 'WPM': i[1], 'link': i[2]})