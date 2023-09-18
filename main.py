'''
2023.09.09
팀 개쩌는고릴라! 깃허브 사용 연습. class 사용 연습.

2023.09.11
vidual studio 에서 파이썬 실생시 계속 non-utf-8 에러가 나서 고생했다. 
결국 file을 utf-8로 다시 만들어 주었는데, 자동으로 새 파일을 설정하는 법은 못 찾았다. 

2023.09.12
savefile 1.0을 완성했다. 아직 테스트는 해보지 않았다. 
'''

import savefile
savefile.set_type('sitv')
from pyfiglet import Figlet
import os
import jmutils

version = '1.0'
CWD = os.getcwd()

def print_intro():
    print(CWD)
    font = Figlet(font = 'slant')
    print(font.renderText('''+++++++++++
      star in the
      v   o    i    d
    +++++++++++
    '''))

def check_files(checklist = None, CWD = os.getcwd()):
    if checklist == None:
        checklist = [{'save':[{}]}]
    unexistlist = []
    for i in checklist[0].keys():
        os.makedirs(CWD+'\\'+i, exist_ok=1)
        unexistlist += check_files(checklist[0][i], CWD+'\\'+i)
    for i in range(1, len(checklist)):
        if not os.path.isfile(CWD+'\\'+checklist[i]):
            unexistlist.append(checklist[i])
    return unexistlist
    
def chcwd(path):
    global CWD
    CWD = path
    
def start():
    print(CWD)
    print_intro()
    unexistfiles = check_files(CWD = CWD)
    if unexistfiles:
        print('누락 요소: ')
        print(*unexistfiles, sep = '\n')
        print('필수 구성 요소가 누락되어 게임을 실행할 수 없습니다. ')
        input('enter to exit...')
        return -1
    
start()
    