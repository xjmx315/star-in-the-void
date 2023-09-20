#jmutils.py
version = '1.0'
import time

def choice(options, qustion = ''):
    print(qustion)
    for i, option in enumerate(options):
        print(i, option)
    answer = input()
    try:
        answer = int(answer)
        if -1< answer < len(options):
            return answer
        else: 
            print('범위에 맞는 입력을 해주세요. ')
            return choice(options)
    except:
       print('올바른 숫자를 입력해 주세요. ')
       return choice(options)
   
def say(string, temp = 0.02):
    for i in string:
        print(i, end = '', flush=True)
        time.sleep(temp)
        