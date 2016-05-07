health = 100
print("A vicious warg is chasing you.")
print("Options:")
print("1 - Hide in the cave.")
print("2 - Climb a tree.")

input_value = ''

while input_value != 'exit' and health > 80:
    input_value = raw_input("Enter choice:")

    if input_value == '1':
        print('You hide in a cave.')
        print('The warg finds you and injures your leg with its claws')
        health = health - 10
    elif input_value == '2':
        print('You climb a tree.')
        print('The warg eventually looses interest and wanders off')
