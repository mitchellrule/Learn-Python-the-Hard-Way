prompt = "> "

def start():
	print "You are in a dimmly lit room."
	print "There are 3 doors ahead of you,"
	print "One on your right, one on your left, and one in front of you."
	print "Which one do you choose?"

	choice = raw_input(prompt)

	if "left" in choice:
		monster_room()
	elif "right" in choice:
		puzzle_room()
	elif "forward" in choice or "front" in choice:
		key_room()
	else:
		print "What?"

def monster_room():
	print "You slowly creep into the dark room..."
	print "A huge skeleton leaps at your from the darkness!"
	print "There is a sword and a torch lying on the other side of the room."
	print "What do you do?"
	
	choice = raw_input(prompt)

	if "sword" in choice:
        print "You dive for the sword to kill the skeleton."
        dead("The skeleton stops you in your tracks.\nHe tears off your head.")
    elif "torch" in choice:
    	print "You attempt to burn the skeleton."
    	dead("Why would that ever work. He tears off your head.")
    elif "kick" in choice:
    	print "You kick that skelly hard yo!\nHe dead now lol."
    	treasure()
    else:
    	print "What?"

def puzzle_room:
	print "The room is empty and dank."
	print "There is a riddle written on the wall"
	print "What has a foot but no legs?"

	choice = raw_input(prompt)

	if "snail" in choice:
		treasure()
	else:
		print "Wrong lol."

def key_room:
    print "There's a door with a HUGE keyhole in the middle."
    print "You know how to open it."
    print "Where is the key?"

    choice = raw_input(prompt)

    if "mat" in choice:
    	print "Nice you found the key!"
    	print "It opens the door. Wow! ;^)"
        treasure()
    else:
    	print "Kek the key isn't there."

def treasure():
	print "Congrats big fella!\nYou made it to the treasure room."
	print "There's treasure in here for you."
	print "How much do you take?"

	choice = raw_input(prompt)

	if choice > 0 and choice < 100:
		print "Top kek mate!"
		exit(0)
	elif choice > 100:
		print "Jeez that's stacks!"
		exit(0)
	else:
		print "That's not a number"


def dead(how):
	print how, "You lose."
	exit(0)

start() 