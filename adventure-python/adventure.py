import sys
import random

player = {
    "room": "outside",
    "inventory": []
}

rooms = {
    "outside": {
        "title": "Outside",
        "description": "You are standing outside of a huge cave entrance.",
        "east": "castle",
        "west": "cave",
        "move possibility": "east, west",
        "items": ["key", 'torch'],
        "lock": False,  # otwarty
        "light": 'bright', # światło Zapalone domyślnie
    },
    "cave": {
        "title": "Cave",
        "description": "You're in a cave.",
        "east": "outside",
        "move possibility": "east",
        "items": ["rocks", "torch", "rope", "coins", "torch"],
        "lock": False,  # otwarty
        "light": 'dark', # światło zgaszone domyślnie
    },
    "castle": {
        "title": "Castle",
        "description": "You're getting to the castle",
        "east": "hall",
        "west": "outside",
        "north": "front room",
        "south": "dining room",
        "move possibility": "east, west, north, south",
        "items": ["sword"],
        "lock": True,  # zamknięty
        "light": 'dark', # światło zgaszone domyślnie
    },
    "front room": {
        "title": "Front room",
        "description": "You're getting to the front room in the Castle",
        "south": "castle",
        "east": "bedroom",
        "move possibility": "south, east",
        "items": ["chest", "coins", "torch"],
        "lock": True,  # zamknięty
        "light": "bright", # światło zapalone domyślnie
    },
    "hall": {
        "title": "Hall",
        "description": "You're in the Hall in the Castle",
        "west": "castle",
        "north": "bedroom",
        "move possibility": "west, north",
        "items": ["umbrella", "torch"],
        "lock": False,  # otwarty
        "light": "dark", # światło zgaszone domyślnie
    },
    "bedroom": {
        "title": "Bedroom",
        "description": "You're in main bedroom.",
        "south": "hall",
        "west": "front room",
        "move possibility": "south, west",
        "items": ["pajama", "book", "the golden cup"],
        "lock": True,  # zamknięty
        "light": "dark", # światło zgaszone domyślnie
    },
    "dining room": {
        "title": "Dining room",
        "description": "You're in beautiful, full of tables and meat, \
dining room.",
        "north": "castle",
        "move possibility": "north",
        "items": ["wine", "beer", "pizza", "prosciutto"],
        "lock": False,  # otwarty
        "light": "dark", # światło zgaszone domyślnie
    },
}

characters = {
    "wizard": {
        "name": "Merlin",
        "lines": ["Greetings, adventurer!", "Get away..."],
        "quest": False,
    },
    "king": {
        "name": "King Arthur",
        "lines": [
            "Go ahead!",
            "I'm the boss here.",
            "Give me some fine wine and whores!",
        ],
    },
}


def movement_validation(command):
    if command == "w":
        command = "west"
    elif command == "e":
        command = "east"
    elif command == "s":
        command = "south"
    elif command == "n":
        command = "north"
    return command


def character_meeting():
    char_met = random.randint(1, 10)
    if char_met == 1:
        print("You meet the king.")
        talking = input(
            f"Do you want to talk to {characters['king']['name']}? y/n: "
        ).lower()
        if talking in ["yes", "y"]:
            print(random.choice(characters["king"]["lines"]))
    elif char_met == 3 or 5:
        print("You meet the wizard!")
        talking = input(
            f"Do you want to talk to {characters['wizard']['name']}? y/n: "
        ).lower()
        if talking in ["yes", "y"]:
            if (
                "the golden cup" not in player["inventory"]
                and not characters["wizard"]["quest"]
            ):
                print(random.choice(characters["wizard"]["lines"]))
                print("Bring me the Golden Cup and you will win the game.")
                characters["wizard"]["quest"] = True
            elif "the golden cup" in player["inventory"]:
                print("OMG, where did you find it?!")
                print("You won.")
                sys.exit()
            else:
                print(random.choice(characters["wizard"]["lines"]))

def turn_light(next_position): #zapalanie światła
    if rooms[next_position]['light'] == "dark":
        if "torch" in player['inventory']:
            torch_use = input('Press t to light your torch: ').lower()
            if torch_use in ["t", "torch"]:
                print('You have light the torch, and You leave it here')
                rooms[next_position]['light'] = 'bright'
                player["inventory"].remove('torch')
        else:
            print('You have to find the torch, its dark here')
            

def movement(command):  # pokazuje możliwości ruchu
    current_position = player["room"]
   
    next_position = rooms[current_position][command]
    # check if room closed
    if rooms[next_position]["lock"]:  # czy zamknięte
        if "key" in player["inventory"]:
            player["inventory"].remove("key")
            rooms[next_position]["lock"] = False
        else:
            print("The room is closed. Find a key first.")
            return
    player["room"] = next_position
    
    turn_light(next_position) #czy zapalone światło
    if rooms[player["room"]]['light'] == "bright":
        if "key" not in player["inventory"]:
            if next_position in ["castle", "hall", "dining room", "front room"]:
                key_found = random.randint(1, 5)
                if key_found == 1:
                    player["inventory"].append("key")
                    print("You've just found a key!")
                 if key_found == 2:
                    player["inventory"].append("torch")
                    print("You've just found a torch!")
                
        character_meeting()



def main():
    print("Type 'help' for a list of commands.")
    describe_room()
    playing = True
    while playing:
        command = get_command()
        if command in ["look", "l"]:
            describe_room()
        elif command in ["quit", "q"]:
            print("Bye!")
            playing = False
        elif command in ["west", "w", "east", "e", "south", "s", "north", "n"]:
            command = movement_validation(command)
            movement(command)
        elif command in ["get", "g"] or "get" in command:
            get_items(command)
        elif command in ["inventory", "i"]:
            show_inventory()
        elif command in ["help", "h", "?"]:
            show_help()
        else:
            print(f"Unrecognized command: {command}")


def show_help():
    list_of_commands = [
        "look, l",
        rooms[player["room"]]["move possibility"],
        "get, g, get <item name>",
        "inventory, i",
        "quit, q",
    ]
    for command_option in list_of_commands:
        print(command_option)


def get_items(command):
    if rooms[player["room"]]['light'] == "bright":
        if "get " in command:
            item_to_get = command.split(" ", 1)[1]
        else:
            item_to_get = input("Get what? ").lower()
        while item_to_get not in rooms[player["room"]]["items"]:
            item_to_get = input("This item does not exists, repeat the name or q to quit: ")
            if item_to_get in ["q", 'quit']:
                break
        random_choice = random.randint(0, 1)
        if random_choice:
            player["inventory"].append(item_to_get)
            print("Taken.")
            # remove item from room
            rooms[player["room"]]["items"].remove(item_to_get)
        else:
            print("You didn't find it. Search again.")
    else:
        print('Its too dark here, You can find nothing')


def show_inventory():
    current_inventory = ", ".join(player["inventory"])
    if current_inventory:
        print(f"You are carrying: {current_inventory}")
    else:
        print("Your inventory is empty.")


def get_command():
    print()
    return input("> ").lower()


def describe_room():

    room = rooms[player["room"]]
    print()
    print(room["title"])
    print()
    print(room["description"])
    if rooms[player["room"]]['light'] == "bright":
        print(f"There are following exits: {room['move possibility']}")
        if room["items"]:
            print(f'There are following items: {", ".join(room["items"])}')
    else:
        print('Its dark here, You have to use torch')


if __name__ == "__main__":
    main()
