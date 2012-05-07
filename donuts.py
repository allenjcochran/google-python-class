#!/usr/bin/python -tt
# Copyright 2010 Google Inc.

import sys

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) <= 9:
    name = sys.argv[1]
    print 'The number of donuts', sys.argv[1]
  if len(sys.argv) >= 9:
  	name = sys.argv[1]
  	print 'The number of donuts', 'many'
  else:
    name = 'I don\'t know how many donuts you are talking about'
  print 'How many Donuts\?', name

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()