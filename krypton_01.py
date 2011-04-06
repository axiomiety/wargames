#!/usr/bin/python

CYPHERTEXT="YRIRY GJB CNFFJBEQ EBGGRA"

def main():
  print "Krypton Level 2"
  print "--------------"
  # rot13

  # generate [A..Z]
  alphabet = map(chr, range(65,91))
  for c in CYPHERTEXT:
    if c != ' ':
      print alphabet[(ord(c)-65 +13)%26],
    else:
      print ' '

if __name__ == "__main__":
  main()
