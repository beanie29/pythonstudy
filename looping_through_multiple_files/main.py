import fileinput


with fileinput.input() as f:
    print(f.filename())
    # for line in f:
    #     print(line)