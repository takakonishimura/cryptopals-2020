"""
Convert hex to base64

######## -> a hex symbol
The string:
`49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d`

###### -> base64 symbol
Should produce:
`SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t`
"""

import conversion

def convertHexToBase64(hexStr:str) -> str:
    output = ''
    while len(hexStr) > 0:
        lastThree = hexStr[-3:]
        hexStr = hexStr[:-3]
        while len(lastThree) < 3: lastThree = '0' + lastThree

        bin_substr = conversion.binForHex[lastThree[0]] + conversion.binForHex[lastThree[1]] + conversion.binForHex[lastThree[2]]
        output = conversion.base64ForBin[bin_substr[0:6]] + conversion.base64ForBin[bin_substr[6:12]] + output

    return output


if __name__ == '__main__':
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    print('input: {}'.format(input))
    print('output: {}'.format(convertHexToBase64(input)))
    print('expected: {}'.format(expected))