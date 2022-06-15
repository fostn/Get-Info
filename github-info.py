import requests
print(
"""
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⠿⠟⠛⠛⠛⠛⠻⠿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣦⠀⠀⠀
⠀⢀⣾⣿⡿⠁⠀⠀⣴⣦⣄⠀⠀⠀⠀⠀⣀⣤⣶⡀⠈⢿⣿⣷⡀⠀
⠀⣾⣿⡟⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⢻⣿⣷⠀
⢠⣿⣿⠁⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠈⣿⣿⡄
⢸⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⡇
⠘⣿⣿⡦⠤⠒⠒⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠧⠤⢴⣿⣿⠃
⠀⢿⣿⣧⡀⠀⢤⡀⠙⠻⠿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⢀⣼⣿⡿⠀
⠀⠈⢿⣿⣷⡀⠈⢿⣦⣤⣾⣿⣿⣿⣿⣿⣷⣄⠀⠀⢀⣾⣿⡿⠁⠀
⠀⠀⠀⠻⣿⣿⣦⣄⡉⣿⣿⢿⣿⠉⢻⣿⢿⣿⣠⣴⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣧⣼⣿⣤⣾⣷⣶⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀
[Get info about any account on Github]
Coded By fostn :
insta @f09l
Twitt @lwv5
telegram Channel @ifostn
"""

)
username = input("Enter Username : ")
url = (f"https://soud.me/api/Github?username={username}")
info = requests.get(url).json()

def github():
	avatar_url = info['info']['avatar_url']
	created = info['info']['created_at']
	bio = info['info']['bio']
	company = info['info']['company']
	email = info['info']['email']
	followers = info['info']['followers']
	following = info['info']['following']
	id = info['info']['id']
	location = info['info']['location']
	name = info['info']['name']
	public_gists = info['info']['public_gists']
	public_repos = info['info']['public_repos']
	twitter_username = info['info']['twitter_username']
	print("_"*42)
	print("Username : "+username)
	print("name : "+str(name))
	print("Date create : "+str(created))
	print("Bio : " + str(bio))
	print("company : "+str(company))
	print("email : " + str(email))
	print("followers : " + str(followers))
	print("following : " + str(followers))
	print("id : " + str(id))
	print("location : " + str(location))
	print("public gists :"+str(public_gists))
	print("public repos :"+str(public_repos))
	print('Twitter acoount : ' + str(twitter_username))
	print("avatar url : "+avatar_url)
	print("_"*42)
	print("For More Tools Follow Me")
github()
