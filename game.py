from random import randint

health = 100

print("\nYou're standing at the entrance of a labyrinth. You want to get to the center where the holy grail is.")
print("You can go left (type 'L'), right (type 'R'), or straight ahead (type 'S'): ")
input_value = raw_input("Enter what you want to do: ")

options = ['good', 'bad', 'nothing', 'good', 'bad']

bag = []

good = {'A fairy grants you a wish.' : 'wish', 'You find a cake.' : 'cake', 'You find a sword.' : 'sword', 'You find 100 balloons.' : '100 balloons', 'You find 1 million golden coins.' : '1 million coins'}
bad = {'A big Ogre is in your way.' : 'ogre', 'You encounter quicksand.' : 'quicksand', 'You see a big hungry bear running at you.' : 'bear', 'You see a bridge, guarded by a troll.' : 'troll' }

bad_solution = {'ogre' : {'wish' : 'You use your wish to make the ogre disappear and keep on going.', 'sword' : 'You fight the ogre with your sword. The ogre runs away and you continue your journey.'}, 'quicksand' : {'wish' : 'You wish for the quicksand to disappear and continue your journey.', '100 balloons' : 'You use the balloons to fly over the quicksand and keep on going.'}, 'bear' : {'cake' : 'You throw the cake at the bear. While the bear is eating the cake you slip by him.', 'wish' : 'You wish the bear to be friendly, pet it, and move on.'}, 'troll' : {'100 balloons' : 'You use the balloons to fly over the river and avoid dealing with the troll.', 'cake' : 'You offer the troll cake and the troll lets you pass.', '1 million coins' : 'You pay the troll 1 million golden coins to let you pass.'} }

won = False

corners_walked = 0

while(input_value != 'exit' and health > 0 and not won):
    random_nr = randint(0, (len(options) - 1))
    event = options[random_nr]
    corners_walked += 1

    if (event == 'nothing'):
        print('\nYour path is clear and you walk to the next intersection.')

    elif (event == 'good' and len(good) > 0):
        random_good = randint(0, (len(good) - 1))
        good_event = good.keys()[random_good]
        in_bag = good.pop(good_event)

        print(good_event)
        print("\nYou put a " + in_bag + " into your bag and keep on going.")
        bag.append(in_bag)

    elif (event == 'good' and len(good) <= 0):
        print("There would have been a fairy but she already left. So, no wish but no threat either.")

    elif (event == 'bad'):
        random_bad = randint(0, (len(bad) - 1))
        bad_event = bad.keys()[random_bad]
        bad_event_key = bad[bad_event]

        print(bad_event)

        is_saved = False

        if len(bag) > 0:
            print("\nYou have the following items in your bag:")
            for item in bag:
                print(item)

            selection = raw_input("Which one do you want to use? ")
            while(selection not in bag):
                selection = raw_input("You don't have that item. Please choose one that you have:")

            bag.remove(selection)

            solutions = bad_solution[bad_event_key]
            # picked solution works
            if (solutions.has_key(selection)):
                print solutions[selection]
                is_saved = True
            else:
                # picked solution does not work
                print('\nUnfortunately a ' + selection + ' does not work against ' + bad_event_key + '.')

        if not is_saved:
            health = health - 30
            if (health <= 0):
                print('\nYour health is too bad and you die.')
                break

            print('\nBadly injured you overcome the situation. You lose 30 health points and keep on moving.')
            print('Your health is: ' + str(health))

    if (corners_walked == 10):
        won = True
        break

    print("\n\nYou can go left (type 'L'), right (type 'R'), or straight ahead (type 'S'): ")
    input_value = raw_input("Enter what you want to do: ")

if won:
    print("\n\nCongratulations! You found the holy grail!")

if not won:
    print("\n\nWell, that didn't go as planned. Maybe try once more?")
