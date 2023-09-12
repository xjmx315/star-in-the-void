'''
2023.09.09
팀 개쩌는고릴라! 깃허브 사용 연습. class 사용 연습.

2023.09.11
vidual studio 에서 파이썬 실생시 계속 non-utf-8 에러가 나서 고생했다. 
결국 file을 utf-8로 다시 만들어 주었는데, 자동으로 새 파일을 설정하는 법은 못 찾았다. 
'''

import savefile
from pyfiglet import Figlet
import os
version = '1.0'

print(os.getcwd())
font = Figlet(font = 'slant')
print(font.renderText('''+++++++++++
  star in the
  v   o    i    d
+++++++++++
'''))

