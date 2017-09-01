
def showTitle():
    print('=========')
    print('SKELETON QUEST')
    print('=========')

showTitle()
def showInstructions():
    # print('=========')
    # print('SKELETON QUEST')
    # print('=========')
    print('Commands: ')
    print('---------------')
    print('To move type: "go [direction]"')
    print('To get item: "take [item]"')
    print('To equip item: "equip [item]"')
    print('To use item: "use [item]"')
    print('TO drop item: "drop [item]"')
    print('To fight enemy: "fight"')
    print('To see inventory: "inv"')
    print('To see player status: "stat"')
    print('---------------')
    # print('To show map: "show [maps]"')

def showStatus():
    print('you are in the ' + rooms[currentRoom]['name'])
    if currentRoom == 0:
        print(rooms[currentRoom])
    print('---------------')
    if 'item' in rooms[currentRoom]:
        print('you see a ' + roomItem['name'])
    print('---------------')
    if 'enemy' in rooms[currentRoom]:
        currentEnemy = rooms[currentRoom]['enemy']
        # print(currentEnemy)#take out
        print('you see a ' + roomEnemy['name'])
    print('---------------')

# validcommands = ['go', 'take', 'equip', 'use', 'drop', 'fight', 'inv']

inventory = ['sword', 'cap', 'robe', 'potion', 'noweap']



# # weapons should do different damage to different enemy types

allItems = {

#0 = weapons, 1 = helms, 2 = armor, 3 = items
0 : {
         0: {'name': 'noweap',
                   'defense': 0,
                   'attack': 0},
         1 : {'name': 'sword',
                    'attack': 2},
         2 : {'name': 'mace',
                    'attack': 3},

},

1 : {
         0: {'name': 'nohelm',
                   'defense': 1,
                   'attack': 0},
         1: {'name': 'helm',
                  'defense': 2},
         2: {'name': 'cap',
                    'defense': 1},

},

2 : {
         0: {'name': 'noarm',
                   'defense': 1,
                   'attack': 0},
         1: {'name': 'cuirass',
                  'defense': 2},
         2: {'name': 'robe',
                     'defense': 0},

},

3 : {
         1: {'name': 'potion',
                    'restore': 4},
         2: {'name': 'book'},

             },

4 : {
         1: {'name': 'potion',
                    'restore': 4},
         2: {'name': 'book'},

             },
}

enemies = {
           1: {
                        'ran_num': 1,
                        'name': 'skeleton',
                        'type': 'skeleton',
                        'health': 4,
                        'attack': 3,
                        'item': 'potion'},
           2: {         'ran_num': 2,
                        'name': 'ghoul',
                        'type': 'ghoul',
                        'health': 5,
                        'attack': 4,
                        'item': 'cuirass'},
           3: {'name': 'giant skeleton',
                              'type': 'skeleton',
                              'health': 8,
                              'attack': 5,
                              'item': 'helm'},

          }
#
# rooms = {
#
#           1: {"name" : "hall",
#               "east" : 2,
#               "north" : 5,
#               "south" : 3},
#
#           2: {"name" : "bedroom",
#               "west" : 1,
#               "south" : 4,
#               'item' : 'sword'},
#
#           3: {"name" : "kitchen",
#               "north" : 1},
#
#           4: {"name" : "bathroom",
#               "north" : 2,
#               "enemy" : "ghoul"},
#
#           5: {"name" : "dungeon",
#               "south" : 1,
#               "north" : 6,
#               "enemy" : "skeleton"},
#
#           6: {"name" : "lair",
#               "south" : 5,
#               "east" : 7,
#               "enemy" : "giant skeleton"}
#
#         }

rooms = {

          0: {"name" : "hall"}
}


#
# items = {0: {'name': 'cobweb'},
#
#          1:{'name': 'sword'},
#
#          2:{'name': 'helm'},
#
#
# }

enemyItems = { 0: {'name': 'great helm',
                   'defense': 2,
                   'm_value': 50},
               1: {'name': 'iron cuirass',
                   'defense': 3,
                   'm_value': 100}
                   }
