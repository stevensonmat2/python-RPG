def showInstructions():
    print('New Quest')
    print('=========')
    print('Commands: ')
    print('To move type: "go [direction]"')
    print('To get item: "take [item]"')

def showStatus():
    print('---------------')
    print('you are in the ' + rooms[currentRoom]['name'])
    print('---------------')
    if 'item' in rooms[currentRoom]:
        print('you see a ' + rooms[currentRoom]['item'])
    print ('---------------')

inventory = []

rooms = {

          1: {"name" : "hall",
              "east" : 2,
              "south" : 3},

          2: {"name" : "bedroom",
              "west" : 1,
              "south" : 4,
              'item' : 'sword'},

          3: {"name" : "kitchen",
              "north" : 1},

          4: {"name" : "bathroom",
              "north" : 2}

        }

currentRoom = 1

showInstructions()

while True:

    showStatus()

    move = input(">enter command: ").lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('you cant go that way!')

    if move[0] == 'take':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' obtained!')
            del rooms[currentRoom]['item']
        else:
            print('you already took ' + move[1] + '!')

 # print('you are in room ' + currentRoom)
 # print('this is the ' + rooms[currentRoom]['name'])
 # move = input('>')
 # currentRoom = rooms[currentRoom][move]
 # print('you are now in room ' + currentRoom)
 # print('this is the' + rooms[currentRoom]['name'])
