import requests
import bs4
import sys


def fetch_news(opfile):
    url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-IN&gl=IN&ceid=IN:en"
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    o = open(opfile, "a")
    cclass = ['QmrVtf', 'RD0gLb', 'kybdz']

    for tag in soup.find_all('h3', {"class": "ipQwMb ekueJc RD0gLb"}):
        o.write(tag.parent['data-n-cvid'])
        o.writelines(tag.contents[0].text)
        o.write("\n")
        for c in tag.parent.contents:
            if(c['class'] == cclass):
                o.write(c.contents[0].contents[2].text)
                o.write(" ")
                o.write(c.contents[0].contents[3].text)
                o.write("\n")

    o.close()


opfile = sys.argv[1]
fetch_news(opfile)