#
# enemies  = {
#          0: {'name': 'mouse'},
#
#          1: {'name': 'rat',
#              'attack': 2,
#              'defense': 2,
#              'health': 2},
#
#          2: {'name': 'ghoul',
#              'attack': 4,
#              'defense': 3,
#              'health': 5},
#
#          3: {'name': 'skeleton',
#              'attack': 3,
#              'defense': 3,
#              'health': 4},
#
#          }
currentRoom = 0
currentEnemy = 'n'
currentWeap = 'sword'
currentArm = 'noarm'
currentHelm = 'nohelm'
currentSpell = 'n'
currentItem = 'n'

playerDef = 1
playerHealthMax = 8
playerHealthNow = 8
playerHealthCurr = 8
enemyHealthNow = 1
enemyHealth = 1
enemyHealthCurr = 0

# currentRoom = 0
lastRoom = 0
roomItem = 0
roomEnemy = 0

# print(weapons.values())

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

showInstructions()

while True:

    showStatus()


    # print(playerDef)
    # print(currentHelm)


    move = input(">enter command: ").lower().split()

    if move[0] == 'com':
        print(showInstructions())

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            # currentRoom = rooms[currentRoom][move[0]]


            if rooms[currentRoom][move[1]] not in rooms:

                if lastRoom > currentRoom:
                    # if currentRoom not in rooms:
                    # lastRoom =
                    prevRoom = currentRoom
                    rooms[currentRoom][move[1]] = lastRoom + 1
                    currentRoom = lastRoom + 1
                    # rooms[currentRoom][move[0]] = lastRoom + 1
                    print(prevRoom)
                    print(currentRoom)

                    if move[1] == 'south':

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
                            rooms[currentRoom]['item'] = allItems[randint(0, 4)][randint(1, 2)]
                            roomItem = rooms[currentRoom]['item']
                        # else:
                        #     roomItem = items[0]['name']
                        # if no enemy yet
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 2:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # else:
                        #     roomEnemy = enemies[0]['name']
                    if move[1] == 'north':
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
                            rooms[currentRoom]['item'] = allItems[randint(0, 4)][randint(1, 2)]
                            roomItem = rooms[currentRoom]['item']
                        # else:
                        #     roomItem = items[0]['name']
                        # if no enemy yet
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 2:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # else:
                        #     roomEnemy = enemies[0]['name']
                    if move[1] == 'east':
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
                            rooms[currentRoom]['item'] = allItems[randint(0, 4)][randint(1, 2)]
                            roomItem = rooms[currentRoom]['item']
                        # else:
                        #     roomItem = items[0]['name']
                        # if no enemy yet
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 2:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # else:
                        #     roomEnemy = enemies[0]['name']
                    if move[1] == 'west':
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
                            rooms[currentRoom]['item'] = allItems[randint(0, 4)][randint(1, 2)]
                            roomItem = rooms[currentRoom]['item']
                        # else:
                        #     roomItem = items[0]['name']
                        # if no enemy yet
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 2:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # else:
                        #     roomEnemy = enemies[0]['name']
                        print(lastRoom)
                        print(rooms[currentRoom])
                    lastRoom = currentRoom

                else:

                    currentRoom = rooms[currentRoom][move[1]]
                    lastRoom = currentRoom
                    print(lastRoom)
                    if move[1] == 'south':
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
                            rooms[currentRoom]['item'] = allItems[randint(0, 4)][randint(1, 2)]
                            roomItem = rooms[currentRoom]['item']
                        # else:
                        #     roomItem = items[0]['name']
                        # if no enemy yet
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 7:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # else:
                        #     roomEnemy = enemies[0]['name']
                    if move[1] == 'north':
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
                            rooms[currentRoom]['item'] = allItems[randint(0, 4)][randint(1, 2)]
                            roomItem = rooms[currentRoom]['item']
                        # else:
                        #     roomItem = items[0]['name']
                        # if no enemy yet
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 7:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # else:
                        #     roomEnemy = enemies[0]['name']
                    if move[1] == 'east':
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
                            rooms[currentRoom]['item'] = allItems[randint(0, 4)][randint(1, 2)]
                            roomItem = rooms[currentRoom]['item']
                        # else:
                        #     roomItem = items[0]['name']
                        # if no enemy yet
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 7:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # else:
                        #     roomEnemy = enemies[0]['name']

                    if move[1] == 'west':
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
                            rooms[currentRoom]['item'] = allItems[randint(0, 4)][randint(1, 2)]
                            roomItem = rooms[currentRoom]['item']
                        # else:
                        #     roomItem = items[0]['name']
                        # if no enemy yet
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 7:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # else:
                        #     roomEnemy = enemies[0]['name']
                        print(rooms[currentRoom])
                    else:
                        print(rooms[currentRoom])
                        pass

            else:

                currentRoom = rooms[currentRoom][move[1]]
                print(rooms[currentRoom])

        else:
            print('cant go that way')

    if move[0] == 'inv':
        print('---------------')
        print('Inventory: ' + str(inventory))
        print('---------------')
        query = input('type "[item]" for details or any key to exit: ')
        if query in inventory:
            type = range(len(allItems.keys()))

            # scan = allItems[0].keys()
            for x in type:
                scan = allItems[x].keys()
                for i in scan:
                    if query in allItems[x][i]['name']:
                        print('---------------')
                        read = allItems[x][i].items()
                        for pair in read:
                            print('{}: {}'.format(pair[0], pair[1]))
                            # print(pair)#('{} {}'.format(pair))
                        # print('{} {}'.format('name', 'cap'))
                        # print(allItems[x][i]['name'], allItems[x][i])


                # if query in allItems[2]:
                #     print('---------------')
                #     print(allItems[2][query])
                # if query in allItems[3]:
                #     print('---------------')
                #     print(allItems[3][query])
        # else:
        #     pass
        #     print('---------------')

    if move[0] == 'take':
        # if move[1] == roomItem['name']:
        if move[1] in rooms[currentRoom]['item']['name']:
            inventory.append(roomItem['name'])
            print('---------------')
            print(move[1] + ' obtained!')
            print('---------------')
            print(roomItem)
            # roomItem =
            del rooms[currentRoom]['item']
            roomItem = 0



            # inventory[item] = item
        else:
            print('---------------')
            print('there is no ' + move[1] + '!')
            print('---------------')

    if move[0] == 'drop':
        if move[1] in items or weapons or helms:
            if move[1] in inventory:
                rooms[currentRoom]['item'] = move[1]
                inventory.remove(move[1])
                print('---------------')
                print('Inventory:', inventory)
                print('---------------')
                if move[1] == currentWeap:
                    currentWeap = 'none'
                if move[1] == currentHelm:
                    currentHelm = 'nohelm'
                    playerDef = helms[currentHelm]['defense'] + armor[currentArm]['defense']
                if move[1] == currentArm:
                    currentArm = 'noarm'
                    playerDef = helms[currentHelm]['defense'] + armor[currentArm]['defense']
            else:
                print('---------------')
                print('you dont have that it')
                print('---------------')
        else:
            print('---------------')
            print('that aint real!')
            print('---------------')
    # else:
    #     print('---------------')
    #     print('there is no ' + move[1] + '!')
    #     print('---------------')
    # if move[0] == 'show' and move[1] == 'inventory':
    #     print('Inventory = ' + str(inventory))

    if move[0] == 'equip':
        if move[1] in inventory:
            if move[1] in weapons:
                currentWeap = move[1]
                print('---------------')
                print(currentWeap + ' equipped!')
                print('---------------')
            if move[1] in helms:
                currentHelm = move[1]
                playerDef = helms[currentHelm]['defense'] + armor[currentArm]['defense']
                print('---------------')
                print(currentHelm + ' equipped!')
                print('---------------')
                print(currentHelm)
                #add ARMOR SECTION
        elif move[1] not in weapons or helms or items:
            print('---------------')
            print('that aint real')
            print('---------------')
        else:
            print('---------------')
            print('you dont have that item')
            print('---------------')

    if move[0] == 'use':
        if move[1] in inventory:
            if move[1] in items:
                currentItem = move[1]
                if playerHealthNow < playerHealthMax:
                    healAmnt = items[currentItem]['restore']
                    playerHealthNow = playerHealthNow + healAmnt
                    if playerHealthNow > playerHealthMax:
                        playerHealthNow = playerHealthNow - (playerHealthNow - playerHealthMax)
                    inventory.remove(move[1])
                    print('---------------')
                    print(move[1] + ' used!')
                    print('---------------')
                    print('HP = ', playerHealthNow)
                    print('---------------')
                else:
                    print('your health is full')
                    # del inventory[currentItem]
            else:
                print('you cant use that')
        else:
            print('you dont have that')

    if move[0] == 'fight':
        print('---------------')
        if 'enemy' in rooms[currentRoom]:

            currentEnemy = rooms[currentRoom]['enemy']
            # print(enemyHealth)#take out
            if 'enemy' in rooms[currentRoom] and currentWeap != 'noweap':
                # print('you hit ' + rooms[currentRoom]['enemy'] + ' with ' + str(currentWeap))
                print('you hit ' + str(roomEnemy['name']) + ' with ' + str(currentWeap))

                enemyHealth = roomEnemy['health']
                # enemyHealth = enemies[currentEnemy]['health']
                enemyHealthNow = enemyHealth - allItems[0][currentWeap]['attack']
                enemyHealthRem = enemyHealth - enemyHealthNow
                enemyHealthCurr = enemyHealthCurr + enemyHealthRem
                enemyHealthFin = enemyHealth - enemyHealthCurr
                print('---------------')
                print('enemy HP = ' + str(enemyHealthFin))
                print('---------------')
            else:
                print('***************')
                print('NO WEAPON EQUIPPED')
                print('***************')
                continue
                # print(enemyHealth)
            if enemyHealthFin <= 0:
                print(rooms[currentRoom]['enemy'] + ' slain!')
                print('---------------')
                rooms[currentRoom]['item'] = enemies[currentEnemy]['item']
                print(rooms[currentRoom]['enemy'] + ' dropped ' + enemies[currentEnemy]['item'])
                print('---------------')
                del rooms[currentRoom]['enemy']
                enemyHealthCurr = 0
                    # print(rooms[currentRoom]['enemy'] + ' slain!')

            else:
                print('---------------')
                print(rooms[currentRoom]['enemy'] + ' fights back!')
                print('---------------')
                playerHealthCurr = playerHealthNow - (enemies[currentEnemy]['attack'] - playerDef)
                playerHealthNow = playerHealthCurr
                print('---------------')
                print('player HP = ' + str(playerHealthNow))
                print('---------------')
                # enemyHealthCurr = enemyHealthNow
                # query = input('Hit Again? (y/n): ')
                # print('---------------')
                #
                # if query == 'y':
                #     enemyHealth = enemyHealth - items[currentWeap]['attack']
                #     if enemyHealth == 0:
                #         print(rooms[currentRoom]['enemy'] + ' slain!')
                #         print('---------------')
                #         rooms[currentRoom]['item'] = enemies[currentEnemy]['item']
                #         print('---------------')
                #         print(enemies[currentEnemy]['item'])
                #         print('---------------')
                #         del rooms[currentRoom]['enemy']
                #         print('---------------')
                #     else:
                #         continue
                # if query == 'n':
                #     print('run away!')


        else:
            print('---------------')
            print('nothing to fight here')
            print('---------------')# else:

    if playerHealthNow <= 0:
        print('You died! Game over, man! Game over!')
        print('---------------')
        break

    if move[0] == 'stat':
        print('---------------')
        print('HP = ' + str(playerHealthNow) + '/' + str(playerHealthMax))
        print('Equipped Weapon: ' + weapons[currentWeap]['name'])
        print('---------------')
        print('Equipped Helm: ' + helms[currentHelm]['name'])
        print('---------------')
        print('Equipped Armor: ' + armor[currentArm]['name'])
        print('---------------')

    # else:
    #     continue
        # query = input('play again? y/n: ')
        # if query == 'y':
        #     continue
        # elif query == 'n':
        #     break
    # else:
    #     print('please enter valid command')