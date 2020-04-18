

player = {
    'room': 'outside',
    'inventory': []
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance.",
        "east": "castle",
        "west": "cave",
        "move posibility": "There are following exits: east, west",
        "items": ["key"]
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
        "east": "outside",
        "move posibility": "There are following exits: east",
        "items": ["rocks", "torch", "rope", "coins"]
    },
    "castle":{
        "title": "Castle",
        "description": "You're getting to the castle",
        "east": "hall",
        "west": "outside",
        "north": "front room",
        "move posibility": "There are following exits: east, west, north",
        "items": ["sword"]
    },
    "front room":{
        "title": "Front room",
        "description": "You're getting to the front room in the Castle",
        "south": "castle",
        "move posibility": "There are following exits: south",
        "items": ["chest", "coins"]
    },
    "hall":{
        "title": "Hall",
        "description": "You're in the Hall in the Castle",
        "west": "castle",
        "move posibility": "There are following exits: west",
        "items": ["key"]
    }

}

def movement_validation(command):
    if command == 'w':
        command = 'west'
    elif command == 'e':
        command = 'east'
    elif command == 's':
        command = 'south'
    elif command == 'n':
        command = 'north'
    return command


def movement(command): #pokazuje możliwości ruchu
    current_position = player['room']
    next_position = rooms[current_position][command]
    player['room'] = next_position

def main():
    describe_room()
    playing = True
    while playing:
        command = get_command()
        if command in ['look', 'l']:
            describe_room()
        elif command in ['quit', 'q']:
            print('Bye!')
            playing = False
        elif command in ['west', 'w', 'east', 'e', 'south', 's', 'north', 'n']:
            command = movement_validation(command)
            movement(command)
            describe_room()
        elif command in ['get', 'g'] or 'get' in command:
            get_items(command)
        elif command in ['info', 'i']:
            show_inventory()
        else:
            print(f'Unrecognized command: {command}')


def get_items(command):
    if 'get ' in command:
        item_to_get = command.split(' ', 1)[1]
    else:
        item_to_get = input('Get what? ').lower()
    player["inventory"].append(item_to_get)
    print("Taken.")
    # remove item from room
    rooms[player['room']]['items'].remove(item_to_get)


def show_inventory():
    current_inventory = ", ".join(player['inventory'])
    if current_inventory:
        print(f'You are carrying: {current_inventory}')
    else:
        print('Your inventory is empty.')


def get_command():
    print()
    return input('> ').lower()


def describe_room():
    room = rooms[player['room']]
    print()
    print(room['title'])
    print()
    print(room['description'])
    print(room['move posibility'])
    if room['items']:
        print(f'There are following items: {", ".join(room["items"])}')


if __name__ == '__main__':
    main()
