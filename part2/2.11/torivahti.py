import time
from urllib.request import urlopen, Request
import os
import sys

atk = 'https://www.tori.fi/uusimaa/tietokoneet_ja_lisalaitteet?'

def hae_sivu_ja_tallenna(url):
    tiedosto = "data.txt"
    if os.path.isfile(tiedosto): os.remove(tiedosto)
    hashurl = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(hashurl).read()
    response = str(response)
    with open(tiedosto, "w") as tiedosto:
        tiedosto.write(response)

def hae_kaikki():
    file = open("data.txt", "r")
    response = file.read()
    alku = 'class="li-title'
    loppu = 'list_price ineuros'
    result = []
    a = 0
    while a < len(response):
        a = response.find(alku, a)
        b = response.find(loppu,a)
        if a == -1:
            return result
        else:
            result.append(response[a+15:b+30])
            a += 1
    return result

def tulosta(lista, maara):
    korvattavat =[ ['"', ' '], [r'\xe4', "ä"],[r'xc4','Ä'], [r'\xf6', 'ö'], [r'\xe5', 'ö'], [r'&quot;', '"'], [r'&',''],[r'/p',''],
    [r'<',''],[r'div',''],[r'\t',''],[r'\n',''],[r'>',''],[r'/',''],[r';',''],[r'\xd6','Ö'],[r'\xe9', 'é'],
    [r'class= list-details-container',''],[r'p class= list_price ineuros',''],[r'p class= param',''],[r'\'\'',' tuumaa'],[r'   ','  ']]
    for i in lista[:maara]:
        for n in korvattavat:
            i = i.replace(n[0], n[1])
        print(i)

# support for run with arguments
try:
    maara = sys.argv[1]
    taajuus = sys.argv[2]
except IndexError as error:
    print("Kuinka monta tulosta näytetään: ", end="")
    maara = input()
    print("Kuinka usein tulokset päivitetään (sek): ", end="")
    taajuus = input()

while True:
    
    maara = int(maara)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("ATK:\n")
    hae_sivu_ja_tallenna(atk)
    lista = hae_kaikki()
    tulosta(lista, maara)
    print("-"*10+"\n")
    time.sleep(int(taajuus))

