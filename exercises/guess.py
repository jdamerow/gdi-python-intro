from random import randint

def get_input():
    user_input = raw_input("Guess the number I though of: ")
    input_as_int = int(user_input)
    return input_as_int

random_number = randint(1, 10)

input_as_int = get_input()

# looping over user input
while input_as_int != random_number:
    if input_as_int > random_number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    input_as_int = get_input()

print("You are right! You are so awesome!")
print(random_number)
