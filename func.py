import os
import requests
from bs4 import BeautifulSoup

found = 0


def makeDir(dir):
  if not os.path.exists(dir):
    os.mkdir(dir)


def downloadGames(ID, url, rootPath):
  txt = requests.get(url).text
  soup = BeautifulSoup(txt, 'html.parser')
  for item in soup.find_all('img'):
    if 'Place-420x230-' in str(item):
      imghash = item['src'].split("Place-420x230-", 1)[1]
      imghash = imghash.split(".Png")[0]
      final = "Hash Found: " + imghash
      print(final)
      dwnurl = 'https://contentstore.roblox.com/v1/content?hash=' + imghash
      # Thank you Lanausse for the downloader!
      response = requests.get(dwnurl)
      filePath = rootPath + "/" + imghash
      open(filePath + ".rbxl", 'wb').write(response.content)
      finalmsg = "Downloaded: " + imghash + ".rblx"
      print(finalmsg)
      found = 1
  if found == 0:
    print('Failed to find hash')
