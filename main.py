print("hello you")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "your are", age, "years old")

health = 10

print("You are starting with", health, "health")

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes": 
        print("let's play!")

        left_or_right = input("First Choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around? (across/around)? ")

            if ans == "around":
                print("You went around and reach the other side of the lake")

            elif ans == "across":
                print("You managed to get across, but were bit by an Eel and lost 5 health.")
                health -= 5


        else:
            print("You fell into a ravine and lost...")


    else:
        print("See you later...")
      
elif age >= 14:
    print("You can play with a supervisor")
else:
    print("You are not old enough to play")
