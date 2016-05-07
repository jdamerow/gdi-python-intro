from random import randint

items = {
    'sword':'ogre',
    'cake':'wolf',
    'balloons':'bees',
    'kitty':'troll',
}

def does_item_protect(obstacle, item):
    # Your code goes here.
    # Your code should do something with the obstacle and item variables and assign the value to a variable for returning
    # You could use two dictionaries to assign what happens when a certain item does or does not protect agains an obstacle.

    return items[item] == obstacle


input_obstacle = raw_input("You encounter: ")
while input_obstacle not in items.values():
    input_obstacle = raw_input("That's not real. What do you really encounter? ")

input_item = raw_input("You have a: ")
while input_item not in items.keys():
    input_item = raw_input("That doesn't exist. What do you defend yourself with? ")

protected = does_item_protect(input_obstacle, input_item)
# Display the answer in some meaningful way
print("you are protected is " + str(protected))
