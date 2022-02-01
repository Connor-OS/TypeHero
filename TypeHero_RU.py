import os
import sys
import pandas as pd
import glob
import random
import time

application_path = os.path.dirname(sys.executable)

# Get wordlist from user
while True:
    print('choose wordlist from:')
    files = [file[19:] for file in glob.glob("./wordlist/russian/*")]
    [print(file, end =", ") for file in files]
    print()
    lis = input('-')
    if lis in files:
        break
    else:
        print('wordlist not found')

# Get language from the user
while True:
    lang = input('Choose language from: \nEnglish or Руски: ')
    if lang == 'English':
        dictionary = pd.read_csv('./wordlist/russian/'+lis,index_col='RU')
        break
    elif lang == 'Руски':
        dictionary = pd.read_csv('./wordlist/russian/'+lis,index_col='EN')
        break
    else:
        print('language not supported')

# main gameplay loop
wrd_count = 0
incorrect = 0
minutes = int(input('minutes : '))
t_start = time.time()
while (time.time()-t_start < minutes*60 and dictionary.shape[0] > 0):
    wrd = random.choice(dictionary.index)
    print('Word is:',wrd)
    responce = input('-')
    if responce == dictionary.loc[wrd][0]:
        wrd_count += 1
        dictionary = dictionary.drop(wrd)
        print('Correct')
    else:
        incorrect += 1
        print('Incorrect, translation was', dictionary.loc[wrd][0])

#final statistics
print(f'words total = {wrd_count}')
print(f'misspellings = {incorrect}')
print(f'words per minute = {wrd_count/minutes}')