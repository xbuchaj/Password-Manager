'''
        cypher.py - v1.0 - developed by xbuchaj in 2023        
This script contains all the important functions for encryption 
and decryption using the AES-128 cipher, as well as a function 
for generating a 128-bit key for the given cipher.
All functions can be used independently without the need for other 
libraries (except the 'random' library) and without the need for 
other source codes.
I hope that I have understood the whole principle of encryption 
enough to make encryption safe with the functions I have created.

LICENSE:
Copyright 2023 @xbuchaj
Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
'''

from libraries.configparserLib import ConfigParser
import libraries.randomLib as random

subtitutionBytes = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]

Rcon = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1b, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00],
]

GaloisField = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

invGaloisField = [
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
]

def keyGen():
    '''
    A function that creates a 128-bit key and write them in the config.ini
    file.
    '''
    key = ""
    for counter in range(128):
        key = key + str(random.randrange(0,2))
    key = hex(int(key, base = 2))
    while len(key) < 34:
        key = key[:2] + "0" + key[2:] 
    configObject = ConfigParser()
    configObject["KEY"] = {
        "key": key 
    }
    with open('database/config.ini', 'w') as config:
        configObject.write(config)

def padding(inputData):
    '''
    The function converts input data from text form to hexadecimal form. If 
    there are insufficient number of hexadecimal numbers after division, it 
    will assign the value 0x20. But if there are more than necessary after 
    dividing the hexadecimal numbers, it creates additional values.
    Parameters:
        inputData (str): input data in text form
    Returns:
        list: list with created strings of hexadecimal data
    '''
    outputData = []

    while True:
        hexForm = "0x"

        if len(inputData) < 16:
            for i in range(16):
                if len(inputData) > 0:
                    hexCharacter = hex(ord(inputData[0]))
                    if len(hexCharacter) == 4:
                        hexForm = hexForm + hexCharacter[2] + hexCharacter[3]
                    else:
                        hexForm = hexForm + "0" + hexCharacter[2]
                    inputData = inputData.replace(inputData[0], "", 1)
                else:
                    hexForm = hexForm + "20"
            outputData.append(hexForm)
            return outputData
        
        if len(inputData) == 16:
            for i in range(16):
                if len(inputData) > 0:
                    hexCharacter = hex(ord(inputData[0]))
                    if len(hexCharacter) == 4:
                        hexForm = hexForm + hexCharacter[2] + hexCharacter[3]
                    else:
                        hexForm = hexForm + "0" + hexCharacter[2]
                    inputData = inputData.replace(inputData[0], "", 1)
                else:
                    hexForm = hexForm + "20"
            outputData.append(hexForm)

            hexForm = "0x"
            hexForm = hexForm + (16 * "20")
            outputData.append(hexForm)
            return outputData

        if len(inputData) > 16:
            for i in range(16):
                hexCharacter = hex(ord(inputData[0]))
                if len(hexCharacter) == 4:
                    hexForm = hexForm + hexCharacter[2] + hexCharacter[3]
                else:
                    hexForm = hexForm + "0" + hexCharacter[2]
                inputData = inputData.replace(inputData[0], "", 1)
            outputData.append(hexForm)    

def toMatrix(data):
    '''
    The function divides the input data in hexadecimal form after padding 
    into a 4x4 matrix. If there is more input data, it will create more 
    matrices.
    Parameters:
        data (list): list of data in hexadecimal form
    Returns:
        list: list with created matrix / matrices
    '''
    outputData = []

    for i in range(len(data)):
        matrix = []
        for j in range(2, 33, 8):
            matrix.append([(data[i])[j] + (data[i])[j + 1], (data[i])[j + 2] + (data[i])[j + 3], (data[i])[j + 4] + (data[i])[j + 5], (data[i])[j + 6] + (data[i])[j + 7]])
        outputData.append(matrix)
    return outputData

def RotWord(matrix):
    '''
    The function rotates the data in the last column of the matrix. It 
    will rotate so that the first element in the column will be the last, 
    the second will be the first, the third will be the second and the 
    fourth will be the third.
    Parameters:
        matrix (list): matrix with data
    Returns:
        list: matrix with rotate data in the last column
    '''
    flag = matrix[0][len(matrix[0]) - 1]
    matrix[0][len(matrix[0]) - 1] = matrix[1][len(matrix[0]) - 1]
    matrix[1][len(matrix[0]) - 1] = matrix[2][len(matrix[0]) - 1]
    matrix[2][len(matrix[0]) - 1] = matrix[3][len(matrix[0]) - 1]
    matrix[3][len(matrix[0]) - 1] = flag
    return matrix

