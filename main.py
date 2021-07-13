print("hello Adventurer!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "your are", age, "years old")

health = 10


if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("let's play!")

        weapon = input("Pick a weapon (sword/bow/axe) ")

        left_or_right = input("First Choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around? (across/around)? ")

            if ans == "around":
                print("You went around and reach the other side of the lake")

            elif ans == "across":
                print("You managed to get across, but were bit by an Eel and lost 5 health.")
                health -= 5

            ans = input("You see a river and a house, Which do you go to(river/house)? ")
            if ans == "house":
                print("You go the house and get attacked by the owner, you loose 5 health.")
                health -= 5

                if health <= 0:
                    print("You have 0 health and you lost the game...")
                elif weapon == "sword" or "axe":
                    print("Luckily, you manage to fight back thanks to your", weapon, "and escape. You reach a village, you win!")

            else:
                print("you fell into the river and lost...")


        else:
            print("You fell into a ravine and lost...")


    else:
        print("See you later...")
      
elif age >= 14:
    print("You can play with a supervisor")
else:
    print("You are not old enough to play")
