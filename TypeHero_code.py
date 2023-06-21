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



wordlist = open('./wordlist/Person.java')

dictionary = []
for word in wordlist:
    if word != "\n":
        dictionary.append(word.strip().rstrip("\n"))

def C_input(wrd):
    responce = ""
    wrd_pos = 0
    colours = []
    while True:
        key = ord(getch.getch())
        
        if key == 127:
            responce = responce[:-1]
            colours = colours[:-1]
            wrd_pos -= 1

        else:
            char = chr(key)
            if char == wrd[wrd_pos]:
                # sys.stdout.write(colour.GREEN + chr(key) + colour.END)
                colours.append(colour.GREEN)
            else:
                # sys.stdout.write(colour.RED + chr(key) + colour.END)
                colours.append(colour.RED)

            # sys.stdout.flush()
            responce += char
            wrd_pos += 1

        print("\033[A")
        for i,letter in enumerate(responce):
            print(colours[i] + letter +colour.END, end ='')
        print(wrd[wrd_pos:], end='')
        sys.stdout.flush()

        if(len(responce) == len(wrd)):
            print()
            return responce

# main gameplay loop

wrd_count = 0
incorrect = 0
minutes = int(input('minutes : '))
t_start = time.time()
while (time.time()-t_start < minutes*60):
    wrd = random.choice(dictionary)
    print(wrd,end='')
    sys.stdout.flush()
    print("\033[A")
    responce = C_input(wrd)
    if responce == wrd:
        wrd_count += 1
    else:
        incorrect += 1
        print(colour.RED + 'Incorrect' + colour.END)





print(f'words total = {wrd_count}')
print(f'misspellings = {incorrect}')
print(f'words per minute = {wrd_count/minutes}')





