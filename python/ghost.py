from random import randint

print("Ghost game is about to start ...")

feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = randint(1, 3)
    
    print("Three doors ahead ... ")
    print("A ghost is behind one.")
    print("Which door door do you open?")

    door = input("1, 2 or 3?")
    door_num = int(door)

    if (door_num == ghost_door):
        print("GHOST!!!")
        feeling_brave = False
    else:
        print("Phew ... no ghost!")
        print("You enter the next room.")
        score = score + 1

print("Run away!!")
print("Game over! You scored: ", score)