import pygame
from pygame.locals import *

userface = [1024,768]
def main():
    pygame.init()
    screen = pygame.display.set_mode(userface)
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                return

if __name__ == '__main__':
    main()

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
    choice = input("you are taking flight 971 to Rekjavik, correct?")
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
               
info()