#!/usr/bin/env python3
"""
Lantern Lighthouse - A Choose Your Own Adventure Game
A single-file Python 3 command-line game with inventory, multiple endings, and replay capability.
"""

def get_valid_choice(valid_options):
    """Prompt user for input until a valid choice is provided."""
    while True:
        user_input = input("\n> ").strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid choice. Please enter one of: {', '.join(valid_options)}")


def display_scene(scene_data):
    """Display a scene's description and available choices."""
    print("\n" + "=" * 60)
    print(scene_data["description"])
    print("=" * 60)
    if "inventory_note" in scene_data:
        print(f"[Inventory Note: {scene_data['inventory_note']}]")
    print("\nWhat do you do?")
    for key, text in scene_data["choices"].items():
        print(f"  {key}) {text}")


def play_game():
    """Main game loop."""
    inventory = set()
    current_scene = "start"
    
    # Define all scenes in the game
    scenes = {
        "start": {
            "description": """
You awaken on a rocky shore, the sound of crashing waves in your ears.
In the distance, a lighthouse beam cuts through the thick fog.
You're drenched and disoriented, with no memory of how you got here.
The lighthouse seems like your only chance at rescue.""",
            "choices": {
                "a": "Head toward the lighthouse along the beach",
                "b": "Search the beach for supplies first",
            }
        },
        
        "beach_search": {
            "description": """
You search along the shoreline and discover an old shipwreck half-buried in sand.
Near the wreckage, you find a rusty but functional lantern and an old journal.
The journal contains cryptic notes about "the keeper's test" and mentions a hidden cave.""",
            "choices": {
                "a": "Take the lantern and head to the lighthouse",
                "b": "Take the journal and search for the hidden cave",
                "c": "Take both and head to the lighthouse",
            },
            "inventory_note": "You found a lantern and journal!"
        },
        
        "lighthouse_approach": {
            "description": """
You approach the lighthouse. The iron door is sealed shut, and the lock glows with an eerie blue light.
A sign reads: "Only those who carry the keeper's light may enter."
You notice a narrow path leading up the cliff face toward a cave entrance.""",
            "choices": {
                "a": "Try to force the lighthouse door",
                "b": "Take the cliff path to the cave",
                "c": "Call out for help and wait",
            }
        },
        
        "cave_entrance": {
            "description": """
You climb the narrow path and reach a dark cave mouth.
The wind howls ominously, and you hear strange echoes from within.
Your eyes adjust to the darkness.""",
            "choices": {
                "a": "Enter the cave cautiously",
                "b": "Return to the lighthouse and try the door again",
            }
        },
        
        "cave_interior": {
            "description": """
Deep inside the cave, you find an ancient chamber with murals on the walls.
They depict a guardian spirit and a ritual. On an altar sits a glowing crystal key.
As you approach, the cave begins to tremble.""",
            "choices": {
                "a": "Take the crystal key quickly and run out",
                "b": "Study the murals carefully before taking anything",
                "c": "Leave the cave and return to the lighthouse",
            },
            "inventory_note": "A crystal key glows before you..."
        },
        
        "lighthouse_interior": {
            "description": """
You unlock the lighthouse door with the crystal key!
Inside, you find a control panel, a spiral staircase, and the lighthouse keeper—
a ghostly figure who appears trapped between worlds.
The keeper looks at you with desperate eyes.""",
            "choices": {
                "a": "Ask the keeper what happened here",
                "b": "Climb to the top of the lighthouse immediately",
                "c": "Search the control panel for clues",
            }
        },
    }
    
    # Game state tracking
    while True:
        if current_scene not in scenes:
            # Handle special ending scenes
            if current_scene == "good_ending_rescue":
                print("\n" + "=" * 60)
                print("""
╔═══════════════════════════════════════════════════╗
║          GOOD ENDING: RESCUED AND FREE            ║
╚═══════════════════════════════════════════════════╝

Your signal reaches a passing cargo ship. Within hours, you're aboard,
warm and safe, wrapped in blankets with hot tea in your hands.
The lighthouse fades into the distance as you sail away.

You wonder about the keeper's fate, but you know you did the right thing.
Your adventure at Lantern Lighthouse becomes just another mystery of the sea.""")
                print("=" * 60)
                return
            
            elif current_scene == "good_ending_peace":
                print("\n" + "=" * 60)
                print("""
╔═══════════════════════════════════════════════════╗
║        GOOD ENDING: SPIRITS AT PEACE              ║
╚═══════════════════════════════════════════════════╝

The keeper's form shimmers and fades as the curse lifts.
A warm light fills the lighthouse, and you feel a profound sense of peace.
The keeper smiles one last time before vanishing completely.

The lighthouse becomes an ordinary beacon once more, and you signal for rescue.
Days later, you're found and returned to civilization, forever changed by what you witnessed.""")
                print("=" * 60)
                return
            
            elif current_scene == "bad_ending_trapped":
                print("\n" + "=" * 60)
                print("""
╔═══════════════════════════════════════════════════╗
║       BAD ENDING: TRAPPED WITH THE KEEPER         ║
╚═══════════════════════════════════════════════════╝

As you try to flee, the lighthouse doors slam shut behind you.
The keeper's form solidifies, and you realize the curse needs a host.
You become one with the lighthouse, forever bound to tend its light.

Your rescuers never come. Another victim may wash ashore someday,
and the cycle will continue once more...""")
                print("=" * 60)
                return
            
            elif current_scene == "bad_ending_lost_sea":
                print("\n" + "=" * 60)
                print("""
╔═══════════════════════════════════════════════════╗
║        BAD ENDING: LOST TO THE SEA                ║
╚═══════════════════════════════════════════════════╝

Your makeshift raft is no match for the treacherous waters.
The fog rolls in thick, disorienting you completely.
You drift for hours, then days, until you're too weak to paddle.

The lighthouse beam grows fainter with each passing night.
Your adventure ends not with a bang, but with the gentle pull of the tide.""")
                print("=" * 60)
                return
            
            else:
                print("ERROR: Unknown scene")
                return
        
        scene = scenes[current_scene]
        display_scene(scene)
        
        valid_choices = list(scene["choices"].keys())
        choice = get_valid_choice(valid_choices)
        
        # Scene transitions with inventory checks
        if current_scene == "start":
            if choice == "a":
                current_scene = "lighthouse_approach"
            elif choice == "b":
                current_scene = "beach_search"
        
        elif current_scene == "beach_search":
            if choice == "a":
                inventory.add("lantern")
                current_scene = "lighthouse_approach"
            elif choice == "b":
                inventory.add("journal")
                current_scene = "cave_entrance"
            elif choice == "c":
                inventory.add("lantern")
                inventory.add("journal")
                current_scene = "lighthouse_approach"
        
        elif current_scene == "lighthouse_approach":
            if choice == "a":
                if "lantern" in inventory:
                    current_scene = "lighthouse_interior"
                else:
                    print("\n[The door won't budge without the keeper's light!]")
                    current_scene = "lighthouse_approach"
            elif choice == "b":
                current_scene = "cave_entrance"
            elif choice == "c":
                print("\n[You shout into the fog, but no one hears you...]")
                print("[Hours pass. Your throat grows hoarse. You must make a decision.]")
                current_scene = "lighthouse_approach"
        
        elif current_scene == "cave_entrance":
            if choice == "a":
                current_scene = "cave_interior"
            elif choice == "b":
                current_scene = "lighthouse_approach"
        
        elif current_scene == "cave_interior":
            if choice == "a":
                inventory.add("lantern")
                current_scene = "lighthouse_approach"
            elif choice == "b":
                print("\n[As you study the murals, the trembling stops.]")
                print("[You learn the keeper was cursed to guard the lighthouse forever.]")
                inventory.add("lantern")
                inventory.add("knowledge")
                current_scene = "lighthouse_approach"
            elif choice == "c":
                current_scene = "lighthouse_approach"
        
        elif current_scene == "lighthouse_interior":
            if choice == "a":
                if "knowledge" in inventory:
                    print("\n[The keeper tells you of the curse that binds them.]")
                    print("[They beg you to reach the top and ring the bell to break it.]")
                    current_scene = "good_ending_peace"
                else:
                    current_scene = "bad_ending_trapped"
            elif choice == "b":
                current_scene = "good_ending_rescue"
            elif choice == "c":
                if "journal" in inventory:
                    print("\n[You find a ritual to free the keeper!]")
                    current_scene = "good_ending_peace"
                else:
                    print("\n[You can't decipher the ancient symbols without the journal.]")
                    current_scene = "bad_ending_lost_sea"


def main():
    """Entry point for the game."""
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "LANTERN LIGHTHOUSE" + " " * 25 + "║")
    print("║" + " " * 10 + "A Choose Your Own Adventure Game" + " " * 15 + "║")
    print("╚" + "═" * 58 + "╝\n")
    
    while True:
        play_game()
        
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if play_again in ["yes", "y", "no", "n"]:
                break
            print("Please enter 'yes' or 'no'.")
        
        if play_again in ["no", "n"]:
            print("\nThank you for playing Lantern Lighthouse! Farewell, adventurer.\n")
            break


if __name__ == "__main__":
    main()
