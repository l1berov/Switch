import colorama, os, time, vk_api, sys
from os import system
from colorama import Fore , Back , Style

os.system('clear')

print(Fore.YELLOW+'''
  ______    _                _ 
 |  ____|  (_)              | |
 | |__ _ __ _  ___ _ __   __| |
 |  __| '__| |/ _ \ '_ \ / _` |
 | |  | |  | |  __/ | | | (_| |
 |_|  |_|  |_|\___|_| |_|\__,_| by batyarimskiy                          
''')

with open("ids.txt") as f:
    user_ids = f.read().splitlines()

session = vk_api.VkApi(token = input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# '))
vk = session.get_api()
    
for user_id in user_ids:
    vk.friends.add(
        user_id=user_id
    )
        
    time.sleep(40)