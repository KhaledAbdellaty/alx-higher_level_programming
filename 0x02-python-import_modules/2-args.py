#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    print("{} {}{}".format(
         argc,
         "argument" if argc == 1 else "arguments",
         ":" if argc != 0 else "."
         ))
    if argc > 0:
        for i in range(argc):
            print("{}: {}".format(i + 1, argv[i]))
