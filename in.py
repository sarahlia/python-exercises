friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

print("rix" in "matrix")

movies_watched = {"Inception", "The Green Book", "The Lord of the Rings"} #we don't care about order here, so use set
user_movie = input("Enter a movie you've watched recently: ")
# print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't seen that yet.")


number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y": #compares the lowercase y user_input to "y". OR do this instead of using 'lower': if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You got it!")
    elif number - user_number in (1, -1): #OR do this(better): elif abs(number - user_number) == 1:
        print("You were off by 1..")
    else:
        print("Sorry, you guessed wrong.")
