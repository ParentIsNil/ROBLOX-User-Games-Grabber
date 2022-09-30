import os
import requests
from bs4 import BeautifulSoup


def makeDir(dir):
  if not os.path.exists(dir):
    os.mkdir(dir)


def downloadGames(ID, url):
  found = 0
  gamenames = []
  intofgames = 0
  intofhash = 0
  txt = requests.get(url).text
  soup = BeautifulSoup(txt, 'html.parser')
  apiurl = ''.join(['https://users.roblox.com/v1/users/', ID])
  apiname = requests.get(apiurl)
  userdata = apiname.json()
  rootPath = ''.join([userdata.get('name', ''), "'s Games"])
  makeDir(rootPath)
  for item in soup.find_all('span'):
    if 'PlaceName' in str(item):
      item = str(item)
      gamename = item.split(">", 1)[1]
      gamename = gamename.split("</span>")[0]
      gamenames.insert(intofgames, gamename)
      intofgames = intofgames + 1
  for item in soup.find_all('img'):
    if 'Place-420x230-' in str(item):
      imghash = item['src'].split("Place-420x230-", 1)[1]
      imghash = imghash.split(".Png")[0]
      final = ''.join(["Hash Found: ", imghash])
      print(final)
      dwnurl = ''.join(
        ['https://contentstore.roblox.com/v1/content?hash=', imghash])

      # Thank you Lanausse for the downloader!
      response = requests.get(dwnurl)
      filePath = ''.join([rootPath, "/", gamenames[intofhash]])
      open(''.join([filePath, ".rbxl"]), 'wb').write(response.content)
      finalmsg = ''.join(["Downloaded: ", gamenames[intofhash], ".rblx"])
      print(finalmsg)
      intofhash = intofhash + 1
      found = 1
  if found == 0:
    print('User has no games :(')
