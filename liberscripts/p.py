import vk_api, colorama, os
from vk_api import VkUpload
from colorama import Fore , Back , Style

os.system('clear')

print(Fore.YELLOW+'''
  _____  _           _        
 |  __ \| |         | |       
 | |__) | |__   ___ | |_ ___  
 |  ___/| '_ \ / _ \| __/ _ \ 
 | |    | | | | (_) | || (_) |
 |_|    |_| |_|\___/ \__\___/  by l1berov and utils switch. 
                              
''')

vk_session = vk_api.VkApi(token=input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# '))
api = vk_session.get_api()

upload = vk_api.VkUpload(vk_session)

alb = input(Fore.GREEN+'Введите id альбома'+Fore.WHITE+' ~# ')
#/----------------------------------------------------------------------------/#
for i in range(9999):
    phot6 = upload.photo('lol.png',album_id=int(alb)) 
    print(Fore.CYAN+Back.BLACK+'Загруженнa фотография №'+str( i))
else:
	print(Fore.RED+'Произошла ошибка!')