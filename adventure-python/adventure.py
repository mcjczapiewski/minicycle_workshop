import random

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
        "move possibility": "east, west",
        "items": ["key"]
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
        "east": "outside",
        "move possibility": "east",
        "items": ["rocks", "torch", "rope", "coins"]
    },
    "castle":{
        "title": "Castle",
        "description": "You're getting to the castle",
        "east": "hall",
        "west": "outside",
        "north": "front room",
        "move possibility": "east, west, north",
        "items": ["sword"]
    },
    "front room":{
        "title": "Front room",
        "description": "You're getting to the front room in the Castle",
        "south": "castle",
        "move possibility": "south",
        "items": ["chest", "coins"]
    },
    "hall":{
        "title": "Hall",
        "description": "You're in the Hall in the Castle",
        "west": "castle",
        "move possibility": "west",
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
    print("Type 'help' for a list of commands.")
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
        elif command in ['inventory', 'i']:
            show_inventory()
        elif command in ['help', 'h', '?']:
            show_help()
        else:
            print(f'Unrecognized command: {command}')


def show_help():
    list_of_commands = [
        'look, l',
        rooms[player['room']]['move possibility'],
        'get, g, get <item name>',
        'inventory, i',
        'quit, q'
    ]
    for command_option in list_of_commands:
        print(command_option)


def get_items(command):
    if 'get ' in command:
        item_to_get = command.split(' ', 1)[1]
    else:
        item_to_get = input('Get what? ').lower()
    
    random_choice = random.randint(0,1)
    if random_choice:       
        player["inventory"].append(item_to_get)
        print("Taken.")
        # remove item from room
        rooms[player['room']]['items'].remove(item_to_get)
    else:
        print("You didn't find it. Search again.")


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
    print(f"There are following exits: {room['move possibility']}")
    if room['items']:
        print(f'There are following items: {", ".join(room["items"])}')


if __name__ == '__main__':
    main()
