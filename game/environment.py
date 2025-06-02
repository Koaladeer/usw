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

    def is_terminal(self):
        return self.world["rooms"][self.current_room].get("terminal", False)
