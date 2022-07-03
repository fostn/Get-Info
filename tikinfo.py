import requests
print(
"""
 ______   __     __  __     __     __   __     ______   ______    
/\__  _\ /\ \   /\ \/ /    /\ \   /\ "-.\ \   /\  ___\ /\  __ \   
\/_/\ \/ \ \ \  \ \  _"-.  \ \ \  \ \ \-.  \  \ \  __\ \ \ \/\ \  
   \ \_\  \ \_\  \ \_\ \_\  \ \_\  \ \_\\"\_\  \ \_\    \ \_____\ 
    \/_/   \/_/   \/_/\/_/   \/_/   \/_/ \/_/   \/_/     \/_____/ 
    -------------------------------------------------------------
    Insta : f09l    Twitt : lwv5      Telegram Channel : @ifostn
    -------------------------------------------------------------
"""
	)
User = input("Enter Username : ")
def TikTok():
	Data = requests.get(f'https://0ff0a6eb-9885-4c7f-9d03-00c09c0a7e4b.id.repl.co/?username={User}').json()
	name = Data['name']
	bio = Data['bio']
	followers = Data['followers']
	following = Data['following']
	id = Data['id']
	image = Data['avatar']
	print("Username : " + str(User))
	print("Name : "+ str(name))
	print("Bio : "+ str(bio))
	print("Followers : "+ str(followers))
	print("Following : "+ str(following))
	print("Id : "+ str(id))
	print("Image Url : "+ str(image))
	print("\nFor more tools, follow me !")
TikTok()