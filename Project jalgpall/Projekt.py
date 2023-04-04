# programm võtab internetist FC Hii umaa valitud hooaja andmed, koondab need kokku ja väljastab
#lõpuks ekraanile saadud info.

#impordimae vajalikud moodulid
from bs4 import BeautifulSoup
from easygui import *
import requests
import pandas as pd
import numpy as np


#Eeldame, et inimene sisestab FC Hiiumaa jalgpall.ee vastava tiimi hooaja (v.a 2022) kokkuvõtva lehekülje
#Näiteks https://jalgpall.ee/voistlused/2/team/587?season=2021
#url = input('Sisestage Fc Hiiumaa hooaja lehekülje URL: ')
url = 'https://jalgpall.ee/voistlused/2/team/587?season=2021'

#avame lehekülje kust lugeda tahame.
html_text = requests.get(url)
html = html_text.text
soup = BeautifulSoup(html, 'html.parser')

aastad_netist = soup.find_all('div', class_ = 'input')
aastakesed = []
aastad = []
for aasta in aastad_netist:
    aastakesed.append(aasta.text.replace('\n', ''))
K = 4
for x in range(0, len(aastakesed[1]), K):
    aastad.append(aastakesed[1][x : x + K])




"""
#Otsime üles kõik hooajal peetud mängud
tulemused_netist = soup.find_all('a', class_ = 'result')
tulemused = []
for tulemus in tulemused_netist:
    tulemus = tulemus.text.replace(' ', '')
    tulemused.append(tulemus)

#Otsime tiimi mis asus vasakul pool
vasak_tiim_netist = soup.find_all('td', class_ = 'team left',)
vasakul_olev_tiim = []
for tiim in vasak_tiim_netist:
    tiim = tiim.text.replace('\n', '')
    vasakul_olev_tiim.append(tiim)

#Otsime tiimi mis asus paremal pool
parem_tiim_netist = soup.find_all('td', class_ = 'team right',)
paremal_olev_tiim = []
for tiim in parem_tiim_netist:
    tiim = tiim.text.replace('\n', '')
    paremal_olev_tiim.append(tiim)


"""

#leiame mis mängijad mitu mängu hooajal mängisid
def mängude_arv(mängud_netist):
    tbody = mängud_netist.find_all('tbody')[2]
    mängud_td = tbody.find_all('td')
    mängijate_listike = []
    mängude_list = []
    mängijate_list = []
    for mängud in mängud_td:
        mängijate_listike.append(mängud.text.replace('\n', ''))
    mängude_list.append(mängijate_listike[4::5])
    mängijate_list.append(mängijate_listike[1::5])
    mängijate_mängud = {'Mängijad' : mängijate_list[0], 'Mängude arv':mängude_list[0]}
    return mängijate_mängud

df_mängud = pd.DataFrame(mängude_arv(soup))

#a = gspread.service_account('')
#sh = sa.open('jalgpall')

#Teeme listi, kus on kirjas kõik väravate lööjad
def väravad(väravad_soup):
    tbody = väravad_soup.find_all('tbody')[3]
    väravad_td = tbody.find_all('td')
    väravate_listike = []
    väravate_kogus = []
    väravalööjate_nimed = []
    for värav in väravad_td:
        väravate_listike.append(värav.text.replace('\n', ''))
    väravate_kogus.append(väravate_listike[4::5])
    väravalööjate_nimed.append(väravate_listike[1::5])
    väravalööjate_list = dict(zip(väravalööjate_nimed[0], väravate_kogus[0]))
    return (väravalööjate_list)


#leiame mitu kollast kaarti keegi sai
def minutid(minutid_soup):
    tbody = minutid_soup.find_all('tbody')[5]
    minutid_td = tbody.find_all('td')
    minutite_listike = []
    minutite_list = []
    mängijate_nimed = []
    for minut in minutid_td:
        minutite_listike.append(minut.text.replace('\n', ''))
    minutite_list.append(minutite_listike[4::5])
    mängijate_nimed.append(minutite_listike[1::5])
    minutite_dict  = dict(zip(mängijate_nimed[0], minutite_list[0]))
    return minutite_dict


