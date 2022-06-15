import requests
print(

Insta : f09l 
Twitt : lwv5
Telegram Channel : @ifostn
"""
	)
User = input("Enter Username : ")
def TikTok():
	Data = requests.get(f'https://tufaah.osc-fr1.scalingo.io/tiktok/?user={User}').json()
	name = Data['name']
	bio = Data['bio']
	followers = Data['followers']
	following = Data['following']
	id = Data['id']
	image = Data['image']
	print("Username : " + str(User))
	print("Name : "+ str(name))
	print("Bio : "+ str(bio))
	print("Followers : "+ str(followers))
	print("Following : "+ str(following))
	print("Id : "+ str(id))
	print("Image Url : "+ str(image))
	print("\nFor more tools, follow me !")
TikTok()
