
from environment import GameEnvironment

def main():
    env = GameEnvironment("../data/world_config.json")
    inventory = set()

    print("Welcome to the Adventure Game!")
    print("-------------------------------")
    print("You can check available actions with '?'")

    while not env.is_terminal():

        print(f"\n{env.get_state()}")
        action = input(">> ").strip().lower()


        # Handle picking up items
        if action == "take key" and "iron_key" not in inventory:
            if "item" in env.world["rooms"][env.current_room]:
                inventory.add(env.world["rooms"][env.current_room]["item"])
                print("You picked up the key.")

        # Handle using key
        if action == "use key":
            room_data = env.world["rooms"][env.current_room]
            if room_data.get("requires") == "iron_key" and "iron_key" in inventory:
                env.current_room = room_data["actions"]["use key"]
                print("You unlocked the door with the iron key.")
                continue
            else:
                print("You don't have the right key.")
                continue
        if action == "?":
            print(env.get_available_actions(inventory))
        else:
            # General action handler
            success = env.perform_action(action)
            if not success:
                print("You can't do that here.")

    print(f"\n{env.get_state()}")
    print("Game over.")

if __name__ == "__main__":
    main()
