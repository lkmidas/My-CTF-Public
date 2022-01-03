from malduck import *

def RC4_gen_stream(data, key):
    S = list(range(256))
    j = 0
    out = b""
    #KSA Phase
    for i in range(256):
        j = (j + S[i] + key[i % len(key)] ) % 256
        S[i] , S[j] = S[j] , S[i]

    #PRGA Phase
    i = j = 0
    x = 0
    for b in data:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        rnd = S[(S[i] + S[j]) % 256]
        out += p8(rnd)
    return out

#data = [194, 70, 82, 103, 8, 95, 185, 247, 153, 22, 82, 34, 71, 77, 78, 240, 105, 6, 80, 79, 196, 187, 238, 159, 67, 233, 202, 140, 51, 199, 122, 92, 65, 126, 98, 133, 205, 109, 100, 10, 22, 81, 151, 71, 193, 116, 158, 67]
data = [b for b in b"0_4nd_w3lc0m3_t0_th3_w0rld_0f_0bfusc4ti0n_gratzz"]
key = b"hO7nMqKeFYv9VVAS7qlX"
result = b""

stream = RC4_gen_stream(data, key)
# DEC
# x = 0
# for i in range(len(data)):
#    result += p8(((data[i] - stream[i]) & 0xff) ^ stream[i] ^ x)
#    x = stream[i]

# ENC
x = 0
for i in range(len(data)):
    result += p8(((data[i] ^ stream[i] ^ x) + stream[i]) & 0xff)
    x = stream[i]

print(result)
for i in range(len(result)):
    print("{}".format(hex(result[i])), end=" ")