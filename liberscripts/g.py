import vk_api, os, time, colorama
from colorama import Fore , Back , Style  

os.system('clear')

print(Fore.YELLOW+'''
   _____                       
  / ____|                      
 | |  __ _ __ ___  _   _ _ __  
 | | |_ | '__/ _ \| | | | '_ \ 
 | |__| | | | (_) | |_| | |_) |
  \_____|_|  \___/ \__,_| .__/ 
                        | |    
                        |_|    by l1berov and utils switch. 
                              

Утилита находится в бета - тестировании из за множество капчи при ее работе. 
''')

vk_session = vk_api.VkApi(token=input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# '))

tit = input(Fore.GREEN+'Введите название для групп'+Fore.WHITE+' ~# ')

api = vk_session.get_api()

for i in range(9999):
    api.groups.create(title=tit, description='vk.com/0blivion.lost'); time.sleep(25)
    print(Fore.CYAN+Back.BLACK+'Создана группа №'+str( i)) 
