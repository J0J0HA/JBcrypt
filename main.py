import jbcrypt

msg = input("MSG: ")
encrypted = jbcrypt.encode(msg)
decrypted = jbcrypt.decode(msg)
print("MSG", msg)
print("ENC", encrypted)
print("DEC", decrypted)
