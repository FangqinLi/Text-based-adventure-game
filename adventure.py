import sys
import json
import doctest
import os
# print(os.getcwd())

class Game:
    def __init__(self, map_filename):
        self.load_map(map_filename)
        self.current_room = self.start_room
        self.player_inventory = []

        self.commands = [
                self.go,
                self.look,
                self.get,
                self.inventory,
                self.quit,
                self.help,
                self.drop
            ]

    def load_map(self, map_filename):
        with open(map_filename, 'r') as file:
            map_data = json.load(file)

        self.rooms = {} 

        for room_data in map_data["rooms"]:
            room_name = room_data["name"]
            room_desc = room_data["desc"]
            room_exits = room_data["exits"]
            room_items = room_data.get("items", [])

            self.rooms[room_name] = {
                "name": room_name,
                "desc": room_desc,
                "exits": room_exits,
                "items": room_items
            }

        self.start_room = self.rooms[map_data["start"]]


    def get_room_by_name(self, name):
        return self.rooms[name]

    def get_current_room(self):
        return self.current_room

    def go(self, direction):
        exits = self.current_room["exits"]
        if direction in exits:
            self.current_room = self.get_room_by_name(exits[direction])
            return True
        else:
            return False

    def look(self):
        room = self.current_room
        room_name = room["name"]
        room_desc = room["desc"]
        room_exits = ", ".join(room["exits"].keys())
        room_items = ", ".join(room.get("items", []))

        if room_items:
            return f"{room_name}\n\n{room_desc}\n\nExits: {room_exits}\nItems: {room_items}"
        else:
            return f"{room_name}\n\n{room_desc}\n\nExits: {room_exits}"



    def get(self, item_name):
        if "items" in self.current_room and item_name in self.current_room["items"]:
            self.current_room["items"].remove(item_name)
            self.player_inventory.append(item_name)
            return True
        else:
            return False

    def inventory(self):
        return self.player_inventory

    def help(self, *args):
        help_text = "You can run the following commands:\n"
        for command in self.commands:
            command_name = command.__name__
            if command_name == "go" or command_name == "get" or command_name == "drop":
                help_text += f"  {command_name} ...\n" 
            else:
                help_text += f"  {command_name}\n"
        print(help_text) 


    def quit(self):
        self.should_quit = True

    def drop(self, item_name):
        if item_name in self.player_inventory:
            self.player_inventory.remove(item_name)
            self.current_room["items"].append(item_name)
            print(f"You drop the {item_name}.")
        else:
            print(f"You don't have a {item_name} to drop.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 adventure.py [map_filename]")
        sys.exit(1)

    game = Game(sys.argv[1])

    print(game.look())

    while True:
        try:
            print("What would you like to do?")
            command = input("> ").strip().lower()
        except EOFError:
            print("Use 'quit' to exit.")
            continue
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        if command == "help":
            game.help()
        else:
            command = command.split(" ", 1)
            verb = command[0]

            if verb == "go":
                if len(command) < 2:
                    print("Sorry, you need to 'go' somewhere.")
                else:
                    direction = command[1]
                    if game.go(direction):
                        print(game.look())
                    else:
                        print(f"There's no way to go {direction}.")

            elif verb == "look":
                print(game.look())

            elif verb == "get":
                if len(command) < 2:
                    print("Sorry, you need to 'get' something.")
                else:
                    item_name = command[1]
                    if game.get(item_name):
                        print(f"You pick up the {item_name}.")
                    else:
                        print(f"There's no {item_name} anywhere.")

            elif verb == "inventory":
                items = game.inventory()
                if items:
                    print("Inventory:")
                    for item in items:
                        print(" ", item)
                else:
                    print("You're not carrying anything.")

            elif verb == "drop":
                if len(command) < 2:
                    print("Sorry, you need to 'drop' something.")
                else:
                    item_name = command[1]
                    game.drop(item_name)

            elif verb == "quit":
                print("Goodbye!")
                break

            else:
                print("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
