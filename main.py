import colorama, json, lib, time, pynput
from os import system
import os
from colorama import Style, Fore, Back
import json

colorama.init() # Initiate colorama lib (needed for escape codes)
action_list = ["analyze", "complete", "exit", "load", "suggest"]
# scommand_list = ["l_add", "l_clear", "l_set", "p_clear", "p_set", "s_list", "help", exit]
scommands = {"l_add": "Add to the list of known letters",
             "l_clear": "Clear the known list of letters [Clears List]",
             "l_set": "Set the known list of letters (but not their positions) [Clears List]",
             "p_clear": "Clear the known positions [Clears List]",
             "p_set": "Set the known positions of letters",
             "s_list": "Get a list of suggested words",
             "help": "View this list",
             "exit": "Exit suggestion mode"}
action = None
word_list = []

if __name__ == '__main__':
    print("Initiating WordleAuto...")
    time.sleep(1)
    print("Loading Word list...")

    if os.path.exists("./data.json"):  # Load words from word list file
        f = open("./data.json")
        json_file = json.load(f)
        word_list = json_file["word_list"]
        f.close()

    print("Loaded Word List!")
    # (action is None) or (action not in action_list)

    while True:  # Command Handler
        print("\n\nAction List:")
        print(f"[{', '.join([x for x in action_list])}]")
        action = input("\nPlease input the action to take: ")
        if action not in action:
            system("cls")
            print(f"{Fore.RED}Error{Fore.RESET}: Selected action not in list")
            print("Please check the commands spelling")
            time.sleep(2)
        else:
            lib.process_action(action)

