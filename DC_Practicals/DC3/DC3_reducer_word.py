import sys

current_word = None
count = 0

for line in sys.stdin:

    word, val = line.strip().split("\t")

    val = int(val)

    if word == current_word:
        count += val

    else:
        if current_word:
            print(f"{current_word}\t{count}")

        current_word = word
        count = val

if current_word:
    print(f"{current_word}\t{count}")