import fnmatch
import os
import pygame
from pygame import mixer

from os import system

mixer.init()
rootpath = "D:\\University\\assistant\\music"
pattern = "*.mp3"
allMusic = []
index = 0
pause = False
# MUSIC_END = pygame.USEREVENT + 1
# pygame.mixer.music.set_endevent(MUSIC_END)
# running = True
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         if event.type == MUSIC_END:
#             print('music end event')
#             pygame.mixer.music.play()

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        allMusic.append("music/" + str(filename))

def play_music():
    pygame.mixer.music.load(allMusic[index])
    pygame.mixer.music.play()




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