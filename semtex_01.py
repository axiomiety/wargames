#!/usr/bin/python
import socket
import struct
HOST='semtex.labs.overthewire.org'
PORT=24000 # x86/elf

# REFRENCES:
# http://docs.python.org/tutorial/inputoutput.html

def main():
  print "Semtex Level 1"
  print "--------------"
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST,PORT))
  myfile = open("semtex1.bin","wb")
  flag = True
  while 1:
    data = s.recv(1) # silly. but it works
    if not data: break
    if flag:
      myfile.write(data)
      flag = False
    else:
      flag = True

  myfile.close()
  s.close()

if __name__ == "__main__":
  main()
