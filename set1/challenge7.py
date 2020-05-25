"""
AES in ECB mode

The Base64-encoded content in this file has been encrypted via AES-128 in ECB mode under the key `YELLOW SUBMARINE`.
(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
"""

from Crypto.Cipher import AES
import base64

if __name__ == "__main__":
    KEY = b"YELLOW SUBMARINE"

    with open("set1/seven.txt", "r") as f:
        cipherText = base64.b64decode(f.read())

    cipher = AES.new(KEY, AES.MODE_ECB)
    plaintext = cipher.decrypt(cipherText)

    print(plaintext.decode('utf-8'))
