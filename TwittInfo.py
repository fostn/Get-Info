import requests 
print(
""""
╭━┳━╭━╭━╮╮
┃┈┈┈┣▅╋▅┫┃
┃┈┃┈╰━╰━━━━━━╮
╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉
╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤
╲┃┈┈┈┈╭━┳━━━━╯
╲┣━━━━━━┫ Twitter Info By fostn

Insta : @f09l 
Twitt : @lwv5
Telegram Channel : @ifostn
"""""
	)

def info():
	username = input("Enter Username : ").replace('@' ,'')
	url = (f'https://tufaah.osc-fr1.scalingo.io/twitter/?user={username}')
	data = requests.get(url).json()
	date = data['date']
	name = data['name']
	id = data['id']
	followers = data['followers']
	following = data['following']
	img = data['image']
	print("Username : " + username)
	print("name : " + str(name))
	print("ID : " + str(id))
	print("followers : " + str(followers))
	print("following : " + str(following))
	print("Date created : " + str(date))
	print("Img Url : " + str(img))
	print("\nFor more tools, follow me ! ")

info()


