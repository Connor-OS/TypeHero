import pygame
from pygame import mixer
import time
import random
import vlc
import sys
import random
import time
import getch


displayWidth = 800
displayHeight = 600 


def load_wordlist() -> list:
    wordfile = open('/usr/share/dict/words')
    wordlist = []
    for word in wordfile:
        wordlist.append(word.rstrip("\n"))
    return wordlist

def init_Pygame() -> pygame.display:
    pygame.init()
    mixer.init()

    surface= pygame.display.set_mode((displayWidth, displayHeight ))
    surface.fill((0,0,0)) 

    pygame.display.set_caption('TypeHero')
    return surface

def display_word() -> str:
    display_surface.fill((0,0,0)) 
    word = random.choice(wordlist)
    text = font.render(word, True, white, black)
    textRect = text.get_rect()
    textRect.center = (displayWidth/2,displayHeight/3)
    display_surface.blit(text, textRect)
    return word


def display_type(user_word) -> str:
    # display_surface.fill((0,0,0)) 
    text = font.render(user_word, True, white, black)
    textRect = text.get_rect()
    textRect.center = (displayWidth/2,2*displayHeight/3)
    display_surface.blit(text, textRect)
    return word


if(__name__) == "__main__":
    print('oio')
    wordlist = load_wordlist()
    display_surface = init_Pygame()
    font = pygame.font.Font('freesansbold.ttf', 32)
    white = (255, 255, 255)
    red = (255, 0, 0)
    red = (0, 255, 0)
    black = (0, 0, 0)


    while True:

        for event in pygame.event.get():

            
            if event.type == pygame.QUIT:
            
                pygame.quit()
                quit()
            
            word = display_word()
            user_word = ''
            while(word):
                char = chr(ord(getch.getch()))
                correct_char = True
                user_word += char
                if(char != word[0]):
                    print(char)
                    correct_char = False
                display_type(user_word)
                word = word[1:]
                pygame.display.update()
            

