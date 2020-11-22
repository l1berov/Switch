import vk_api, os, time, colorama
from colorama import Fore , Back , Style  
from vk_api.utils import get_random_id
from random import randint

os.system('clear')

print(Fore.YELLOW+
'''
   _____                       
  / ____|                      
 | (___  _ __   __ _ _ __ ___  
  \___ \| '_ \ / _` | '_ ` _ \ 
  ____) | |_) | (_| | | | | | |
 |_____/| .__/ \__,_|_| |_| |_| by batyarimsky
        | |                    
        |_|                                                                               

''')    
tok = input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# ')
token = vk_api.VkApi(token = tok) 
vk = token.get_api()
num = int(input(Fore.GREEN+'Введите количество смс'+Fore.WHITE+' ~# '))
mes = input(Fore.GREEN+'Введите сообщение для рассылки'+Fore.WHITE+' ~# ')
for a in range(num):
    try:
        ange = randint(666666, 99999999)
        vk.messages.send(user_id=ange, message=mes, random_id=get_random_id())
        time.sleep(25)
    except Exception as e:
        print(Fore.CYAN+'Стоят настройки приватности!')