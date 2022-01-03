data = open("./child", "rb").read()
print(len(data))
key = b"h3ll"
enc = b""

for i in range(len(data)):
    if i < 4:
        enc += bytes([data[i] ^ key[i % 4]])
    else:
        enc += bytes([data[i] ^ enc[i-4]])
    
for i in range(len(data)):
    print("{}, ".format(hex(enc[i])), end="")
    if i % 16 == 15:
        print("\\")

print()
#open("./child_enc", "wb").write(enc)