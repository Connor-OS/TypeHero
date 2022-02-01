# A simple fun typing game with lots of performace monitoring features
#!/home/connor/PycharmProjects/Test/venv/bin/python3
import sys
import random
import time
import getch
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
        print('Incorrect')





print(f'words total = {wrd_count}')
print(f'misspellings = {incorrect}')
print(f'words per minute = {wrd_count/minutes}')
