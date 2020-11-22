import vk_api, time, colorama, os
from vk_api.longpoll import VkLongPoll, VkEventType
from colorama import Fore , Back , Style

os.system('clear')

print(Fore.YELLOW+
'''
   _____  _             _   
  / ____|| |           | |  
 | |     | |__    __ _ | |_ 
 | |     | '_ \  / _` || __|
 | |____ | | | || (_| || |_ 
  \_____||_| |_| \__,_| \__|  by l1berov and utils switch.

''')

vk_session = vk_api.VkApi(token=input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# '))
api = vk_session.get_api()
users = input(Fore.GREEN+'Введите id страницы, которая будет добавлена в беседу'+Fore.WHITE+' ~# ')
for i in range(9999):
    api.messages.createChat(user_ids=users, title="Created By l1berov"); time.sleep(80)
    print(Fore.CYAN+Back.BLACK+'Создана беседа №'+str( i)) 

else:
  print(Fore.RED+'Произошла ошибка!')