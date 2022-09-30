import requests
from func import downloadGames, makeDir

UserID = input("Enter User ID (users account must be older than 2008): ")
rootPath = UserID + "'s Games"
makeDir(rootPath)
url = 'http://web.archive.org/web/200710im_/http://www.roblox.com/User.aspx?id=' + UserID
req = requests.get(url)

if req.status_code == 200:
  print("Found Account")
  downloadGames(UserID, url, rootPath)
else:
  code = "Failed: " + UserID + " Error Code: " + str(req.status_code)
  print(code)
