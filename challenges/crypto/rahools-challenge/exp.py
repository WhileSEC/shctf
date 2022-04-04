from pwn import *
p = remote("0.cloud.chals.io", 10294)
p.sendline("3X0TICENGR4MAOGNER")
log.success(p.recvallS())
p.close()
