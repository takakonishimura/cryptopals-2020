"""
Single-byte XOR cipher

The hex encoded string:
`1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736`

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
"""

def fixedByteStringXOR(cipherBytes, xorByte):
    output = b''
    for byte in cipherBytes:
        output = output + bytes([byte ^ xorByte])
    
    return output

def majorityRealLetters(inputBytes, threshold):
    counter = 0
    for byte in inputBytes:
        if (byte == 32) or (byte >= 65 and byte <= 90) or (byte >= 97 and byte <= 122): counter = counter + 1

    if (counter > len(inputBytes) * threshold): return True
    return False

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

if __name__ == '__main__':
    input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    inputAsBytes = bytes.fromhex(input)

    print('----------Tay\'s Solution:----------')
    for i in range(255):
        output = fixedByteStringXOR(inputAsBytes, i)
        if majorityRealLetters(output, .95):
            print('Choice: {}'.format(chr(i)))
            print(output)

    print('----------Matt\'s Solution:----------')
    freqScoreChart = dict()
    for i in range(255):
        output = fixedByteStringXOR(inputAsBytes, i)
        freqScoreChart[i] = freqScore(output)

    topChoice = sorted(freqScoreChart, key = lambda x: freqScoreChart[x], reverse=True)[0]
    print('Top Choice: {}'.format(chr(topChoice)))
    print(fixedByteStringXOR(inputAsBytes, topChoice))
