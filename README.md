# WordleAuto
A tool for *Wordle* that suggests words based off of inputted data. This is not perfect, its base framework was created in 2 hours.
A future version will add the feature for *Worlde* to be done automatically (For those who are into that kind of thing).

### Packages:
- colorama
- pynput
- pywin32 *(uses win32gui)*

### Usage:
1. Load a file from the main command menu via the `load` command. Select a word list that contains all words under the `"word_list"` key
2. Select any other command (analyze will analyze all words in the list and suggest a word best suited to be the starter word. `Complete` is not implemented (functionality mentioned before, auto completion), and `suggest` which is the main command that you will use).\
Use `suggest` and then help to see its usage. Then select one of the unused words from its list of candidates and rinse and repeat.

###Note:
The included ***data.json*** is the official *Wordle* word list as of `April 5th, 2022`

Simple. \
Enjoy!
