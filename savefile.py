version = '1.0'
loadtype = '.game'
from genericpath import isfile
import os
import jmutils
import pickle
import time

class gamefile:
    def __init__(self, filename):
        self.filename = filename
        self.version = '1.0'
        self.username = ''
        self.metapath = ''
    
    def make_meta(self, path):
        self.metapath = path
        data = metafile(self.filename)
        data.info = 'star-in-the-void game save file'
        data.user = self.username
        with open(os.path.join(path, self.filename+'.meta')) as fw:
            pickle.dump(data, fw)
        return os.path.join(path, self.filename+'.meta')
    
class metafile:
    def __init__(self, filename):
        self.filename = filename
        self.lastsave = time.time()
        self.info = ''
        self.user = ''
        
    def info(self):
        time = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(self.lastsave))
        info = self.info +'\n'+ time +'\n'+ self.user
        return info
    
#-------------
def get_gamefile(path = os.getcwd()):
    #print(path, '에서 파일을 불러옵니다. ')
    able_files = choice_file(loadtype+'.meta', path)
    targetindex = jmutils.choice(['새로 만들기']+able_files, '---불러올 파일을 선택하세요: ')
    if targetindex:
        target = able_files[targetindex-1]
        print(read_metafile(os.path.join(path, target)))
        if jmutils.choice(['아니오', '예'], '이 파일을 로드할까요?'):
            if os.path.isfile(os.path.join(path, target[:-5])):
                with open(os.path.join(path, target[:-5]), 'rb') as fr:
                    data = pickle.load(fr)
                return data
            else:
                print('메타파일은 존재하지만 연결된 파일이 없습니다. ')
                return get_gamefile(path) #개선 가능성
    return make_file(path)

def make_file(path):
    print('새로운 파일의 이름을 입력하세요: ')
    filename = input()
    data = gamefile(filename + '.' + loadtype)
    data.make_meta(path)
    with open(os.path.join(path, filename), 'wb') as fw:
        pickle.dump(data, fw)
    return data
    
def read_metafile(path):
    with open(path, 'rb') as fr:
        data = pickle.load(fr)
    return data.info()
     
def choice_file(filetype = None, path = None):
    if filetype:
        target = []
        for filename in os.listdir(path):
            if ismatch_type(filename, filetype):
                target.append(filename)
        return target
    return os.listdir()
            
def ismatch_type(filename, filetype):
    i = -1
    while i >= len(filetype)*(-1):
        if filename[i] != filetype[i]:
            return 0
        i -= 1
    return 1
#----------------------

def set_type(newtype):
    global loadtype
    loadtype = newtype