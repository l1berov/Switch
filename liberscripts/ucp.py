import vk_api, os, time, colorama
from colorama import Fore , Back , Style  

os.system('clear')

print(Fore.YELLOW+'''
  _    _ _____          _   
 | |  | |  __ \        | |  
 | |  | | |__) |__  ___| |_ 
 | |  | |  ___/ _ \/ __| __|
 | |__| | |  | (_) \__ \ |_ 
  \____/|_|   \___/|___/\__| by l1berov and utils switch. 
                              
''')
vk_session = vk_api.VkApi(token=input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# '))
api = vk_session.get_api()
posts = api.wall.get(count=100)['items']
while(posts):
    for post in posts:
        api.wall.delete(post_id=post['id'])
        posts = api.wall.get(count=100)['items']
        print(Fore.CYAN+'Пост удален!')
