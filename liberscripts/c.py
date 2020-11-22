import vk_api, colorama, os, time

from colorama import Fore , Back , Style

e = 1

os.system('clear')

print(Fore.YELLOW+
'''
   _____                          
  / ____|                         
 | |     ___  _ __ ___  _ __ ___  
 | |    / _ \| '_ ` _ \| '_ ` _ \ 
 | |___| (_) | | | | | | | | | | |
  \_____\___/|_| |_| |_|_| |_| |_| by l1berov and utils switch.

''')   
tok = input(Fore.GREEN+'Введите токен'+Fore.WHITE+' ~# ')
token = vk_api.VkApi(token = tok) 
vk = token.get_api()
owner = input(Fore.GREEN+'Введите id страницы, куда нужно писать комментарии'+Fore.WHITE+' ~# ')
postid = input(Fore.GREEN+'Введите id поста'+Fore.WHITE+' ~# ')
massa = input(str(Fore.GREEN+'Введите текст'+Fore.WHITE+' ~# '))
for e in range(999999):
    vk.wall.createComment(owner_id=owner,post_id=postid,message=massa); time.sleep(20)