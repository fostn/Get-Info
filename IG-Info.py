import requests
print(
"""
╭━┳━╭━╭━╮╮
┃┈┈┈┣▅╋▅┫┃
┃┈┃┈╰━╰━━━━━━╮
╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉
╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤
╲┃┈┈┈┈╭━┳━━━━╯
╲┣━━━━━━┫ Insta Info By Fostn

Insta : f09l 
Twitt : lwv5
Telegram Channel : @ifostn
"""
	)

username = input("Enter Username : ")
url = (f'https://h-a-m-o.herokuapp.com/hamo/instagram/info/?user={username}')
request = requests.get(url).json()
Name = request['name']
Id = request['id']
Followers = request['followers']
Following = request['following']
Posts = request['posts']
Date = request['data']
print("Name : " + Name)
print("Id : " + Id)
print("Followers : " + Followers)
print("Following : " + Following)
print("Posts : " + Posts)
print("Date created : " + Date)
