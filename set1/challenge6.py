"""
File six.txt has been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

- Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
- Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
    `this is a test`
    and
    `wokka wokka!!!`

    is 37. Make sure your code agrees before you proceed.

- For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
- The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
- Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
- Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
- Solve each block as if it was single-character XOR. You already have code to do this.
- For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.
"""

import base64

def getHammingDistance(cipherBytes, xorBytes):
    return sum([bin(byte ^ xorBytes[i]).count("1") for i,byte in enumerate(cipherBytes)])

freq = {
    'a': 8.497,
    'b': 1.492,
    'c': 2.202,
    'd': 4.253,
    'e': 11.162,
    'f': 2.228,
    'g': 2.015,
    'h': 6.094,
    'i': 7.546,
    'j': 0.153,
    'k': 1.292,
    'l': 4.025,
    'm': 2.406,
    'n': 6.749,
    'o': 7.507,
    'p': 1.929,
    'q': 0.095,
    'r': 7.587,
    's': 6.327,
    't': 9.356,
    'u': 2.758,
    'v': 0.978,
    'w': 2.560,
    'x': 0.150,
    'y': 1.994,
    'z': 0.077,
    ' ': 12
}

def freqScore(inputBytes):
    return sum( [ freq.get(chr(byte), 0) for byte in inputBytes] )

def bruteForce(cipherText):
    freqScoreChart = list()

    for i in range(255):
        output = fixedByteStringXOR(cipherText, [i])
        freqScoreChart.append((i, freqScore(output), output))
    return sorted(freqScoreChart, key = lambda x: x[1], reverse=True)[0]

def fixedByteStringXOR(cipherBytes, xorBytes):
    output = b""
    for i, byte in enumerate(cipherBytes):
        output += bytes([byte ^ xorBytes[i % len(xorBytes)]])

    return output

if __name__ == "__main__":
    print('----------hamming distance----------')
    input1 = b"this is a test"
    input2 = b"wokka wokka!!!"
    expect = 37
    output = getHammingDistance(input1, input2)

    print("input1: {}".format(input1))
    print("input2: {}".format(input2))
    print("expect: {}".format(expect))
    print("output: {}".format(output))

    print('----------long file----------')
    with open("set1/six.txt", "r") as f:
        cipherText = base64.b64decode(f.read())


    hammingScores = list() # keysize, score

    for keysize in range(2, 41):
        distances = list()
        copy = cipherText
        while(len(copy) > keysize*2):
            (sample1, sample2, copy) = (
                copy[0 : keysize],
                copy[keysize : keysize*2],
                copy[keysize*2 :]
            )
            distances.append(getHammingDistance(sample1, sample2)/keysize)

        average = sum(distances)/len(distances)
        hammingScores.append((keysize, average))

    (KEYSIZE, bestKeyScore) = sorted(hammingScores, key = lambda x: x[1])[0]

    print('winning score is size {} with score {}'.format(KEYSIZE, bestKeyScore))

    cipherByKeyIdx = list()
    for _ in range(KEYSIZE): cipherByKeyIdx.append(list())

    for group in zip(*[iter(cipherText)] * KEYSIZE):
        for idx in range(KEYSIZE): cipherByKeyIdx[idx].append(group[idx])

    resultTable = [bruteForce(cipherGroup) for cipherGroup in cipherByKeyIdx]
    key = bytes([res[0] for res in resultTable])

    print('key is: {}'.format(key))

    decipheredText = fixedByteStringXOR(cipherText, key).decode('utf-8')
    print('\nDeciphered Text is:\n\n{}'.format(decipheredText))