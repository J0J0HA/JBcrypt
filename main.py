import jbcrypt

msg = input("MSG: ")
for i in range(100):
    encrypted = jbcrypt.encode(msg, rxl=10)
    print("ENC", encrypted)
encrypted = jbcrypt.encode(msg, rxl=10)
decrypted = jbcrypt.decode(encrypted)
print("DEC", decrypted)
