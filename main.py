import colorama, json, lib, time, pynput
from os import system
import os
from colorama import Style, Fore, Back
import json

colorama.init()  # Initiate colorama lib (needed for escape codes)
action_list = ["analyze", "complete", "exit", "load", "suggest"]
# scommand_list = ["l_add", "l_clear", "l_set", "p_clear", "p_set", "s_list", "help", exit]
scommands = {"l_add": "Add to the list of known letters",
             "l_clear": f"Clear the known list of letters [{Fore.RED}Clears List{Fore.YELLOW}]",
             "l_set": f"Set the known list of letters (but not their positions) [{Fore.RED}Clears List{Fore.YELLOW}]",
             "p_clear": f"Clear the known positions [{Fore.RED}Clears List{Fore.YELLOW}]",
             "p_set": "Set the known positions of letters",
             "s_list": "Get a list of suggested words",
             "i_set": f"Set the invalid letters list [{Fore.RED}Clears List{Fore.YELLOW}]",
             "i_add": f"Add to the invalid letters list [{Fore.RED}Clears List{Fore.YELLOW}]",
             "i_clear": "Clear the invalid letters list",
             "help": "View this list",
             "exit": "Exit suggestion mode"}
action = None
word_list = []
key_prompt = False

if __name__ == '__main__':
    print("Initiating WordleAuto...")
    time.sleep(1)
    print("Starting Async Any_Key Listener")
    lib.any_key_prompt()

    # Add script to attempt to auto load the word list
    # print("Loading Wordlist")
    # if os.path.exists("./data.json"):  # Load words from word list file
    #     f = open("./data.json")
    #     json_file = json.load(f)
    #     word_list = json_file["word_list"]
    #     f.close()
    #
    # print("Loaded Word List!")
    # # (action is None) or (action not in action_list)

    while True:  # Command Handler
        print(f"\n{Fore.GREEN}Action List{Fore.YELLOW}:{Fore.RESET}")
        print(f"[{f'{Fore.GREEN},{Fore.YELLOW} '.join([x for x in action_list])}]")
        print(f"{Fore.GREEN}Word List Load Status: "
              f"{[f'{Fore.GREEN}Loaded! {Fore.BLUE}{len(word_list)} words', f'{Fore.RED}Not Loaded'][not word_list]}")
        print()  # New Line
        print(f"{Fore.GREEN}Please input the action to take{Fore.YELLOW}:{Fore.RESET} ", end='')
        action = input()
        if action not in action:
            system("cls")
            print(f"{Fore.RED}Error{Fore.RESET}: {Fore.YELLOW}Selected action not in list")
            print(f"{Fore.RED}Please check the commands spelling{Fore.RESET}")
            time.sleep(2)
        else:
            lib.process_action(action)

