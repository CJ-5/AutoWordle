import colorama, time, sys, os, json
from colorama import Style, Fore, Back
from collections import OrderedDict
import main


def process_action(_action):
    if _action == "analyze":
        # Analyze the current word list
        file = None
        if not main.word_list:
            print("No wordlist has been loaded... Please load a word list via the 'load' command")
        else:
            wordlist = main.word_list

            # Run Analysis Script
            letter_pop = {'a': 0,
                          'b': 0,
                          'c': 0,
                          'd': 0,
                          'e': 0,
                          'f': 0,
                          'g': 0,
                          'h': 0,
                          'i': 0,
                          'j': 0,
                          'k': 0,
                          'l': 0,
                          'm': 0,
                          'n': 0,
                          'o': 0,
                          'p': 0,
                          'q': 0,
                          'r': 0,
                          's': 0,
                          't': 0,
                          'u': 0,
                          'v': 0,
                          'w': 0,
                          'x': 0,
                          'y': 0,
                          'z': 0}

            for w in wordlist:  # Scan letter occurrences
                for l in w:
                    letter_pop[l] += 1

            print("Results Gathered")
            print("\n")
            key_list = list(letter_pop.keys())
            for i in range(len(letter_pop)):
                print(f"{key_list[i]}: {letter_pop[key_list[i]]}")

            # Sort
            pop_sorted = {key: value for key, value in sorted(letter_pop.items(), key=lambda _value: _value[1])}
            pop_keys = list(pop_sorted.keys())[::-1]
            pop_values = list(pop_sorted.values())[::-1]

            print("Letters that appeared the most: ")
            # Top ten letters
            for i in range(len(pop_sorted)):
                print(f"{pop_keys[i]}: {pop_values[i]}")

    elif _action == "complete":
        print("Not Implemented...")
        time.sleep(1)
        os.system("cls")
    elif _action == "exit":  # Exit Program
        print("Exiting...")
        time.sleep(0.3)
        sys.exit(-1)
    elif _action == "load":  # Load a word list
        file_loaded = False
        while not file_loaded:
            os.system("cls")
            print(f"{Fore.YELLOW}Loading word list...{Fore.RESET}")

            file_path = input("File Path: ")

            if os.path.isfile(file_path):
                f = open(file_path)
                main.word_list = json.load(f)["word_list"]
                f.close()
                file_loaded = True  # Exit Loop
            else:  # file does not exist
                print(f"{Fore.RED}Specified File path does not exist{Fore.RESET}")
        print(f"{Fore.GREEN}File Loaded{Fore.RESET}")
        time.sleep(1)
    elif _action == "suggest":
        os.system("cls")
        _stat = True
        _action = None

        # Add Script to deal with conflicts of letters being in one list and not the other
        active_list = []  # Known letters (Max of 6)
        active_pos = {0: None,  # List of positions that we know the letter is in
                      1: None,
                      2: None,
                      3: None,
                      4: None,
                      5: None,
                      6: None}
        invalid_letters = []  # Letters that are not in the word

        while _stat:
            # Loop Headers
            os.system("cls")
            print(f"\n{Fore.BLUE}Running Suggestions Analytics{Fore.RESET}\n")
            print(f"{Fore.GREEN}Action List:{Fore.RESET} {Fore.YELLOW}"
                  f"[{Fore.RESET}{', '.join(x for x in list(main.scommands.keys()))}{Fore.YELLOW}]{Fore.RESET}")

            print(f"{Fore.GREEN}Known Letter List: {Fore.YELLOW}"
                  f"{[''.join(x for x in active_list), 'Empty List'][not active_list]}")
            print(f"{Fore.GREEN}Invalid Letter List: "
                  f"{Fore.YELLOW} {[''.join(x for x in invalid_letters), 'Empty List'][not invalid_letters]}")
            print(f"""
            {Fore.GREEN}Known Position List:
            {Fore.YELLOW}1{Fore.RESET}: {Fore.BLUE}{active_pos[0]}
            {Fore.YELLOW}2{Fore.RESET}: {Fore.BLUE}{active_pos[1]}
            {Fore.YELLOW}3{Fore.RESET}: {Fore.BLUE}{active_pos[2]}
            {Fore.YELLOW}4{Fore.RESET}: {Fore.BLUE}{active_pos[3]}
            {Fore.YELLOW}5{Fore.RESET}: {Fore.BLUE}{active_pos[4]}
            {Fore.YELLOW}6{Fore.RESET}: {Fore.BLUE}{active_pos[5]}
            """)


            # "l_add", "l_clear", "l_set", "p_clear", "p_set", "exit"
            saction = input(f"{Fore.GREEN}Action:{Fore.BLUE} ")

            if saction not in list(main.scommands.keys()):
                print("Suggest Analytics Command is invalid. Please choose from the action list")
            else:  # Command is ok
                if saction == "l_add":  # Add to the list of known letters
                    if len(active_list) == 6:
                        print(f"{Fore.RED}Cant add to list, there are already 6 letters. Please use 'l_clear' to"
                              f" clear the active list or 'l_set' to set a new list")
                        time.sleep(3)
                    else:
                        print(f"{Fore.GREEN}Adding to list of known letters{Fore.RESET}\n")
                        letter = input(f"   {Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ")
                        if not len(letter) == 1:
                            print(f"{Fore.RED}Letter can only be {Fore.YELLOW}1{Fore.RED} in length.{Fore.RED}")
                        else:  # Add letter to list
                            print(f"{Fore.GREEN}Added {Fore.YELLOW}{letter}{Fore.GREEN} to the active list!")
                            active_list.append(letter)
                            time.sleep(1)

                elif saction == "l_clear":  # Clear the list of known letters
                    print(f"{Fore.GREEN}Cleared Active List!{Fore.RESET}")
                    active_list.clear()
                    time.sleep(1)
                elif saction == "l_set":    # The list of known letters (not their exact positions)
                    print(f"{Fore.GREEN}Setting known letters (upto: {Fore.YELLOW}6{Fore.GREEN}){Fore.RESET}\n")
                    letter_list = input(f"{Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ")
                    os.system("cls")
                    if len(letter_list) > 6:
                        print(f"{Fore.RED}List cannot be above 6 letters...{Fore.RESET}")
                        time.sleep(1.4)
                    else:
                        str_format = "".join(x for x in letter_list)
                        print(f"{Fore.GREEN}Set new list to {Fore.YELLOW}{str_format}{Fore.RESET}")
                        active_list = [x for x in letter_list]  # lambda go brr
                elif saction == "p_clear":  # Clear the Position List
                    print(f"{Fore.GREEN}Cleared Position List!")
                    time.sleep(1)
                elif saction == "p_set":    # Set letters into the positions that are known
                    os.system("cls")
                    print(f"{Fore.BLUE}Setting Letter Positions")
                    for i in range(6):
                        char = input(f"{Fore.GREEN}Position {Fore.YELLOW}{i+1}: ")
                        active_pos[i] = [None, char][len(char) == 1 and not char == " "]

                    time.sleep(1)

                elif saction == "i_set":
                    os.system("cls")
                    invalid_letters.clear()
                    print(f"{Fore.BLUE}Setting Invalid Letters")
                    letters = input(f"   {Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ")
                    for x in letters:
                        if x not in invalid_letters:
                            invalid_letters.append(x)

                elif saction == "i_add":
                    os.system("cls")
                    print(f"{Fore.GREEN}Adding to list of invalid letters{Fore.RESET}\n")
                    letter = input(f"   {Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ")
                    if not len(letter) == 1:
                        print(f"{Fore.RED}Letter can only be {Fore.YELLOW}1{Fore.RED} in length.{Fore.RED}")
                    elif letter in invalid_letters:
                        print(f"{Fore.RED}Letter is already in list.")
                    else:  # Add letter to list
                        print(f"{Fore.GREEN}Added {Fore.YELLOW}{letter}{Fore.GREEN} to the invalid letter list list!")
                        invalid_letters.append(letter)
                    time.sleep(2)
                elif saction == "i_clear":
                    os.system("cls")
                    print(f"{Fore.GREEN}Invalid Letter List Cleared!{Fore.RESET}")
                    os.system("cls")
                elif saction == "s_list":   # Print list of suggested words
                    print(f"{Fore.GREEN}Generating Suggestion List...{Fore.YELLOW} (This may take a while)\n")
                    print(f"{Fore.BLUE}Progress{Fore.RESET}:{Fore.YELLOW} 0%", end='')

                    # Generate list of words that contain known letters
                    word_list = main.word_list
                    candidates0 = []
                    wl_length = len(word_list)
                    print('\033[?25l', end="")  # Hide Cursor
                    for i, word in enumerate(word_list):
                        valid = True
                        # Check to make sure the word does not contain any invalid letters
                        for letter in word:
                            if letter in invalid_letters:
                                valid = False
                                break

                        # Initial Check (Check to make sure that all known letters are in the word)
                        if valid:
                            for kl in active_list:
                                _valid = False
                                for letter in word:  # if the word contains a known letter _valid will tick True
                                    _valid = letter == kl
                                    if _valid:
                                        break

                                if not _valid:
                                    valid = False
                                    break

                        if valid:  # Position Check
                            for x, char in enumerate(word):
                                if active_pos[x] is not None:
                                    valid = active_pos[x] == char
                                    if not valid:
                                        break

                        if valid:
                            candidates0.append(word)

                        print(f'\r{Fore.BLUE}Progress{Fore.RESET}:{Fore.YELLOW} {round((i / wl_length) * 100)}%', end='')

                    print('\033[?25h', end="")  # Show Cursor
                    print("\n")
                    print(f"{Fore.GREEN}List of candidates: {Fore.YELLOW}"
                          f"{f'{Fore.GREEN},{Fore.YELLOW} '.join(x for x in candidates0)}")
                    input("Press Any Key to Continue...")

                elif saction == "help":  # Print Help Command
                    for list_item in main.scommands:
                        print(f"{f'{Fore.GREEN}{list_item}{Fore.RESET}:':<30}"  # Key
                              f"{Fore.YELLOW}{main.scommands[list_item]}{Fore.RESET}")  # Definition
                    print("\n\n")
                elif saction == "exit":
                    print(Fore.RESET)
                    _stat = False
