#!/usr/bin/python
import sys

CYPHERTEXT="OMQEMDUEQMEK"

def main():
  print "Krypton Level 3"
  print "--------------"
 
  # for lev3, the shit is 14 - but the password is in lower case
  shift = int(sys.argv[1])
  # generate [A..Z]
  alphabet = map(chr, range(65,91))
  for c in CYPHERTEXT:
    if c != ' ':
      print alphabet[(ord(c)-65 +shift)%26],
    else:
      print ' '

if __name__ == "__main__":
  main()
