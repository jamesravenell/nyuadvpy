#!/usr/bin/env python3

import pprint

def use_for_loop():
   old_things = [0,1,2,3,4,5,6,7,8,9]
   pprint.pprint(old_things)
   new_things = []
   for ITEM in old_things:
       if not(ITEM % 2):
           new_things.append(ITEM)
   pprint.pprint(new_things)
   return

def use_list_comprehension():
   '
   Create a list comprehension
   A list comprehension has 3 parts
   new_list = [OUTPUT_EXPRESSION ITERATION PREDICATE_EXPRESSION]
   '
   old_things = [0,1,2,3,4,5,6,7,8,9]
   new_things = [ITEM for ITEM in old_things if not(ITEM % 2)]
   pprint.pprint(new_things)
   return

def list_compr_without_predicate():
   old_things = [0,1,2,3,4,5,6,7,8,9]
   new_things = [new  + str(ITEM) for ITEM in old_things]
   pprint.pprint(new_things)
   new_things = [newer {}.format(ITEM) for ITEM in old_things]
   pprint.pprint(new_things)
   return

def main():
   print(Using for loop)
   use_for_loop()
   print(Using list comprehension)
   use_list_comprehension()
   print(List comprehension without predicate)
   list_compr_without_predicate()

if __name__ == __main__:
   main() 
