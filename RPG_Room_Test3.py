from random import randint

def showTitle():
    print('=========')
    print('SKELETON QUEST')
    print('=========')

showTitle()


# name = input('What is your name? ')


def showInstructions():
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
    # print('---------------')
    # print('To show map: "show [maps]"')

def showStatus():
    print('===============')
    print('you are in the ' + rooms[currentRoom]['name'])
    print('---------------')
    if 'south' in rooms[currentRoom]:
        if 'north' == lastMove:
            print('you came from the south')
        else:
            print('you can go south')
    if 'north' in rooms[currentRoom]:
        if 'south' == lastMove:
            print('you came from the north')
        else:
            print('you can go north')
    if 'east' in rooms[currentRoom]:
        if 'west' == lastMove:
            print('you came from the east')
        else:
            print('you can go east')
    if 'west' in rooms[currentRoom]:
        if 'east' == lastMove:
            print('you came from the west')
        else:
            print('you can go west')
    # print(rooms[currentRoom])
    # print(roomItems)
    print('---------------')

    if 'items' in rooms[currentRoom]:
        for i in roomItems:
            print("you see a " + i['name'])

            print('---------------')

    if roomEnemy != 0:
        if 'enemy' in rooms[currentRoom]:
            # currentEnemy = rooms[currentRoom]['enemy']
            print('you see a ' + roomEnemy['name'])
            print('---------------')

def drop_item(dropped):
    if dropped in inventory:
        print({dropped}, 'dropped!')
        roomItems.append(dropped)
        rooms[currentRoom]['items'] = roomItems
        print(roomItems)
        inventory.remove(dropped)



inventory = ['sword', 'cap', 'robe', 'potion', 'mace', 'warhammer']

roomItems = [0]



# # weapons should do different damage to different enemy types

allItems = {

#0 = weapons, 1 = helms, 2 = armor, 3 = items
0 : {
         0: {'name': 'noweap',
                   'defense': 0,
                   'attack': 0},
         1 : {'name': 'sword',
                    'attack': 3},
         2 : {'name': 'mace',
                    'attack': 4},
         3 : {'name': 'warhammer',
                    'attack': 5},
},

1 : {
         0: {'name': 'nohelm',
                   'defense': 1,
                   'attack': 0},
         1: {'name': 'helm',
                  'defense': 2},
         2: {'name': 'cap',
                    'defense': 1},
         2: {'name': 'Barbute',
                    'defense': 4},
},

2 : {
         0: {'name': 'noarm',
                   'defense': 1,
                   'attack': 0},
         1: {'name': 'cuirass',
                  'defense': 4},
         2: {'name': 'robe',
                     'defense': 1},

},

3 : {
         1: {'name': 'potion',
                    'restore': 4},
         2: {'name': 'book'},

             },

4 : {
      1: {'name': 'mug'},
      2: {'name': 'fork'},

          },
}

enemies = {
           1: {
                        'name': 'skeleton',
                        'type': 'skeleton',
                        'health': 8,
                        'attack': 0 + randint(6, 7),
                        'item': 'potion'},
           2: {
                        'name': 'ghoul',
                        'type': 'ghoul',
                        'health': 10,
                        'attack': 0 + randint(5, 8),
                        'item': 'cuirass'},

       3: {             'name': 'giant skeleton',
                        'type': 'skeleton',
                        'health': 16,
                        'attack': 0 + randint(7, 10),
                        'item': 'great helm'},

          }
#

rooms = {

          0: {"name" : "hall"}
}




enemyItems = { 0: {'name': 'great helm',
                   'defense': 2,
                   'm_value': 50},
               1: {'name': 'iron cuirass',
                   'defense': 3,
                   'm_value': 100}
                   }
lastMove = 'n'
currentRoom = 0
currentEnemy = 'n'
currentWeap = {'name': 'sword',
                    'attack': 3}
