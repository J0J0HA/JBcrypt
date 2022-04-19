import jbcrypt

msg = input("MSG: ")
encrypted = jbcrypt.encode(msg)
decrypted = jbcrypt.decode(msg)
print(msg)
print(encrypted)
print(decrypted)
