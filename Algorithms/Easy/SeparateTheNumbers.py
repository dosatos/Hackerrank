#!/bin/python3

import sys

def is_beautiful(start, rest):
    # is beautiful if rest will be exhausted
    # return False once found that is not beautiful
    while True:
        if rest == "":
            return True
        next_num = str(int(start) + 1)
        next_num_length = len(next_num)
        if not rest.startswith(next_num):
            return False
        if rest.startswith(next_num):
            start = next_num
            rest = rest[next_num_length:]

def separateNumbers(s):
    for idx in range(1, len(s)):
        start = s[:idx]
        rest = s[idx:]
        # increase the base by moving the pointer until beautiful is found
        if is_beautiful(start, rest):
            print("YES {}".format(start))
            return None
    print("NO")
    return None

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)
