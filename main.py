print("hello you")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "your are", age, "years old")

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ")
    if wants_to_play == "yes": 
      print("let's play")
      
elif age >= 14:
    print("You can play with a supervisor")
else:
    print("You are not old enough to play")
