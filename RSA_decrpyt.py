c = int(input('Ciphertext: '))
p = int(input('First factor: '))
q = int(input('Second factor: '))
e = int(input('Public value: '))
n = p*q

phi = (p-1)*(q-1)
d = pow(e, -1, phi)

m = pow(c, d, n)
hex_str = hex(m)[2:]
if len(hex_str) % 2:
    hex_str = '0' + hex_str
plaintext = bytearray.fromhex(hex_str).decode()

print(f"d = {d}")
print(f"plaintext (int) = {m}")
print(f"plaintext (text) = {plaintext}")