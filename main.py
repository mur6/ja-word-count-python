from pathlib import Path
import sys

from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C

def word_count(input_text):
    morpheme_list = tokenizer_obj.tokenize(input_text, mode)
    return len([m.surface() for m in morpheme_list])

def main():
    count = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            line = line.strip("\n")
            count += word_count(line)
    print(count)

main()
