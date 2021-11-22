import os, sys
f = open(os.path.join(sys.path[0], "affischutskick1.in"), "r")
input = f.read().rstrip('\n').split(" ")
print(input)    # ['120', '90', '70']