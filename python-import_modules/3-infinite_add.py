#!/usr/bin/python3
from sys import argv

def func():
    argc = len(argv)
    total_sum = 0

    for i in range(1, argc):
        total_sum += int(argv[i])

    print(total_sum)

if __name__ == "__main__":
    func()

