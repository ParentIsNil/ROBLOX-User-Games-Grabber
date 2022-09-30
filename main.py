import requests
from func import downloadGames

UserID = input("Enter User ID (users account must be older than 2008): ")
url = ''.join([
  "http://web.archive.org/web/200710im_/http://www.roblox.com/User.aspx?id=",
  UserID
])
req = requests.get(url)

if req.status_code == 200:
  print("Found Account")
  downloadGames(UserID, url)
else:
  code = "".join(["Failed: ", UserID, " Error Code: ", str(req.status_code)])
  print(code)
