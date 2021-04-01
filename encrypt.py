import os
import sys
import time
os.system("pip install colorama")
from colorama import Fore, Back, Style 
os.system("pkg install figlet -y")
os.system("clear")
print(Fore.GREEN + '') 
def logo():
    os.system("clear")
    os.system("figlet ENCRYPT MSG")
    time.sleep(2)
    print("developer @AkhilAbhi")
    time.sleep(2)

logo()
print("")
print("")

print("1 : encrypt ")
print("2 : decrypt")

che=input("enter number : ")





def code(msg):
    #print(msg)
    msg=msg.replace('a','#')
    msg=msg.replace('b','&')
    msg=msg.replace('c','ê')
    msg=msg.replace('d','ű')
    msg=msg.replace('e','ā')
    msg=msg.replace('f','M')
    msg=msg.replace('g','$')
    msg=msg.replace('h','*')
    msg=msg.replace('i','`')
    msg=msg.replace('j','W')
    msg=msg.replace('k','R')
    msg=msg.replace('l','G')
    msg=msg.replace('m','9')
    msg=msg.replace('n','1')
    msg=msg.replace('o','6')
    msg=msg.replace('p','5')
    msg=msg.replace('q','4')
    msg=msg.replace('r','3')
    msg=msg.replace('s','7')
    msg=msg.replace('t','2')
    msg=msg.replace('u','8')
    msg=msg.replace('v','0')
    msg=msg.replace('w','V')
    msg=msg.replace('x','C')
    msg=msg.replace('y','í')
    msg=msg.replace('z','P')
    msg=msg.replace(' ','+')
    os.system("clear")
    logo()
    print(Fore.YELLOW)
    print("please wait  massge is encrypting....")
    time.sleep(3)
    print(" ")
    
    print('as6 encrypt code')
    print(Back.BLUE)
    print(Fore.RED)
    print(msg)
    print(Style.RESET_ALL)
    
    
    
    


#exit

def exit():
    os.system("clear")
    print("exiting....")
    time.sleep(2)




def decode(msg):
    msg=msg.replace('#','a')
    msg=msg.replace('&','b')
    msg=msg.replace('ê','c')
    msg=msg.replace('ű','d')
    msg=msg.replace('ā','e')
    msg=msg.replace('M','f')
    msg=msg.replace('$','g')
    msg=msg.replace('*','h')
    msg=msg.replace('`','i')
    msg=msg.replace('W','j')
    msg=msg.replace('R','k')
    msg=msg.replace('G','l')
    msg=msg.replace('9','m')
    msg=msg.replace('1','n')
    msg=msg.replace('6','o')
    msg=msg.replace('5','p')
    msg=msg.replace('4','q')
    msg=msg.replace('3','r')
    msg=msg.replace('7','s')
    msg=msg.replace('2','t')
    msg=msg.replace('8','u')
    msg=msg.replace('0','v')
    msg=msg.replace('V','w')
    msg=msg.replace('C','x')
    msg=msg.replace('í','y')
    msg=msg.replace('P','z')
    msg=msg.replace('+',' ')
    os.system("clear")
    print(Fore.RED)
    logo()
    print(Style.RESET_ALL)
    print(Fore.YELLOW)
    print('please wait massge is decryptong...')
    
    print(" ")
    print(" ")
    print("decrypted")
    
    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print(Back.RED)
    print(msg)
    
    print(Style.RESET_ALL)
    
    tx=open("decode.txt","a")
    tx.write(msg)



def encrypt():
    msg=input("enter msg : ")
    if msg:
        code(msg)
    else:
        logo()

if che=='1':
    logo()
    print(' ')
    print(' ')
    encrypt()
    
    # TODO: write code...
elif che=='2':
    logo()
    print(' ')
    print(' ')
    msg=input("past your code (as6) : ")
    if msg:
        decode(msg)
        
    else:
        logo()
        
else:
    exit()
    
    
    

