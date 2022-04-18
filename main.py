import jbcrypt

msg = input("MSG: ")
encrypted = jbcrypt.encrypt(msg)
decrypted = jbcrypt.decrypt(msg)
print(msg)
print(encrypted)
print(decrypted)
