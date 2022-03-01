import colorama, time, sys, os, json
from colorama import Style, Fore, Back


def process_action(_action):
    if _action == "analyze":
        file = input("File Path: ")
        if os.path.isfile(file):
            f = open(file)
            wordlist = json.load(f)["word_list"]
            f.close()

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

            # Sort to List
            pop_sorted = {key: value for key, value in sorted(letter_pop.items(), key=lambda _value: _value[1])}
            print("Letters that appeared the most: ")
            print(f"")

        else:
            print(f"{Fore.RED}Error{Fore.RESET}: File Does Not exist")
    elif _action == "complete":
        pass
    elif _action == "exit":
        sys.exit(-1)
