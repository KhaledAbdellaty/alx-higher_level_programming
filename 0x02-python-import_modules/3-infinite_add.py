#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = 0
    for i in range(len(argv)):
        argc += int(argv[i])
    print("{}".format(argc))
