def cheer(name):
    for letter in name:
        print(f"Gimme a {letter}!")
    print("What does that spell?")
    print(f"{name}!")

user_input = input("What's your name? ")
cheer(user_input)
