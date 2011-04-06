#!/usr/bin/python

CYPHERTEXT="OMQEMDUEQMEK"

def main():
  print "Krypton Level 3"
  print "--------------"

  # generate [A..Z]
  alphabet = map(chr, range(65,91))
  for c in CYPHERTEXT:
    if c != ' ':
      print alphabet[(ord(c)-65 +13)%26],
    else:
      print ' '

if __name__ == "__main__":
  main()
