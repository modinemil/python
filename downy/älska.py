import time

def älskar_älskarinte():
    antal = int(input())
    try:
        float(antal)
    except ValueError:
        print("This is not a number")
    
    varannan = False
    
    while antal > 0:

        if varannan == False:
            print("älskar")
        else:
            print("älskar inte")
        antal = antal -1
        varannan = not varannan
        time.sleep(0.75)

älskar_älskarinte()