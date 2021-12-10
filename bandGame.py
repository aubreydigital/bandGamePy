inventory = []
currentItem = ''
playerMove = ''
gameOver = False

rooms = {
    'Lobby':{'East': 'Bar'},
    'Rooftop Bar':{'South': 'Bar', 'East': 'Stage Room', 'Item': 'Steel guitar'},
    'Bar':{'West': 'Lobby', 'North': 'Rooftop Bar', 'East': 'Bathroom', 'South': 'Basement', 'Item': 'Keyboard'},
    'Basement':{'North': 'Bar', 'East': 'Studio', 'Item': 'Drums'},
    'Stage Room':{'West': 'Rooftop Bar', 'Item': 'Microphone'},
    'Soundcheck Room':{'South': 'Bathroom', 'Item': 'Bass Guitar'},
    'Bathroom':{'North': 'Soundcheck Room', 'West': 'Bar', 'Item': 'Electric Guitar'},
    'Studio': {'West': 'Basement', 'Item': 'Record Executive'}
}
currentRoom = 'Lobby'

def showInstructions():
    print()
    print('Get The Gear®')
    print('-' * 20)
    print('Collect 6 instruments so the band can play!')
    print("Don't get caught by the Record Executive or you lose!")
    print("Move commands: South, North, East, West")
    print("Collect instruments: type yes when prompted")
    print()

showInstructions()

def playerStats(currentRoom, inventory, rooms):
    print(f'You are in the {currentRoom}')
    print('Current inventory: ', inventory)
    if 'Item' in rooms[currentRoom]:
        print('You have stumbled apon the {}'.format(rooms[currentRoom]['Item']))
        addInst = input(str('Would you like to add this item to your inventory? (yes or no) \n'))
        if addInst == 'yes':
            try:
                inventory.append(rooms[currentRoom]['Item'])
                del rooms[currentRoom]['Item']
                print('You are in the {}'.format(currentRoom))
                print('Current inventory: ', inventory)
            except KeyError:
                print()
                print('Invalid response')
                print()
        elif addInst != 'no': 
            print('Invalid entry')
            addInst = input(str('Would you like to add this item to your inventory? (yes or no) \n'))
    print('-' * 20)


def main():
    pass



while gameOver == False and len(inventory) != 6:
    playerStats(currentRoom, inventory, rooms)
    playerMove = input('Enter your move:\n')

    try:
        currentRoom = rooms[currentRoom][playerMove]
    except KeyError:
        print()
        print('Invalid move')
        print()
        continue

    if currentRoom == 'Studio':
        print()
        print('Oh no the Executives in here and you lose!')
        print()
        break
    elif len(inventory) > 5:
        gameOver == True
        print('Congratulations! You win!')
        break
        # currentRoom = 'Studio'
        # continue

    # if len(inventory) == 6:
    #     # gameOver == True
    #     break

