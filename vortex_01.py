#!/usr/bin/python
import socket
import struct
HOST='vortex.labs.overthewire.org'
PORT=5842

# REFERENCES:
# http://docs.python.org/library/struct.html
#
# OPTIONAL:
# http://www.artima.com/weblogs/viewpost.jsp?thread=4829

def main():
  print "Vortex Level 1"
  print "--------------"
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST,PORT))
  d1=()
  for i in range(4):
    d1=d1+struct.unpack("<I",s.recv(4))
  s.send(struct.pack("<I",sum(d1))) # what if we overflow? what happens next?
  result=s.recv(1024)
  print result

if __name__ == "__main__":
    main()
