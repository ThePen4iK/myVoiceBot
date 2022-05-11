import fnmatch
import os
import pygame
import random
from pygame import mixer
import threading
from os import system

mixer.init()
rootpath = "D:\\University\\assistant\\music"
pattern = "*.mp3"
allMusic = []
index = 0
pause = False
running = True



for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        allMusic.append("music/" + str(filename))


def check__music():
    global index
    global running

    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MUSIC_END:
                print("music play")
                index += 1
                pygame.mixer.music.load(allMusic[index])
                pygame.mixer.music.play()


def play_music():
    global index

    pygame.mixer.music.load(allMusic[index])
    pygame.mixer.music.play()
    my_thread = threading.Thread(target=check__music, args=(), daemon=True)
    my_thread.start()

        # for event in pygame.event.get():
        #     if event.type == MUSIC_END:

                # index += 1
                # pygame.mixer.music.load(allMusic[index])
                # pygame.mixer.music.play()

def next_music():
    global index
    index += 1
    pygame.mixer.music.load(allMusic[index])
    pygame.mixer.music.play()


def prev_music():
    global index
    index = index - 1
    pygame.mixer.music.load(allMusic[index])
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def random_music():
    global index
    randomMusic = random.choice(allMusic)
    pygame.mixer.music.load(randomMusic)
    pygame.mixer.music.play()
    # if pygame.mixer.get_busy() == False
    #     index += 1
    #     pygame.mixer.music.load(allMusic[index])
    #     pygame.mixer.music.play()


def repeat_music():
    pygame.mixer.music.play(-1)