#leiame mitu minutit keegi mängis
def kollased_kaardid(kaardid_soup):
    tbody = kaardid_soup.find_all('tbody')[6]
    kollased_kaardid_td = tbody.find_all('td')
    kollaste_kaartide_listike = []
    kollaste_kaartide_list = []
    mängijate_nimed = []
    for kaart in kollased_kaardid_td:
        kollaste_kaartide_listike.append(kaart.text.replace('\n', ''))
    kollaste_kaartide_list.append(kollaste_kaartide_listike[4::5])
    mängijate_nimed.append(kollaste_kaartide_listike[1::5])
    kaartide_dict = dict(zip(mängijate_nimed[0], kollaste_kaartide_list[0]))
    return kaartide_dict



#leiame, mitu punast kaarti keegi sai
def punased_kaardid(kaardid_soup):
    tbody = kaardid_soup.find_all('tbody')[7]
    punased_kaardid_td = tbody.find_all('td')
    punaste_kaartide_listike = []
    punaste_kaartide_list = []
    mängijate_nimed = []
    for kaart in punased_kaardid_td:
        punaste_kaartide_listike.append(kaart.text.replace('\n', ''))
    punaste_kaartide_list.append(punaste_kaartide_listike[4::5])
    mängijate_nimed.append(punaste_kaartide_listike[1::5])
    punaste_kaartide_dict = dict(zip(mängijate_nimed[0], punaste_kaartide_list[0]))
    return punaste_kaartide_dict


"""

def info_faili(mängijad, mängud):
    fail = open("andmed.txt", 'a')
    for mängija in mängijad:
        fail.write(mängija +'\n')
    for rida in fail:
        fail.write(mängud + '\n')
    fail.close


info_faili(mängijate_list_lõplik, mängude_list)
"""
"""
#Otsime, mis aasta kohta infot otsida
aasta_arv_netist = soup.find_all('div', class_ = 'input')
aastad = []
for aasta in aasta_arv_netist:
    aasta = aasta.text.replace('\n', '')
    aastad.append(aasta)
string = aastad[1]
n = 4
hooajad = [string[i:i+n] for i in range(0, len(string), n)]
hooaeg = url[-4: ]

# leiame mitu väravat on kumbki tiim lõõnud   
def vasaku_tiimi_väravad(väravad):
    vasak = []
    for i in väravad:
        vasak.append(i[0])
    return vasak

def parema_tiimi_väravad(väravad):
    parem = []
    for i in väravad:
        parem.append(i[2])
    return parem

vasakul_oleva_tiimi_tulemus = vasaku_tiimi_väravad(tulemused)
paremal_oleva_tiimi_tulemus = parema_tiimi_väravad(tulemused)


#liidame kokku hooajal teeniutud punktid
def punktid(vasak_tiim, parem_tiim, vasak_tulemus, parem_tulemus):
    punktide_arv = 0
    a = 0
    kodus_teenitud_punktid = 0
    vöörsil_teenitud_punktid = 0
    for võistkond in vasak_tiim:
        if vasak_tiim[a] == 'FC Hiiumaa' and vasak_tulemus[a] > parem_tulemus[a]:
            punktide_arv += 3
            kodus_teenitud_punktid += 3
        elif vasak_tiim[a] == 'FC Hiiumaa' and vasak_tulemus[a] == parem_tulemus[a]:
            punktide_arv += 1
            kodus_teenitud_punktid += 1
        elif parem_tiim[a] == 'FC Hiiumaa' and vasak_tulemus[a] == parem_tulemus[a]:
            punktide_arv += 1
            vöörsil_teenitud_punktid += 1
        elif parem_tiim[a] == 'FC Hiiumaa' and vasak_tulemus[a] < parem_tulemus[a]:
            punktide_arv += 3
            vöörsil_teenitud_punktid += 3
        a += 1
    return(punktide_arv, kodus_teenitud_punktid, vöörsil_teenitud_punktid)
(p, k, v) = punktid(vasakul_olev_tiim, paremal_olev_tiim, vasakul_oleva_tiimi_tulemus, paremal_oleva_tiimi_tulemus)

#Väljastame info ekraanile.
msgbox('FC hiiumaa teenis '+ hooaeg + '. aastal '+ str(p) + '. punkti' + '\n' + 'Neist ' + str(k) + ' punkti teeniti kodus ja ' + str(v) + ' teeniti vöörsil. ' + '\n')

msgbox('Fc Hiiumaa eest mängisid:' + ', '.join(mängijate_list_lõplik) )
"""