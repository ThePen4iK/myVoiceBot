import speech_recognition as sr
import pyttsx3
from fuzzywuzzy import fuzz
import random
import sys
import pygame
from os import system
import music

ndel = ['сара', 'не могла бы ты']

commands = ['привет', 'пока',
            'включи музыку', 'включить музыку',
            'следующую', 'включить следующую песню', 'следующая', 'включи следующую песню',
            'верни назад', 'вернуть назад',
            'поставь на паузу', 'поставить на паузу',
            'включи в случайном порядке', 'включить в случайный порядок', 'включи рандом', 'рандом',
            'в рандомном порядке',
            'повтор', 'поставь на повтор',
            'возобнови', 'возобновить'
            ]

r = sr.Recognizer()
pygame.init()
engine = pyttsx3.init()
text = ''
j = 0
num_task = 0


def talk(speech):
    print(speech)
    engine.say(speech)
    engine.runAndWait()


def fuzzy_recognizer(rec):
    global j
    ans = ''
    for i in range(len(commands)):
        k = fuzz.ratio(rec, commands[i])
        if (k > 70) & (k > j):
            ans = commands[i]
            j = k
    return str(ans)


def clear_task():
    global text
    for i in ndel:
        text = text.replace(i, '').strip()
        text = text.replace('  ', ' ').strip()


def listen():
    global text
    text = ''
    with sr.Microphone() as source:
        print("Я вас слушаю...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ru-RU").lower()
        except sr.UnknownValueError:
            pass
        # print(text)
        system('cls')
        clear_task()
        return text


def cmd_init():
    global text, num_task
    text = fuzzy_recognizer(text)
    print(text)
    if text in cmds:
        if (text != 'пока') & (text != 'привет') & (text != 'включи музыку') \
                & (text != 'включить музыку') & (text != 'следующую') \
                & (text != 'включить следующую песню') & (text != 'следующая') \
                & (text != 'включи следующую песню') & (text != 'верни назад') & (text != 'вернуть назад') \
                & (text != 'поставь на паузу') & (text != 'поставить на паузу') & (text != 'возобнови') & (
                text != 'возобновить') \
                & (text != 'включи в случайном порядке') & (text != 'включить в случайный порядок') & (
                text != 'включи рандом') \
                & (text != 'рандом') & (text != 'в рандомном порядке') & (text != 'повтор') & (
                text != 'поставь на повтор'):
            k = ['Секундочку', 'Сейчас сделаю', 'Уже выполняю']
            talk(random.choice(k))
        cmds[text]()
    elif text == '':
        print("Команда не распознана")
    num_task += 1
    # if num_task % 10 == 0:
    #     talk('У вас будут еще задания?')
    engine.runAndWait()
    engine.stop()


def music_play():
    talk("Включаю")
    music.play_music()
    system('cls')


def music_next():
    x = ['Переключаю', 'Секундочку', 'Щяс сделаю']
    music.next_music()
    system('cls')


def music_prev():
    x = ['Переключаю', 'Секундочку', 'Щяс сделаю']
    talk(random.choice(x))
    music.prev_music()
    system('cls')


def music_pause():
    talk("Останавливаю")
    music.pause_music()
    system('cls')


def music_unpause():
    talk("возобновляю")
    music.unpause_music()
    system('cls')


def music_random():
    music.random_music()
    system('cls')


def music_repeat():
    x = ['Выполняю', 'Секундочку', 'Щяс сделаю']
    talk(random.choice(x))
    music.repeat_music()
    system('cls')


def hello():
    k = ['Привет, чем могу помочь?']
    talk(random.choice(k))


def quite():
    x = ['Надеюсь мы скоро увидимся!', 'Рада была помочь']
    talk(random.choice(x))
    engine.stop()
    system('cls')
    sys.exit(0)


cmds = {
    'включи музыку': music_play, 'включить музыку': music_play,

    'следующую': music_next, 'включить следующую песню': music_next, 'следующая': music_next,
    'включи следующую песню': music_next,

    'верни назад': music_prev, 'вернуть назад': music_prev,

    'поставь на паузу': music_pause, 'поставить на паузу': music_pause,

    'возобнови': music_unpause, 'возобновить': music_unpause,

    'включи в случайном порядке': music_random, 'включить в случайный порядок': music_random,
    'включи рандом': music_random, 'рандом': music_random, 'в рандомном порядке': music_random,

    'повтор': music_repeat, 'поставь на повтор': music_repeat,

    'привет': hello,
    'пока': quite,
}

talk('Привет, я Сара, чем могу помочь?')
system('cls')


def main():
    global text, j
    try:
        listen()
        if text != '':
            cmd_init()
            j = 0
    except UnboundLocalError:
        pass
    except NameError:
        pass
    except TypeError:
        pass


while True:
    main()