currentArm = {'name': 'none',
                    'defense': 3}
currentHelm = {'name': 'none',
                    'defense': 0}
currentSpell = 'n'
currentItem = 'n'

playerAttk = 5 + int(currentWeap['attack'])
playerDef = 0 + (currentArm['defense'] + currentHelm['defense'])
playerHealthMax = 20
playerHealthNow = 20
playerHealthCurr = 20
enemyHealthNow = 1
enemyHealth = 1
enemyHealthCurr = 0

lastRoom = 0
roomItem = 0
roomEnemy = 0
roomItems = []

allWeapons = allItems[0]

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


    move = input(">enter command: ").lower().split()

    if move[0] == 'com':
        print(showInstructions())

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            if rooms[currentRoom][move[1]] not in rooms:
                if lastRoom > currentRoom:
                    lastMove = move[1]
                    prevRoom = currentRoom
                    rooms[currentRoom][move[1]] = lastRoom + 1
                    currentRoom = lastRoom + 1
                    roomEnemy = []
                    roomItem = []
                    if move[1] == 'south':
                        rooms[currentRoom] = {'name': 'hallway',
                                              'north': prevRoom}
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['east'] = currentRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['west'] = currentRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['south'] = currentRoom + 1
                        item_chance = randint(1, 10)
                        if item_chance > 0:
                            roomItems.append(allItems[randint(0, 3)][randint(1,2)])
                            rooms[currentRoom]['items'] = roomItems
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 0:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                    if move[1] == 'north':
                        rooms[currentRoom] = {'name': 'hallway',
                                              'south': prevRoom}
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['east'] = currentRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['west'] = currentRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['north'] = currentRoom + 1
                        item_chance = randint(1, 10)
                        if item_chance > 7:
                            roomItems.append(allItems[randint(0, 3)][randint(1, 2)])
                            rooms[currentRoom]['items'] = roomItems
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 2:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                    if move[1] == 'east':
                        rooms[currentRoom] = {'name': 'hallway',
                                              'west': prevRoom}
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['east'] = currentRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['south'] = currentRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['east'] = currentRoom + 1
                        item_chance = randint(1, 10)
                        if item_chance > 7:
                            roomItems.append(allItems[randint(0, 3)][randint(1, 2)])
                            rooms[currentRoom]['items'] = roomItems
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 2:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                    if move[1] == 'west':
                        rooms[currentRoom] = {'name': 'hallway',
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
                        item_chance = randint(1, 10)
                        if item_chance > 7:
                            roomItems.append(allItems[randint(0, 3)][randint(1, 2)])
                            rooms[currentRoom]['items'] = roomItems
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 2:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # print(lastRoom)
                        # print(rooms[currentRoom])
                    lastRoom = currentRoom

                else:
                    lastMove = move[1]
                    currentRoom = rooms[currentRoom][move[1]]
                    lastRoom = currentRoom
                    # print(lastRoom)
                    # print(currentRoom)
                    roomItems = []
                    roomEnemy = []
                    if move[1] == 'south':
                        rooms[currentRoom] = {'name': 'hallway',
                                              'north': lastRoom - 1}
                        door_chance = randint(1, 3)
                        if door_chance == 1 or 2:
                            rooms[currentRoom]['east'] = lastRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1 or 2:
                            rooms[currentRoom]['west'] = lastRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1 or 2:
                            rooms[currentRoom]['south'] = lastRoom + 1
                        item_chance = randint(1, 10)
                        if item_chance > 7:
                            roomItems.append(allItems[randint(0, 3)][randint(1, 2)])
                            rooms[currentRoom]['items'] = roomItems
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 4:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                    if move[1] == 'north':
                        rooms[currentRoom] = {'name': 'hallway',
                                              'south': lastRoom - 1}
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['east'] = lastRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['west'] = lastRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['north'] = lastRoom + 1
                        item_chance = randint(1, 10)
                        if item_chance > 7:
                            roomItems.append(allItems[randint(0, 3)][randint(1, 2)])
                            rooms[currentRoom]['items'] = roomItems
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 4:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                    if move[1] == 'east':
                        rooms[currentRoom] = {'name': 'hallway',
                                              'west': lastRoom - 1}
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['north'] = lastRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['east'] = lastRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['south'] = lastRoom + 1
                        item_chance = randint(1, 10)
                        if item_chance > 7:
                            roomItems.append(allItems[randint(0, 4)][randint(1, 2)])
                        enemy_chance = randint(1, 10)
                        rooms[currentRoom]['items'] = roomItems
                        if enemy_chance > 4:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                    if move[1] == 'west':
                        rooms[currentRoom] = {'name': 'hallway',
                                              'east': lastRoom - 1}
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['west'] = lastRoom + 1
                        door_chance = randint(1, 3)
                        if door_chance == 1:
                            rooms[currentRoom]['north'] = lastRoom + 1
                        door_chance = randint(1, 1)
                        if door_chance == 1:
                            rooms[currentRoom]['south'] = lastRoom + 1
                        item_chance = randint(1, 10)
                        if item_chance > 7:
                            roomItems.append(allItems[randint(0, 3)][randint(1, 2)])
                            rooms[currentRoom]['items'] = roomItems
                        enemy_chance = randint(1, 10)
                        if enemy_chance > 4:
                            rooms[currentRoom]['enemy'] = enemies[randint(1, 3)]
                            roomEnemy = rooms[currentRoom]['enemy']
                        # print(rooms[currentRoom])
                    else:
                        # print(rooms[currentRoom])
                        pass

            else:
                if 'item' in rooms[currentRoom]:
                    roomItems = rooms[currentRoom]['items']
                if 'enemy' in rooms[currentRoom]:
                    roomEnemy = rooms[currentRoom]['enemy']
                currentRoom = rooms[currentRoom][move[1]]
                # print(rooms[currentRoom])

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


    if move[0] == 'take':
        # if move[1] in roomItems:
        for key in allItems:
            check = allItems[key]
            for item in check:

                if allItems[key][item]['name'] == move[1]:

                    roomItems.remove(allItems[key][item])
                    rooms[currentRoom]['items'] = roomItems
                    inventory.append(move[1])
                    print(move[1] + ' obtained!')

    if move[0] == 'drop':
        # print(allItems)
        for key in allItems:
            check = allItems[key]
            for item in check:

                if allItems[key][item]['name'] == move[1]:

                    roomItems.append(allItems[key][item])
                    rooms[currentRoom]['items'] = roomItems
                    inventory.remove(move[1])
                    print(allItems[key][item]['name'])
                    # print(currentWeap)
                #     # print(inventory)
                if allItems[key][item]['name'] == currentWeap['name']:
                    currentWeap = {'name': 'none',
                                   'attack': 0}
                    print(currentWeap)
                    break

                if allItems[key][item]['name'] == currentArm['name']:
                    currentArm = {'name': 'none',
                                   'defense': 0}
                    print(currentWeap)
                    break

                if allItems[key][item]['name'] == currentHelm['name']:
                    currentHelm = {'name': 'none',
                                   'defense': 0}
                    print(currentWeap)
                    break


    if move[0] == 'equip':
        if move[1] in inventory:
            for key in allItems:
                check = allItems[key]
                for item in check:
                    # print(allItems[0])
                    # print(allItems[key][item])
                    # if allItems[key][item]['name'] in allItems[0]:

                    if allItems[key][item]['name'] == move[1]:
                        # print('weapons')
                        # print(allItems[key][item])
                        currentWeap = allItems[key][item]
                        playerAttk = 5 + int(currentWeap['attack'])
                        # print(currentWeap['attack'])
                        print('---------------')
                        print(move[1] + ' equipped!')


        # else:
        #     print('---------------')
        #     print('you dont have that item')
        #     print('---------------')


    if move[0] == 'use':
        if move[1] in inventory:
            for key in allItems:
                check = allItems[key]
                for item in check:

                    if allItems[key][item]['name'] == move[1]:

                        currentItem = allItems[key][item]
                        if playerHealthNow < playerHealthMax:
                            healAmnt = currentItem['restore']
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
                # else:
                #     print('you cant use that')
        else:
            print('you dont have that')

    if move[0] == 'fight':
        print('---------------')
        fighting = True
        while fighting == True:
            if 'enemy' in rooms[currentRoom]:

                currentEnemy = rooms[currentRoom]['enemy']
                if 'enemy' in rooms[currentRoom] and currentWeap['name'] != 'none':

                    # print('you hit ' + str(roomEnemy['name']) + ' with ' + str(currentWeap['name']) + ' for ' + str(weaponAtk))

                    enemyHealth = roomEnemy['health']
                    attackChance = randint(0, 3)
                    weaponAtk = playerAttk - attackChance
                    if attackChance == 0:
                        print('you got a critical hit!')
                    if attackChance == 3:
                        print('you got a close hit!')
                    print('you hit ' + str(roomEnemy['name']) + ' with ' + str(currentWeap['name']) + ' for ' + str(
                        weaponAtk) + ' damage!')
                    enemyHealthNow = enemyHealth - weaponAtk
                    enemyHealthRem = enemyHealth - enemyHealthNow
                    enemyHealthCurr = enemyHealthCurr + enemyHealthRem
                    enemyHealthFin = enemyHealth - enemyHealthCurr
                    # print(weaponAtk)
                    print('---------------')
                    if enemyHealthFin < 0:
                        enemyHealthFin = 0
                    print('enemy HP = ' + str(enemyHealthFin))
                    print('---------------')
                else:
                    print('***************')
                    print('NO WEAPON EQUIPPED')
                    print('***************')
                    break

                if enemyHealthFin <= 0:
                    print(roomEnemy['name'] + ' slain!')
                    print('---------------')
                    fighting = False

                    roomItems.append(allItems[randint(0, 3)][randint(1, 2)])
                    droppedItem = roomItems[-1]
                    rooms[currentRoom]['items'] = roomItems

                    print(roomEnemy['name'] + ' dropped ' + (droppedItem['name']))
                    print('---------------')
                    del rooms[currentRoom]['enemy']
                    enemyHealthCurr = 0
                    roomEnemy = 0

                else:
                    print('---------------')
                    print(roomEnemy['name'] + ' fights back for ' + str(roomEnemy['attack']))
                    print(roomEnemy['attack'])
                    print('---------------')
                    playerHealthCurr = playerHealthNow - (roomEnemy['attack'] - playerDef)
                    playerHealthNow = playerHealthCurr
                    print('---------------')
                    print('player HP = ' + str(playerHealthNow))
                    print('---------------')
                    if playerHealthNow <= 0:
                        break
                    query = input('Hit Again? (y/n): ')
                    print('---------------')

                    if query == 'y':
                        continue
                    elif query == 'n':
                        fighting = False

            else:
                print('---------------')
                print('nothing to fight here')
                print('---------------')

    if playerHealthNow <= 0:
        print('You died! Game over, man! Game over!')
        print('---------------')
        break

    if move[0] == 'stat':
        print(playerAttk)
        print('---------------')
        # print(name)
        print('HP = ' + str(playerHealthNow) + '/' + str(playerHealthMax))
        print('Attack rating: ' + str(playerAttk))
        print('Defense rating: ' + str(playerDef))
        print('Equipped Weapon: ' + currentWeap['name'].title() + ', Attack: ' + str(currentWeap['attack']))
        print('Equipped Helmet: ' + currentHelm['name'])
        print('Equipped Armor: ' + currentArm['name'])
        print('---------------')

