# WordleAuto
A tool for *Wordle* that suggests words based off of inputted data. This is not perfect, its base framework was created in 2 hours.
A future version will add the feature for *Worlde* to be done automatically (For those who are into that kind of thing).

### Packages:
- colorama
- pynput
- pywin32 *(uses win32gui)*

### Usage:
* Download the newest release and unzip into a new folder. Run `main.py` via Command Prompt or with the Pyhton Interperter (`3.9+`)
1. Load a file from the main command menu via the `load` command. Select a word list that contains all words under the `"word_list"` key (use the included data.json which is the current official word list for *Worlde*, as of `April 7th, 2022`)
2. Select any other command (analyze will analyze all words in the list and suggest a word best suited to be the starter word. `Complete` is not implemented (functionality mentioned before, auto completion), and `suggest` which is the main command that you will use).\
Use `suggest` and then help to see its usage. Then select one of the unused words from its list of candidates and rinse and repeat.

### Note:
- The included ***data.json*** is the official *Wordle* word list as of `April 7th, 2022`
- In the *Wordle* source code there are 2 lists of words. There is one that is used for actual daily Wordle words, and
another that adds to the list of allowed guesses. You can guess from either list, but only one is actually chosen from
for the Wordle. Therefore there are words that you may guess and want to add to the list of used words that will be
denied and called invalid, this is not a problem with the code, it is a choice to improve the speed and remove words
that do not need to be processed. If you are making your own list, use only the words under the `Oa` key.

Simple. \
Enjoy!
