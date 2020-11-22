import vk_api, os, time, colorama
from colorama import Fore , Back , Style  
from vk_api.utils import get_random_id
from random import randint

os.system('clear')

print(Fore.YELLOW+
'''
  ______      _  _______      ______      _ 
 |  ____|    | ||__   __|    |  ____|    (_)
 | |__  ___  | |   | |  ___  | |__  _ __  _ 
 |  __|/ _ \ | |   | | / _ \ |  __|| '__|| |
 | |  | (_) || |   | || (_) || |   | |   | |
 |_|   \___/ |_|   |_| \___/ |_|   |_|   |_| by darkcoding12 and vktool 
                                                                                                        
''')
token = vk_api.VkApi(token = input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# '))
vk = token.get_api()
fr = vk.users.getFollowers(count=1000, offset=0)['items']
while(fr):
    for frr in fr:
        try:
            vk.friends.add(user_id=frr)
            print(Fore.CYAN+'Подписчик добавлен!')
        except Exception as er:
            print(Fore.RED+"Подписчик в бане!")
    main()