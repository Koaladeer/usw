import json


class GameEnvironment:
    def __init__(self, config_file="data/world_config.json"):
        with open(config_file) as f:
            self.world = json.load(f)
        self.current_room = self.world["start"]

    def get_state(self):
        return self.world["rooms"][self.current_room]["description"]

    def perform_action(self, action):
        valid = self.world["rooms"][self.current_room].get("actions", {})
        if action in valid:
            self.current_room = valid[action]
            return True
        return False

    def get_available_actions(self, inventory):
        room = self.world["rooms"][self.current_room]
        actions = list(room.get("actions", {}).keys())

        # Include 'take key' if an item is present and not in inventory
        if "item" in room and room["item"] not in inventory:
            actions.append("take key")

        # Include 'use key' if the room requires a key and player has it
        if room.get("requires") == "iron_key" and "iron_key" in inventory:
            actions.append("use key")

        return actions
    def is_terminal(self):
        return self.world["rooms"][self.current_room].get("terminal", False)
