from Crypto.Cipher import AES
import base64



if __name__ == "__main__":
    KEY = b"YELLOW SUBMARINE"

    with open("set1/seven.txt", "r") as f:
        cipherText = base64.b64decode(f.read())

    cipher = AES.new(KEY, AES.MODE_ECB)
    plaintext = cipher.decrypt(cipherText)

    print(plaintext.decode('utf-8'))
