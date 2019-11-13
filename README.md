# ChainTranslator
A little bit of code purely to translate text or a file through of different languages and then back. It has no practical use but _can_ mess up text. Thanks to [SuHun Han](https://github.com/ssut) for his fantastic [python google translate ajax api wrapper](https://github.com/ssut/py-googletrans).

# Usage
```
usage: ChainTranslate.py [-h] (-t TEXT | -f FILE) -p CODE [CODE ...] [-s]
                         [-o FILE]

Mess up some words.

optional arguments:
  -h, --help          show this help message and exit
  -t TEXT             text to run through the translator
  -f FILE             file to open and run through translator
  -p CODE [CODE ...]  list of languages to translate the text through using c
                      codes. Will automatically translate back to original
                      language that it detects.
  -s                  silent mode
  -o FILE             File to write output to.
  ```
