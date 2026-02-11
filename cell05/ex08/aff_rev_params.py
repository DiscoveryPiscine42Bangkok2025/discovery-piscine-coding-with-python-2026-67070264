import sys

if len(sys.argv) < 3:
    print("none")
else:
    i = len(sys.argv) - 1
    while i >= 1:
        print(sys.argv[i])
        i -= 1