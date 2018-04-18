import pygame
from pygame.locals import *

bright_black = (255,50,0)
black = (200,40,0)

bright_grey = (100, 100, 100)
grey = (200, 200, 200)

white = (255, 255, 255)

display_width = 960
display_height = 768

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Checkin Here')

def screenintro():
    bright_grey = (100, 100, 100)
    grey = (200, 200, 200)
    pygame.init()


    while True:
        for e in pygame.event.get():
            if e.type == QUIT:

                pygame.quit()
                quit()
    button('Begin Checkin', 150, 450, 100, 50, grey, bright_grey, button())
    button('Cancel', 550, 450, 100, 50, black, bright_black, button())
    pygame.display.update()



def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def button(msg = 'hello',x = 0,y =0,w = 50,h =50,ic = 25,ac = 25,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

if __name__ == '__main__': screenintro()

pygame.quit()
quit()



def security():
    age = input("Please enter your age.")
    if age == "<15":
        print("Please get a guardian")
        info()
    elif age == "15>=":
        print("Please enter your full name")
    else:
        print("Please enter your age")

def identification():
    choice = input("Please scan your passport by pressing the scan passport button and wait until the blue light turns on. If you want to go back to the info menu please press back.")
    if choice == "scan passport":
        security()
    elif choice == "go back":
        info()

def identification2():
    choice = input("Please enter you confirmation code on the keypad below or enter you first and last name" )
    if choice == "keypad":
        flight()
    elif choice == "name":
        name()

def flight():
    choice = input("you are taking flight 971 to Reykjavik, correct?")
    if choice == "yes":
        boardingpass()
    elif choice == "no":
        identification2()

def info():
    print("Good morning! Please enter your information or scan your passport. Thank you.")
    choice = input("you can enter your identification through passport or your confirmation code. Please select one option.")
    if choice == "passport":
        identification()
    elif choice == "confirmation code":
        identification2()
    else:
        print("you can enter your identification through passport or your confirmation code. Please select one option.")
        info()

def security():
    age = input("Please enter your age.")
    if age == "<15":
        print("Please get a guardian")
        info()
    elif age == "15>-":
        print("Please enter your full name")
    else:
        print("Please enter your age")

screenintro()
info()