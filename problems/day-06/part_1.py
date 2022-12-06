#!/usr/bin/env python3
line = input()
for i in range(len(line)):
    if len(set(line[i : i + 4])) == 4:
        print(i + 4)
        break
