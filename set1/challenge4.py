"""
Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""
def fixedByteStringXOR(cipherBytes, xorByte):
    output = b''
    for byte in cipherBytes:
        output += bytes([byte ^ xorByte])

    return output

freq ={
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
        output = fixedByteStringXOR(cipherText, i)
        freqScoreChart.append((i, freqScore(output), output))
    return sorted(freqScoreChart, key = lambda x: x[1], reverse=True)[0]

if __name__ == '__main__':
    with open("set1/four.txt", "r") as f:
        finalScoreChart = list()

        for l, line in enumerate(f): 
            finalScoreChart.append(bruteForce(bytes.fromhex(line)))

        (key, score, plaintext) = sorted(finalScoreChart, key = lambda x: x[1], reverse=True)[0]

        print('xorkey: {}, score: {}, plaintext: {}'.format(key, score, plaintext))
