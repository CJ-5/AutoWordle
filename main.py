from os import system
import os
import sys
import subprocess
import colorama, json, lib, time, pynput
from win32gui import GetWindowText, GetForegroundWindow
from colorama import Style, Fore, Back
import json
import main

colorama.init()  # Initiate colorama lib (needed for escape codes)
action_list = ["analyze", "complete", "exit", "load", "suggest"]  # Main Actions list
initial_window_title = GetWindowText(GetForegroundWindow())

scommands = {"l_add": "Add to the list of known letters",  # Suggest commands
             "l_clear": f"Clear the known list of letters [{Fore.RED}Clears List{Fore.YELLOW}]",
             "l_set": f"Set the known list of letters (but not their positions) [{Fore.RED}Clears List{Fore.YELLOW}]",
             "p_clear": f"Clear the known positions [{Fore.RED}Clears List{Fore.YELLOW}]",
             "p_set": "Set the known positions of letters",
             "s_list": "Get a list of suggested words",
             "i_set": f"Set the invalid letters list [{Fore.RED}Clears List{Fore.YELLOW}]",
             "i_add": f"Add to the invalid letters list [{Fore.RED}Clears List{Fore.YELLOW}]",
             "i_clear": "Clear the invalid letters list",
             "u_add": "Add to the used words list",
             "u_set": f"Set the used words list ({Fore.LIGHTGREEN_EX}separate the words by a comma{Fore.RESET})",
             "u_clear": "Clear the used words list",
             "reset": "Reset all inputted data",
             "help": "View this command help message",
             "exit": "Exit suggestion mode"}

action = None
word_list_original = []
word_list = []
key_prompt = False

if __name__ == '__main__':
    print("Initiating WordleAuto...")
    time.sleep(1)
    lib.any_key_prompt()

    while True:  # Command Handler
        print(f"\n{Fore.GREEN}Action List{Fore.YELLOW}:{Fore.RESET}")
        print(f"[{Fore.YELLOW}{f'{Fore.GREEN},{Fore.YELLOW} '.join([x for x in action_list])}{Fore.RESET}]")
        print(f"{Fore.GREEN}Word List Load Status: "
              f"{[f'{Fore.GREEN}Loaded! {Fore.LIGHTBLUE_EX}{len(main.word_list)}{Fore.GREEN} words', f'{Fore.RED}Not Loaded'][not main.word_list]}\n")
        print(f"{Fore.GREEN}Please input the action to take{Fore.YELLOW}:{Fore.RESET} ", end='')
        action = input().lower()
        if action not in action:
            system("cls")
            print(f"{Fore.RED}Error{Fore.RESET}: {Fore.YELLOW}Selected action not in list")
            print(f"{Fore.RED}Please check the commands spelling{Fore.RESET}")
            time.sleep(2)
        else:
            lib.process_action(action)
