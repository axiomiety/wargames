#!/usr/bin/python
import sys
from operator import itemgetter
import getopt

# REFERENCES:
# http://wiki.python.org/moin/HowTo/Sorting/
# http://docs.python.org/library/getopt.html
# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

def usage():
  print "-f for frequency analysis, -i <inputFile>, -r 'A=M,D=F'"

def main():
  print "Krypton Level 4"
  print "--------------"

  try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:r:f", ["help","input=","replace=","frequency"])
  except getopt.GetoptError, err:
    print str(err) # will print something like "option -a not recognized"
    usage()
    sys.exit(2)
  
  inputFile = None;
  # we first parse for the input file
  #TODO: there must be a better way to do this...
  for o, a in opts:
    if o == "-h":
      usage()
      sys.exit(1)
    elif o in ("-i", "--input"):
      inputFile = a

  for o, a in opts:
    if o in ("-f", "--freq"): 
      freq(inputFile)
    elif o in ("-r", "--replace"):
      replace(inputFile,a)
  
def replace(inputFile, charSet):
  RED = '\033[91m'
  ENDC = '\033[0m'
  for line in open(inputFile,'r'):
    for (oldChar,newChar) in map(lambda x: x.split('='),charSet.split(',')):
      line = line.replace(oldChar,RED + newChar + ENDC)
    print line

def freq(inputFile):
  # generate [A..Z]
  alphabet = map(chr, range(65,91))
  freqDict = {}
  for a in alphabet:
    freqDict[a] = 0
  print "file: ", inputFile
  for line in open(inputFile,'r'):
    for c in line:
      if (c in alphabet): # is there a better way to do this?
        freqDict[c] = freqDict[c] + 1 

  for (k, v) in sorted(freqDict.items(), key=itemgetter(1), reverse=True):
    print "%s=%s" % (k, v)

if __name__ == "__main__":
  main()
