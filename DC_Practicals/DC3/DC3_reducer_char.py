import sys

current_char = None
count = 0

for line in sys.stdin:

    char, val = line.strip().split("\t")

    val = int(val)

    if char == current_char:
        count += val

    else:
        if current_char:
            print(f"{current_char}\t{count}")

        current_char = char
        count = val

if current_char:
    print(f"{current_char}\t{count}")