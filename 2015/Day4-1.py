import math
import hashlib

secret = "iwrupvqb"

i = 0
while True:
    hexDigit = hashlib.md5(str.encode(secret + str(i))).hexdigest()
    if "00000" in hexDigit[:5]:
        print(i)
        break
    i += 1
