"""
Detect AES in ECB mode

In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
"""

from Crypto.Cipher import AES
import base64

if __name__ == "__main__":
#    KEY = b"YELLOW SUBMARINE"

    with open("set1/eight.txt", "r") as f:
        cipherTexts = [bytes.fromhex(line) for line in f]

        for i,line in enumerate(cipherTexts):
#            print(line)
            segments = set()
            while(len(line)):
                (segment, line) = (line[0:16], line[16:])
                if (segment in segments): print('Line {} has a REPEAT: {}'.format(i, segment))
                else: segments.add(segment)

        print('line 133: {}'.format(cipherTexts[132]))