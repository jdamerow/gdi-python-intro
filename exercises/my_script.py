name_input = raw_input("Let's play a game. What's your name?")
print("Hi " + name_input + "Your standing...")
direction_input = raw_input("What direction do you want to go?")
weight_input = raw_input("You chose to go " + direction_input + " and find an ogre waiting. The ogre asks you to guess its weight in pound: ")
percent10 = .1*float(weight_input)
percentStarting = float(weight_input) - percent10
percentUpperEnd = float(weight_input) + percent10
print('You tell the ogre you think he weighs somewhere between: ' + str(percentStarting) + " and " + str(percentUpperEnd))
raw_input('')
