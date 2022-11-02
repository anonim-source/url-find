import requests
import re
from colorama import Fore

from pyfiglet import Figlet
f = Figlet(font='slant')
print(Fore.LIGHTYELLOW_EX+f.renderText('Url-Find'))

try:
    print(Fore.RED+"https://websiteadı.com gibi girin")
    link = input(Fore.GREEN+"Url girin :")
    r = requests.get(link)
    if r.status_code == 200:
        icerik = r.text
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,icerik)
        for i in url:
            print(Fore.LIGHTCYAN_EX+"[+]",i)      

    else:
        print("hatalı")
except:
    print("Hata")
