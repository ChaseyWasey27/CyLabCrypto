from gmpy2 import iroot
e = int(input('public key: '))
n = int(input('value of n: '))
c = int(input('ciphertext: '))

m = iroot(c, e)

m_hex = hex(m)[2:]
if len(m_hex) % 2:
    m_hex= '0' + m_hex
plaintext = bytearray.fromhex(m_hex).decode()

print(f"plaintext (int) = {m}")
print(f"plaintext (text) = {plaintext}")