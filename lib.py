import json
import os
import sys
import time

from colorama import Fore
from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow

import main


def is_focused():
    return main.initial_window_title == GetWindowText(GetForegroundWindow())


def process_action(_action):
    if _action == "analyze":
        # Analyze the current word list
        file = None
        if not main.word_list:
            print("No wordlist has been loaded... Please load a word list via the 'load' command")
        else:
            wordlist = main.word_list

            # Run Analysis Script
            letter_pop = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
                          'l': 0, 'm': 0, 'n': 0, 'o': 0,  'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
                          'w': 0, 'x': 0, 'y': 0, 'z': 0}

            for w in wordlist:  # Scan letter occurrences
                for l in w:
                    letter_pop[l] += 1

            print(f"{Fore.GREEN}Results Gathered{Fore.RESET}")
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
        pass
    elif _action == "exit":  # Exit Program
        print(f"{Fore.RED}Exiting...{Fore.RESET}")
        time.sleep(0.3)
        sys.exit(-1)
    elif _action == "load":  # Load a word list
        file_loaded = False
        while not file_loaded:
            os.system("cls")
            print(f"{Fore.YELLOW}Loading word list...{Fore.RESET}")
            file_path = input(f"{Fore.GREEN}File Path{Fore.YELLOW}:{Fore.RESET} ")
            if os.path.isfile(file_path):
                f = open(file_path)
                main.word_list_original = json.load(f)["word_list"]
                if len(main.word_list) > 9999:
                    print(f"{Fore.RED}NOTE{Fore.RESET}: {Fore.YELLOW}This wordlist is over "
                          f"{Fore.GREEN}9999{Fore.YELLOW} words, the analysis scripts may take a while.")
                f.close()
                file_loaded = True  # Exit Loop
            else:  # file does not exist
                print(f"{Fore.RED}Specified File path does not exist{Fore.RESET}")
                time.sleep(1)
        print(f"{Fore.GREEN}File Loaded{Fore.RESET}")
        main.word_list = main.word_list_original.copy()
        time.sleep(1)
        os.system("cls")

    elif _action == "suggest":
        os.system("cls")
        _stat = True  # Loop Status
        _action = None

        # Add Script to deal with conflicts of letters being in one list and not the other
        active_list = []  # Known letters (Max of 5)
        active_pos = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None}  # Known Letter Positions
        invalid_letters = []  # Letters that are not in the word
        used_words_list = []  # Which words the user has already attempted

        while _stat:
            # Loop Headers
            os.system("cls")
            print(f"\n{Fore.LIGHTBLUE_EX}Running Suggestions Analytics{Fore.RESET}\n")

            # Action List
            print(f"{Fore.GREEN}Action List:{Fore.RESET} {Fore.YELLOW}"
                  f"[{Fore.RESET}{', '.join(x for x in list(main.scommands.keys()))}{Fore.YELLOW}]{Fore.RESET}")

            # Known Letter List
            print(f"{Fore.GREEN}Known Letter List: {Fore.YELLOW}"
                  f"{[''.join(x for x in active_list), f'{Fore.RED}Empty List{Fore.RESET}'][not active_list]}")

            # Invalid Letter List
            print(f"{Fore.GREEN}Invalid Letter List: "
                  f"{Fore.YELLOW} {[''.join(x for x in invalid_letters), f'{Fore.RED}Empty List'][not invalid_letters]}")

            # Used Words List
            print(f"{Fore.GREEN}Used Words List: "
                  f"{[Fore.YELLOW + f'{Fore.GREEN}, {Fore.YELLOW}'.join([x for x in used_words_list]), f'{Fore.RED}Empty List'][not used_words_list]}{Fore.RESET}")

            print(f"{Fore.GREEN}Known Position List: \
            \n{Fore.YELLOW}1{Fore.RESET}: {Fore.LIGHTBLUE_EX}{active_pos[0]}\
            \n{Fore.YELLOW}2{Fore.RESET}: {Fore.LIGHTBLUE_EX}{active_pos[1]}\
            \n{Fore.YELLOW}3{Fore.RESET}: {Fore.LIGHTBLUE_EX}{active_pos[2]}\
            \n{Fore.YELLOW}4{Fore.RESET}: {Fore.LIGHTBLUE_EX}{active_pos[3]}\
            \n{Fore.YELLOW}5{Fore.RESET}: {Fore.LIGHTBLUE_EX}{active_pos[4]}\n\n")

            # "l_add", "l_clear", "l_set", "p_clear", "p_set", "exit"
            saction = input(f"{Fore.GREEN}Action:{Fore.LIGHTBLUE_EX} ").lower()

            if saction not in list(main.scommands.keys()):
                print(f"{Fore.RED}Suggest Analytics Command is invalid. Please choose from the action list{Fore.RESET}")
                time.sleep(1.3)
            else:  # Command is ok
                if saction == "l_add":  # Add to the list of known letters
                    if len(active_list) == 5:
                        print(f"{Fore.RED}Cant add to list, there are already 5 letters. Please use "
                              f"'{Fore.YELLOW}l_clear{Fore.RED}' to clear the active list or "
                              f"'{Fore.YELLOW}l_set{Fore.RED}' to set a new list")
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
                    main.word_list = main.word_list_original.copy()
                    time.sleep(1)
                elif saction == "l_set":  # The list of known letters (not their exact positions)
                    print(f"{Fore.GREEN}Setting known letters (upto: {Fore.YELLOW}5{Fore.GREEN}){Fore.RESET}\n")
                    original_list = active_list.copy()
                    letter_list = input(f"{Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ")
                    os.system("cls")
                    if len(letter_list) > 5:
                        print(f"{Fore.RED}List cannot be above 5 letters...{Fore.RESET}")
                        time.sleep(1.4)
                    else:
                        str_format = "".join(x for x in letter_list)
                        print(f"{Fore.GREEN}Set new list to {Fore.YELLOW}{str_format}{Fore.RESET}")
                        active_list = [x for x in letter_list]  # lambda go brr

                    # Check for any missing letters from the original list and reset word list if there are any
                    for letter in original_list:
                        if letter not in letter_list:
                            main.word_list = main.word_list_original.copy()
                            break

                elif saction == "p_clear":  # Clear the Position List
                    print(f"{Fore.GREEN}Cleared Position List!")
                    main.word_list = main.word_list_original.copy()
                    time.sleep(1)
                elif saction == "p_set":  # Set letters into the positions that are known
                    os.system("cls")
                    print(f"{Fore.LIGHTBLUE_EX}Setting Letter Positions{Fore.RESET}")
                    original_pos = active_pos.copy()
                    for i in range(5):
                        char = input(f"{Fore.GREEN}Position {Fore.YELLOW}{i + 1}: ")
                        active_pos[i] = [None, char][len(char) == 1 and not char == " "]

                    # Check for any changes the the original keys
                    for i, k in enumerate(active_pos):
                        if active_pos[list(active_pos.keys())[i]] != original_pos[list(original_pos.keys())[i]]:
                            main.word_list = main.word_list_original.copy()
                            break

                    time.sleep(1)

                elif saction == "i_set":
                    os.system("cls")
                    old_letters = invalid_letters.copy()
                    invalid_letters.clear()
                    print(f"{Fore.LIGHTBLUE_EX}Setting Invalid Letters")
                    print(f"{Fore.YELLOW}Note{Fore.RED}:{Fore.RESET} Duplicate letters do not need to be added "
                          f"a quantity check is performed upon list generation.")
                    letters = input(f"   {Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ")

                    # Check for duplicates and conflicts
                    for letter in letters:
                        if letter not in invalid_letters and letter not in active_list:
                            invalid_letters.append(letter)

                    # Check if there is any letters missing from the original list
                    for letter in old_letters:
                        if letter not in letters:
                            main.word_list = main.word_list_original.copy()
                            break

                elif saction == "i_add":
                    os.system("cls")
                    print(f"{Fore.GREEN}Adding to list of invalid letters{Fore.RESET}\n")
                    letter = input(f"   {Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ")
                    if not len(letter) == 1:
                        print(f"{Fore.RED}Letter can only be {Fore.YELLOW}1{Fore.RED} in length.{Fore.RED}")
                    elif letter in invalid_letters:
                        print(f"{Fore.RED}Letter is already in list.")
                    elif letter in active_list:
                        print(f"{Fore.RED}Letter in list of known letters {Fore.YELLOW}NOTE{Fore.RESET}:"
                              f" duplicate letters do not need to be added to this list.")
                    else:  # Add letter to list
                        print(f"{Fore.GREEN}Added {Fore.YELLOW}{letter}{Fore.GREEN} to the invalid letter list list!")
                        invalid_letters.append(letter)
                    time.sleep(2)
                elif saction == "i_clear":
                    os.system("cls")
                    invalid_letters.clear()
                    main.word_list = main.word_list_original.copy()  # Reset Optimized Word List
                    print(f"{Fore.GREEN}Invalid Letter List Cleared!{Fore.RESET}")
                    time.sleep(1)
                    os.system("cls")
                elif saction == "s_list":  # Print list of suggested words
                    print(f"{Fore.GREEN}Generating Suggestion List...{Fore.YELLOW} (This may take a while)\n")
                    print(f"{Fore.LIGHTBLUE_EX}Progress{Fore.RESET}:{Fore.YELLOW} 0%", end='')

                    # Generate list of words that contain known letters
                    word_list = main.word_list.copy()
                    candidates0 = []
                    wl_length = len(word_list)
                    print('\033[?25l', end="")  # Hide Cursor

                    # Generate known letter occurrence list
                    kl_dict = dict()
                    for l in active_list:
                        if l not in list(kl_dict.keys()):  # Create New entry
                            kl_dict[l] = 1
                        else:
                            kl_dict[l] += 1

                    # print(kl_dict)

                    for i, word in enumerate(word_list):  # Generate List of valid Candidates

                        valid = True

                        if word not in used_words_list:
                            # Check to make sure the word does not contain any invalid letters
                            for letter in word:
                                if letter in invalid_letters:
                                    valid = False
                                    break

                            # Initial Check (Check to make sure that all known letters are in the word)
                            if valid:
                                # Generate Letter Occurrence list for the word
                                _w = dict()
                                for l in word:
                                    if l not in _w:
                                        _w[l] = 1
                                    else:
                                        _w[l] += 1

                                # Check Known Letter dictionary vs Local Word Dictionary
                                for l in kl_dict:
                                    if l not in _w:  # Checks if the known letter is actually in the word
                                        valid = False
                                        break
                                    elif kl_dict[l] > _w[l]:  # Checks that occurrences are the same
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

                        print(f'\r{Fore.LIGHTBLUE_EX}Progress{Fore.RESET}:'
                              f'{Fore.YELLOW} {round((i / wl_length) * 100)}%', end='')

                    print(f'\r{Fore.LIGHTBLUE_EX}Progress{Fore.RESET}:'
                          f'{Fore.YELLOW} 100%', end='')

                    # Optimize Word List Speed (Remove any word that is not a candidate any more)

                    # Generate Negative of List
                    list_copy = main.word_list.copy()
                    for cword in candidates0:
                        if cword in list_copy:
                            list_copy.remove(cword)

                    for cword in list_copy:
                        if cword in main.word_list:
                            main.word_list.remove(cword)

                    print('\033[?25h')  # Show Cursor
                    chance = 1 / [len(candidates0), 1][not candidates0]  # fixes divison by 0 issue with code below
                    print(f"{Fore.GREEN}Chances of picking the right word: " +
                          f"{[f'{Fore.YELLOW}{round((chance * 100), 4)}{Fore.GREEN}%', f'{Fore.YELLOW}0{Fore.GREEN}%'][not candidates0]}")
                    candidates0.sort()
                    print(f"{Fore.GREEN}List of candidates: {Fore.YELLOW}"
                          f"{[f'{Fore.GREEN},{Fore.YELLOW} '.join(x for x in candidates0), 'No Candidates Found'][not candidates0]}")

                    print(f"{Fore.LIGHTBLUE_EX}Press any key to continue...{Fore.RESET}")
                    main.key_prompt = True
                    while main.key_prompt:
                        continue

                elif saction == "u_add":
                    print(f"{Fore.LIGHTBLUE_EX}Adding to Used Words List")
                    word = input(f"   {Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ")
                    if len(word) != 5 or word not in main.word_list:
                        print(f"{Fore.RED}Invalid Word Length{Fore.RESET}")
                    else:
                        print(f"{Fore.GREEN}Added {Fore.YELLOW}{word}{Fore.RESET}")
                        used_words_list.append(word)
                    time.sleep(1.3)
                elif saction == "u_clear":
                    print(f"{Fore.LIGHTBLUE_EX}Cleared {Fore.YELLOW}{len(used_words_list)}{Fore.RESET}"
                          f" words from Used Words List!{Fore.RESET}")
                    used_words_list.clear()
                    time.sleep(1.2)
                elif saction == "u_set":
                    print(f"{Fore.LIGHTBLUE_EX}Setting Used Words List {Fore.RESET}")

                    print(f"{Fore.LIGHTBLUE_EX}Please separate the words by a comma{Fore.RESET}")
                    used_words = list(
                        input(f"   {Fore.GREEN}>{Fore.YELLOW}:{Fore.RESET} ").lower().replace(' ', '').split(','))
                    valid_words = []

                    warning = False
                    for word in used_words:
                        if len(word) != 5 or word not in main.word_list:
                            warning = True
                            print(f"{Fore.RED}Invalid Word{Fore.RESET}: {Fore.YELLOW}{word}")
                        else:
                            valid_words.append(word)

                    if not warning:
                        valid_words.sort()
                        print([
                                  f"{Fore.GREEN}Added {Fore.YELLOW}{f'{Fore.GREEN},{Fore.YELLOW} '.join([x for x in used_words])} to the used words list",
                                  f"{Fore.RED}No New Words Added to the list{Fore.RESET}"][not valid_words])
                        for word in valid_words:
                            used_words_list.append(word)
                        time.sleep(1)

                elif saction == "help":  # Print Help Command
                    for list_item in main.scommands:
                        print(f"{f'{Fore.GREEN}{list_item}{Fore.RESET}:':<30}"  # Key
                              f"{Fore.YELLOW}{main.scommands[list_item]}{Fore.RESET}")  # Definition
                    print('\n' * 2)
                elif saction == "reset":  # Clear inputted data
                    main.word_list = main.word_list_original.copy()
                    active_pos = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None}  # Known Letter Positions
                    invalid_letters.clear()
                    active_list.clear()
                    used_words_list.clear()
                elif saction == "exit":
                    print(Fore.RESET)
                    _stat = False


def on_press(_):
    if main.key_prompt and is_focused():
        main.key_prompt = False


def any_key_prompt():
    try:
        print(f"{Fore.GREEN}Started Async Listener{Fore.RESET}")
        kb = keyboard.Listener(on_press=on_press)
        kb.start()
    except Exception:
        print(f"{Fore.RED}Any_Key Async Listener Failed to start{Fore.RESET}")
