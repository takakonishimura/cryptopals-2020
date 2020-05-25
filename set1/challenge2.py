"""
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
`1c0111001f010100061a024b53535009181c`

... after hex decoding, and when XOR'd against:
`686974207468652062756c6c277320657965`

... should produce:
`746865206b696420646f6e277420706c6179`
"""
import conversion

def fixedHexXOR(input1:str, input2:str):
    output = ''
    for i in range(len(input1)):
        bin1 = conversion.binForHex[input1[i]]
        bin2 = conversion.binForHex[input2[i]]
        fourbits = ''

        for i in range(4):
            bit1 = bin1[i] == '1'
            bit2 = bin2[i] == '1'
            bit = (bit1 or bit2) and (not bit1 or not bit2)
            fourbits = fourbits + ('1' if bit else '0')
        output = output + conversion.hexForBin[fourbits]
        
    return output

if __name__ == '__main__':
    input1 = '1c0111001f010100061a024b53535009181c'
    input2 = '686974207468652062756c6c277320657965'
    expected = '746865206b696420646f6e277420706c6179'

    print('input1: {}'.format(input1))
    print('input1: {}'.format(input2))
    print('output: {}'.format(fixedHexXOR(input1, input2)))
    print('expected: {}'.format(expected))
