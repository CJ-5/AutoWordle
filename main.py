import colorama, json, lib, pynput, time
from os import system
from colorama import Style, Fore, Back

colorama.init() # Initiate colorama lib (needed for escape codes)
action_list = ["analyze", "complete", "exit"]
action = None

if __name__ == '__main__':
    print("Initiating WordleAuto...")
    time.sleep(1)
    while (action is None) or (action not in action_list):
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
