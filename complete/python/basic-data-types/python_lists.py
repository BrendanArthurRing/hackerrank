# https://www.hackerrank.com/challenges/python-lists/problem

import sys

if __name__ == '__main__':
    l = list()

    for line in sys.stdin:
        n = line.replace("\n", "").split(" ")

        if "insert" in n:
            l.insert(int(n[1]), int(n[2]))
        
        if "print" in n:
            print(l)
        
        if "remove" in n:
            l.remove(int(n[1]))
        
        if "append" in n:
            l.append(int(n[1]))
        
        if "sort" in n:
            l.sort()
        
        if "pop" in n:
            l.pop()
        
        if "reverse" in n:
            l.reverse()
