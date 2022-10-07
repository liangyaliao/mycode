#!/usr/bin/env python3
"""Amazon Apprenti - Python Project | Liangyan Liao
   creating a simple snake game."""

#import time
import random
import pygame
# from playsound import playsound
from pygame import mixer
# from gtts import gTTS
import sys

#to convert text to audio, and create welcome.mp3 file.
# def convert_to_audio(text):
#     audio = gTTS(text)
#     audio.save("welcome.mp3")
#     playsound(audio)
# convert_to_audio("Hello, welcome to lillian's snake game")

pygame.init() #initiate pygame
WINDOW_SIZE = 600 #to initiate screen's width and length
screen = pygame.display.set_mode([WINDOW_SIZE]*2) #set screen

#load and play welcome.mp3
mixer.music.load('welcome.mp3')
mixer.music.play(-1)

bgmusic = mixer.Sound('class_project/bgmusic.mp3')
bgmusic.play()

snake_unit_size = 20
def snake(snake_unit_size, snake_body):
    """create a segment of snake"""
    for unit in snake_body:
        pygame.draw.rect(screen, "blue", [unit[0], unit[1], snake_unit_size, snake_unit_size])

def rando():
    """get a random x or y axis for snake and food"""
    return round(random.randrange(0, WINDOW_SIZE\
              - snake_unit_size) / snake_unit_size) * snake_unit_size

def choose():
    """after game over, player will need to choose continue or exit"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #press x on top of screen to quit game
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #press esc key to quit game
                exit()
            elif event.key == pygame.K_c: #press c key to continue
                main()
            else:
                wrong_key() #call wrong_key function

def message(msg, color):
    """set up message style"""
    font_style = pygame.font.SysFont("times new roman", 18)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WINDOW_SIZE / 10, WINDOW_SIZE / 3])


def game_over():
    """when game over,hit wall or snake eat itself"""
    ouch = mixer.Sound('class_project/ouch.mp3')
    ouch.play()
    # ouch.stop()
    screen.fill("blue")
    message("c-Play esc-Quit arrows-Move f-Faster", "white")
    pygame.display.update()

def wrong_key():
    """when player hits a wrong key, it will play wrong.mp3"""
    wrong_key = mixer.Sound('class_project/wrong.mp3')
    wrong_key.play()

def main():
    """game on"""
    #initiate snake
    snake_x_axis = rando()
    snake_y_axis = rando()
    snake_x_axis_change = 0
    snake_y_axis_change = 0
    snake_body = []
    length_of_snake = 1
    snake_speed = 5
    #initiate apple's position
    apple_x_axis = rando()
    apple_y_axis = rando()

    running = True
    while running:
        #screen.fill("black")
        #setup background image for screen
        bgimg = pygame.image.load('class_project/grass.jpg')
        bgimg_top = screen.get_height() - bgimg.get_height()
        bgimg_left = screen.get_width()/2 - bgimg.get_width()/2
        screen.blit(bgimg, (bgimg_left,bgimg_top))
        #use arrow keys to move snake
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_axis_change = -snake_unit_size
                    snake_y_axis_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_axis_change = snake_unit_size
                    snake_y_axis_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_axis_change = -snake_unit_size
                    snake_x_axis_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_axis_change = snake_unit_size
                    snake_x_axis_change = 0
                elif event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_f:
                    snake_speed +=1
                else:
                    wrong_key()
            #click x on top of screen to exit game.
            elif event.type == pygame.QUIT:
                sys.exit()
        #move arrow keys, draw snake's new segment on the new cordinates=>snake move
        snake_x_axis += snake_x_axis_change
        snake_y_axis += snake_y_axis_change
        pygame.draw.rect(screen, "red", [apple_x_axis, \
                        apple_y_axis, snake_unit_size, snake_unit_size])
        #the new segment will become snake's head, head will concat with its prior body
        snake_head = []
        snake_head.append(snake_x_axis)
        snake_head.append(snake_y_axis)
        snake_body.append(snake_head)
        #accordingly, delete snake's first segment- its tail, \
        # then snake moves, while keep the sane length
        if len(snake_body) > length_of_snake:
            del snake_body[0]
            snake(snake_unit_size, snake_body)
            for x in snake_body[:-1]:
                if x == snake_head:
                    running = "game over"
                    game_over()
            pygame.display.update()
        #if snake hit walls, call game over function: let player choose to continue or exit.
        if snake_x_axis >= WINDOW_SIZE or snake_x_axis < 0 or \
           snake_y_axis > WINDOW_SIZE or snake_y_axis < 0:
            running = "game over"
            game_over()
        #if snake's head and apple are in the same position => snake ate the apple
        if snake_x_axis == apple_x_axis and snake_y_axis == apple_y_axis:
            #play yummy sound
            yummy = mixer.Sound('class_project/yummy.mp3')
            yummy.play()
            #reset apple position
            apple_x_axis = rando()
            apple_y_axis = rando()
            pygame.display.set_caption(f'Snake ate {length_of_snake - 1} apples')
            length_of_snake += 1

        while running == "game over":
            choose()

        pygame.display.set_caption(f'Press arrow-Snake ate {length_of_snake - 1} apples')
        pygame.time.Clock().tick(snake_speed) #control snake's speed
if __name__ == "__main__":
    main()

