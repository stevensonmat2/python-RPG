rooms = {

          0: {"name" : "hall"}
}



items = {0: {'name': 'cobweb'},

         1:{'name': 'sword'},

         2:{'name': 'helm'},


}

enemyItems = { 0: {'name': 'great helm',
                   'defense': 2,
                   'm_value': 50},
               1: {'name': 'iron cuirass',
                   'defense': 3,
                   'm_value': 100}
                   }

enemies  = {
         0: {'name': 'mouse'},

         1: {'name': 'rat',
             'attack': 2,
             'defense': 2,
             'health': 2},

         2: {'name': 'ghoul',
             'attack': 4,
             'defense': 3,
             'health': 5},

         3: {'name': 'skeleton',
             'attack': 3,
             'defense': 3,
             'health': 4},

         }
from random import randint

firstRoom = randint(0, 3)
if firstRoom == 0:
    rooms[0]['south'] = 1
if firstRoom == 1:
    rooms[0]['north'] = 1
if firstRoom == 2:
    rooms[0]['east'] = 1
if firstRoom == 3:
    rooms[0]['west'] = 1

def showTitle():
    print('=========')
    print('you are in the ' + rooms[currentRoom]['name'])
    print('---------------')
    if 'item' in rooms[currentRoom]:
        print('you see a ' + roomItem['name'])
    print('---------------')
    if 'enemy' in rooms[currentRoom]:
        print('you see a ' + roomEnemy['name'])
    print('---------------')
    # print('you can go ' + currentRoom['east'])
#     print('SKELETON QUEST')
#     print('=========')

currentRoom = 0
lastRoom = 0
roomItem = 0
roomEnemy = 0
while True:


    showTitle()


    print(currentRoom)
    print(rooms[currentRoom])
    print(lastRoom)

    move = input('direction').lower().split()

    if move[0] in rooms[currentRoom]:
        # currentRoom = rooms[currentRoom][move[0]]


        if rooms[currentRoom][move[0]] not in rooms:

            if lastRoom > currentRoom:
            # if currentRoom not in rooms:
            # lastRoom =
                prevRoom = currentRoom
                rooms[currentRoom][move[0]] = lastRoom + 1
                currentRoom = lastRoom + 1
                # rooms[currentRoom][move[0]] = lastRoom + 1
                print(prevRoom)
                print(currentRoom)

                if move[0] == 'south':

                    rooms[currentRoom] = {'name': 'hallway',  # for lastRoom: rooms[currentRoom} + 1 = etc..
                                          'north': prevRoom}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = currentRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = currentRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = currentRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 2:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                if move[0] == 'north':
                    # rooms[currentRoom] = {'south': 'n'}
                    rooms[currentRoom] = {'name': 'hallway',  # for lastRoom: rooms[currentRoom} + 1 = etc..
                                          'south': prevRoom}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = currentRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = currentRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['north'] = currentRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 2:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                if move[0] == 'east':
                    rooms[currentRoom] = {'name': 'hallway',  # for lastRoom: rooms[currentRoom} + 1 = etc..
                                          'west': prevRoom}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = currentRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = currentRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = currentRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 2:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                if move[0] == 'west':
                    rooms[currentRoom] = {'name': 'hallway',  # for lastRoom: rooms[currentRoom} + 1 = etc..
                                          'east': prevRoom}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = currentRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = currentRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['north'] = currentRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 2:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                    print(lastRoom)
                    print(rooms[currentRoom])
                lastRoom = currentRoom

            else:

                currentRoom = rooms[currentRoom][move[0]]
                lastRoom = currentRoom
                print(lastRoom)
                if move[0] == 'south':
                    # rooms[currentRoom] = {'north': 'n'}
                    rooms[currentRoom] = {'name': 'hallway',
                                          'north': lastRoom - 1}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = lastRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = lastRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = lastRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 7:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                if move[0] == 'north':
                    # rooms[currentRoom] = {'south': 'n'}
                    rooms[currentRoom] = {'name': 'hallway',
                                          # 'south': currentRoom + 1,
                                          'south': lastRoom - 1}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = lastRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = lastRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['north'] = lastRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 7:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                if move[0] == 'east':
                    rooms[currentRoom] = {'name': 'hallway',
                                          'west': lastRoom - 1}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['north'] = lastRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['east'] = lastRoom + 1
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = lastRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 7:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']

                if move[0] == 'west':
                    rooms[currentRoom] = {'name': 'hallway',
                                          # 'south': currentRoom + 1,
                                          'east': lastRoom - 1}
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['west'] = lastRoom + 1
                        # print(rooms[currentRoom])
                        # print(rooms)
                    door_chance = randint(1, 3)
                    if door_chance == 1:
                        rooms[currentRoom]['north'] = lastRoom + 1
                    door_chance = randint(1, 1)
                    if door_chance == 1:
                        rooms[currentRoom]['south'] = lastRoom + 1
                    # #if no item yet
                    item_chance = randint(1, 10)
                    if item_chance > 7:
                        rooms[currentRoom]['item'] = items[randint(0, 2)]
                        roomItem = rooms[currentRoom]['item']
                    else:
                        roomItem = items[0]['name']
                    # if no enemy yet
                    enemy_chance = randint(1, 10)
                    if enemy_chance > 7:
                        rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                        roomEnemy = rooms[currentRoom]['enemy']
                    else:
                        roomEnemy = enemies[0]['name']
                    print(rooms[currentRoom])
                else:
                    print(rooms[currentRoom])
                    pass

        else:

            currentRoom = rooms[currentRoom][move[0]]
            print(rooms[currentRoom])

    else:
        print('cant go that way')
