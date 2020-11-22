import vk_api, colorama, os
from vk_api import VkUpload
from colorama import Fore , Back , Style

os.system('clear')

print(Fore.YELLOW+
'''
  __  __              _       
 |  \/  |            (_)      
 | \  / | _   _  ___  _   ___ 
 | |\/| || | | |/ __|| | / __|
 | |  | || |_| |\__ \| || (__ 
 |_|  |_| \__,_||___/|_| \___| by l1berov and utils switch.

''')

vk_session = vk_api.VkApi(token=input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# '))
api = vk_session.get_api()

upload = vk_api.VkUpload(vk_session)

for i in range(9999):
	s = upload.audio(audio="lol.mp3", artist="l1berov", title="switch")
	print(Fore.CYAN+Back.BLACK+'Загруженнa фотография №'+str( i))