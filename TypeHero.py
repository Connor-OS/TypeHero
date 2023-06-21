# A simple fun typing game with lots of performace monitoring features
#!/home/connor/PycharmProjects/Test/venv/bin/python3
import sys
import random
import time
import getch

class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


wordlist = open('/usr/share/dict/words')
dictionary = []
for word in wordlist:
    dictionary.append(word.rstrip("\n"))

def C_input():
    responce = ""
    while True:
        key = ord(getch.getch())
        char = chr(key)
        if key == 32 or key == 13:
            break
        sys.stdout.write(chr(key))
        sys.stdout.flush()
        responce = responce + chr(key)
    print()
    return responce

# main gameplay loop

wrd_count = 0
incorrect = 0
minutes = int(input('minutes : '))
t_start = time.time()
while (time.time()-t_start < minutes*60):
    wrd = random.choice(dictionary)
    print(wrd)
    responce = C_input()
    if responce == wrd:
        wrd_count += 1
    else:
        incorrect += 1
        print(colour.RED + 'Incorrect' + colour.END)





print(f'words total = {wrd_count}')
print(f'misspellings = {incorrect}')
print(f'words per minute = {wrd_count/minutes}')





