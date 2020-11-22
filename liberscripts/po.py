import vk_api, os, time, colorama
from colorama import Fore , Back , Style  

os.system('clear')

print(Fore.YELLOW+'''
  _____             _   
 |  __ \           | |  
 | |__) |___   ___ | |_ 
 |  ___// _ \ / __|| __|
 | |   | (_) |\__ \| |_ 
 |_|    \___/ |___/ \__|
                         by l1berov and utils switch. 
                              
''')
vk_session = vk_api.VkApi(token=input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# '))
api = vk_session.get_api()
numer = int(input(Fore.GREEN+'Введите количество постов'+Fore.WHITE+' ~# '))
mess = input(str(Fore.GREEN+'Введите текст'+Fore.WHITE+' ~# '))
for q in range(int(numer)):
    api.wall.post(message=mess); time.sleep(5); 
    print(Fore.CYAN+'Опубликован пост: '+str(q)+' c текстом: '+str(mess))