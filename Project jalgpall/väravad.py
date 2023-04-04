# programm võtab internetist FC Hii umaa valitud hooaja andmed, koondab need kokku ja väljastab
#lõpuks ekraanile saadud info.

#impordime vajalikud moodulid
from bs4 import BeautifulSoup
from easygui import *
import requests


url = 'https://jalgpall.ee/voistlused/2/team/587?season=2021'

#avame lehekülje kust lugeda tahame.
html_text = requests.get(url)
html = html_text.text
soup = BeautifulSoup(html, 'lxml')



tbody = soup.find_all('tbody')[3]
all_html = tbody.contents
all_td = tbody.find_all('td')
väravate_listike = []
väravate_list = []
mängijate_list = []
for värav in all_td:
    väravate_listike.append(värav.text)
väravate_list.append(väravate_listike[4::5])
mängijate_list.append(väravate_listike[1::5])


print(mängijate_list)