def ShiftRow(matrix, indexRow):
    '''
    The function rotates the data in the row with parameter's index of 
    the matrix. It will rotate so that the first element in the row will 
    be the last, the second will be the first, the third will be the 
    second and the fourth will be the third.
    Parameters:
        matrix (list): matrix with data
        indexRow (int): index of row where you need rotate the data
    Returns:
        list: matrix with rotate data in the row
    '''
    flag = matrix[indexRow][0]
    matrix[indexRow][0] = matrix[indexRow][1]
    matrix[indexRow][1] = matrix[indexRow][2]
    matrix[indexRow][2] = matrix[indexRow][3]
    matrix[indexRow][3] = flag
    return matrix

def subBytes(matrix):
    '''
    The function performs data substitution with data in the substitutionBytes 
    list. The first number of the hexadecimal number indicates the row of the 
    element and the second number indicates the column of the element in the 
    substitutionBytes list.
    Parameters:
        matrix (list): matrix with data
    Returns:
        list: matrix with new data after substitution
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sub = str(hex(subtitutionBytes[int(str(matrix[i][j])[0], base = 16)][int(str(matrix[i][j])[1], base = 16)]))
            if len(sub) == 4:
                matrix[i][j] = sub[2] + sub[3]
            else:
                matrix[i][j] = "0" + sub[2]
    return matrix

def invSubBytes(matrix):
    '''
    The function performs an inverse data substitution with the data position 
    in the substitutionBytes list. The row position in hexadecimal is the first 
    number and the column position in hexadecimal is the second number of the 
    new data.
    Parameters:
        matrix (list): matrix with data
    Returns:
        list: matrix with new data after inverse substitution
    '''
    position = None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            search = int(matrix[i][j], base = 16)
            for k in range(len(subtitutionBytes)):
                for l in range(len(subtitutionBytes[k])):
                    if subtitutionBytes[k][l] == search:
                        position = hex(k)[2] + hex(l)[2]
            matrix[i][j] = position
    return matrix

def KeySchedule():
    '''
    The function calculates ten keys (each key for one round of encryption / decryption) 
    derived from the master key and from previously calculated ones. It puts all the 
    keys in the list in hexadecimal form.
    Returns:
        list: list with round keys
    '''
    configFile = ConfigParser()
    configFile.read("database/config.ini")
    reader = configFile["KEY"]
    cipherKey = reader["key"]
    outputRoundKeys = []
    
    for scheduleRound in range(10):
        column = [[cipherKey[8] + cipherKey[9]], [cipherKey[16] + cipherKey[17]], [cipherKey[24] + cipherKey[25]], [cipherKey[32] + cipherKey[33]]]
        column = RotWord(column)
        column = subBytes(column)

        xorColumn = [[cipherKey[2] + cipherKey[3]], [cipherKey[10] + cipherKey[11]], [cipherKey[18] + cipherKey[19]], [cipherKey[26] + cipherKey[27]]]
        for i in range(4):
            calc = hex(int(column[i][0], base = 16) ^ int(xorColumn[i][0], base = 16) ^ Rcon[scheduleRound][i])
            if len(calc) == 4:
                column[i][0] = calc[2] + calc[3]
            else:
                column[i][0] = "0" + calc[2]
        keyArray = column

        xorColumn = [[cipherKey[4] + cipherKey[5]], [cipherKey[12] + cipherKey[13]], [cipherKey[20] + cipherKey[21]], [cipherKey[28] + cipherKey[29]]]
        for i in range(4):
            calc = hex(int(keyArray[i][0], base = 16) ^ int(xorColumn[i][0], base = 16))
            if len(calc) == 4:
                keyArray[i].append(calc[2] + calc[3])
            else:
                keyArray[i].append("0" + calc[2])

        xorColumn = [[cipherKey[6] + cipherKey[7]], [cipherKey[14] + cipherKey[15]], [cipherKey[22] + cipherKey[23]], [cipherKey[30] + cipherKey[31]]]
        for i in range(4):
            calc = hex(int(keyArray[i][1], base = 16) ^ int(xorColumn[i][0], base = 16))
            if len(calc) == 4:
                keyArray[i].append(calc[2] + calc[3])
            else:
                keyArray[i].append("0" + calc[2])

        xorColumn = [[cipherKey[8] + cipherKey[9]], [cipherKey[16] + cipherKey[17]], [cipherKey[24] + cipherKey[25]], [cipherKey[32] + cipherKey[33]]]
        for i in range(4):
            calc = hex(int(keyArray[i][2], base = 16) ^ int(xorColumn[i][0], base = 16))
            if len(calc) == 4:
                keyArray[i].append(calc[2] + calc[3])
            else:
                keyArray[i].append("0" + calc[2])
        
        key = "0x"
        for i in range(4):
            for j in range(4):
                key = key + str(keyArray[i][j])
        cipherKey = key
        outputRoundKeys.append(key)
    return outputRoundKeys

def galoisMult(a, b):
    """
    The function performs the multiplication of two hexadecimal numbers. If the resulting 
    number has more than eight bits, it performs a bit shift.
    Parameters:
        a (int / hex): first number
        a (int / hex): second number
    """
    p = 0
    hi_bit_set = 0
    for i in range(8):
        if b & 1 == 1: p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set == 0x80: a ^= 0x1b
        b >>= 1
    return p % 256

def encryption(data):
    '''
    The function encrypts the input hexadecimal data and returns a list of all encrypted 
    input data (if there is more than one). AES-128 standard is used for encryption.
    Parameters:
        data (list): list with data in hexadecimal form
    Returns:
        list: list with encrypted data in hexadecimal form
    '''
    state = toMatrix(padding(data))
    cipherKey = toMatrix(KeySchedule())

    for encryptionRound in range(10):

        for inputArray in range(len(state)):

            currentState = subBytes(state[inputArray])

            currentState = ShiftRow(currentState, 1)
            for counter in range(2):
                currentState = ShiftRow(currentState, 2)
            for counter in range(3):
                currentState = ShiftRow(currentState, 3)
            
            for i in range(4):
                column = [int(currentState[0][i], base = 16), int(currentState[1][i], base = 16), int(currentState[2][i], base = 16), int(currentState[3][i], base = 16)]
                for j in range(4):
                    calc = hex(galoisMult(column[0], GaloisField[j][0]) ^ galoisMult(column[1], GaloisField[j][1]) ^ galoisMult(column[2], GaloisField[j][2]) ^ galoisMult(column[3], GaloisField[j][3]))
                    if len(calc) == 4:
                        currentState[j][i] = calc[2] + calc[3]
                    else:
                        currentState[j][i] = "0" + calc[2]

            for i in range(4):
                for j in range(4):
                    calc = hex(int(currentState[i][j], base = 16) ^ int(cipherKey[encryptionRound][i][j], base = 16))
                    if len(calc) == 4:
                        currentState[i][j] = calc[2] + calc[3]
                    else:
                        currentState[i][j] = "0" + calc[2]
            state[inputArray] = currentState
    
    outputHex = []
    for i in range(len(state)):
        oneArrayString = "0x"
        for j in range(4):
            for k in range(4):
                oneArrayString = oneArrayString + str(state[i][j][k])
        outputHex.append(oneArrayString)      
    return outputHex

def decryption(data):
    '''
    The function decrypts the input hexadecimal data and returns a string with the decrypted 
    input data. The reverse encryption method using the AES-128 standard is used for 
    decryption.
    Parameters:
        data (list): list with encrypted data in hexadecimal form
     Returns:
        string: string with decrypted data in text form
    '''
    state = toMatrix(data)
    cipherKey = toMatrix(KeySchedule())

    for decryptionRound in range(9, -1, -1):

        for inputArray in range(len(state)):

            currentState = state[inputArray]

            for i in range(4):
                for j in range(4):
                    calc = hex(int(currentState[i][j], base = 16) ^ int(cipherKey[decryptionRound][i][j], base = 16))
                    if len(calc) == 4:
                        currentState[i][j] = calc[2] + calc[3]
                    else:
                        currentState[i][j] = "0" + calc[2]

            for i in range(4):
                column = [int(currentState[0][i], base = 16), int(currentState[1][i], base = 16), int(currentState[2][i], base = 16), int(currentState[3][i], base = 16)]
                for j in range(4):
                    calc = hex(galoisMult(column[0], invGaloisField[j][0]) ^ galoisMult(column[1], invGaloisField[j][1]) ^ galoisMult(column[2], invGaloisField[j][2]) ^ galoisMult(column[3], invGaloisField[j][3]))
                    if len(calc) == 4:
                        currentState[j][i] = calc[2] + calc[3]
                    else:
                        currentState[j][i] = "0" + calc[2]

            for counter in range(3):
                currentState = ShiftRow(currentState, 1)
            for counter in range(2):
                currentState = ShiftRow(currentState, 2)
            currentState = ShiftRow(currentState, 3)

            currentState = invSubBytes(currentState)

            state[inputArray] = currentState
    
    outputText = ""
    for inputArray in range(len(state)):
        for i in range(len(state[inputArray])):
            for j in range(len(state[inputArray][i])):
                outputText = outputText + chr(int(state[inputArray][i][j], base = 16))
    formatOutputText = outputText[0]
    for index in range(1, len(outputText) - 1):
        if ((outputText[index - 1] != " ") and (outputText[index] == " ") and (outputText[index + 1] != " ")) or (outputText[index] != " "):
            formatOutputText = formatOutputText + outputText[index]
        elif outputText[index] == " ":
            pass
    return formatOutputText