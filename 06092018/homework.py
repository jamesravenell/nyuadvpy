#!/usr/bin/env python3

import pprint

old_things = [0,1,2,3,4,5,6,7,8,9]

def use_for_loop():
    pprint.pprint(old_things)
    new_things = []
    for ITEM in old_things:
        if not(ITEM % 2):
            new_things.append(ITEM)
    pprint.pprint(new_things)

def use_list_comprehension():
    new_things = [ITEM for ITEM in old_things if not(ITEM % 2)]
    pprint.pprint(new_things)
    return

def main():
    use_for_loop()
    use_list_comprehension()

if __name__ == '__main__':
    main()
