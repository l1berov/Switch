# Switch by l1berov
import colorama, os, time
from os import system
from colorama import Fore , Back , Style

os.system("clear")
os.chdir('liberscripts')
	
print(Fore.YELLOW+'''
   _____         _ _       _     
  / ____|       (_) |     | |    
 | (_____      ___| |_ ___| |__  
  \___ \ \ /\ / / | __/ __| '_ \ 
  ____) \ V  V /| | || (__| | | |
 |_____/ \_/\_/ |_|\__\___|_| |_| by l1berov 
''')
print(Fore.WHITE+'\n         [0] - Выход из программы ')
print(Fore.BLUE+'┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
print(Fore.BLUE+'┃ № ┃ Описание                              ┃')
print(Fore.BLUE+'┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩')
print(Fore.YELLOW+'│ 1 │ Накрутка фотографий                   │')
print(Fore.YELLOW+'│ 2 │ Накрутка музыки                       │')
print(Fore.YELLOW+'│ 3 │ Рассылка смс                          │')
print(Fore.YELLOW+'│ 4 │ Накрутка комментариев                 │')
print(Fore.GREEN+'│ 5 │ Накрутка сообщений                    │')
print(Fore.GREEN+'│ 6 │ Накрутка групп                        │')
print(Fore.GREEN+'│ 7 │ Накрутка постов                       │')
print(Fore.GREEN+'│ 8 │ Накрутка друзей                       │')
print(Fore.RED+'│ 9 │ Отчистка постов со стены              │')
print(Fore.RED+'│10 │ Бан страницы                          │')
print(Fore.RED+'│11 │ Перевести подписчиков в друзья        │')
print(Fore.RED+'└───┴───────────────────────────────────────┘')
print(Fore.CYAN+'         Telegram: t.me/liberovstory')

num = input(Fore.CYAN+'\n~/liber/switch/~'+Fore.WHITE+'# ')

if num == ('1'):
  os.system('python3 p.py')
elif num == ('2'):
  os.system('python3 m.py')
elif num == ('3'):
  os.system('python3 sp.py')
elif num == ('4'):
  os.system('python3 c.py')
elif num == ('5'):
  os.system('python3 s.py')
elif num == ('6'):
  os.system('python3 g.py')
elif num == ('7'):
  os.system('python3 po.py')
elif num == ('8'):
  os.system('python3 fff.py')
elif num == ('9'):
  os.system('python3 ucp.py')
elif num == ('10'):
  os.system('python3 b.py')
elif num == ('11'):
  os.system('python3 ftp.py')
