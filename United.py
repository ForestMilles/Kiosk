def security():
    age = input("Please enter your age.")
    if age == "<15":
        print("Please get a guardian")
        info()
    elif age == "15>=":
        print("Please enter your full name")
    else:
        print("Please enter your age")
        

<<<<<<< HEAD
=======
def identification():
    choice = input("Please scan your passport by pressing the scan passport button and wait until the blue light turns on. If you want to go back to the info menu please press back.")
    if choice == "scan passport":
        security()
    elif choice == "go back":
        info()

>>>>>>> 7c99515394acbbe0fddfcc680d475e390e4e788d
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
            
<<<<<<< HEAD
def security():
    age = input("Please enter your age.")
    if age == "<15":
        print("Please get a guardian")
        info()
    elif age == "15>-":
        print("Please enter your full name")
    else:
        print("Please enter your age")
        
            

        
=======
info()
>>>>>>> 7c99515394acbbe0fddfcc680d475e390e4e788d
