from RSAnum import RSAnumberGenerator 

subBytes = [
    ["63", "CA", "B7", "04", "09", "53", "D0", "51", "CD", "60", "E0", "E7", "BA", "70", "E1", "8C"],
    ["7C", "82", "FD", "C7", "83", "D1", "EF", "A3", "0C", "81", "32", "C8", "78", "3E", "F8", "A1"],
    ["77", "C9", "93", "23", "2C", "00", "AA", "40", "13", "4F", "3A", "37", "25", "B5", "98", "89"],
    ["7B", "7D", "26", "C3", "1A", "ED", "FB", "8F", "EC", "DC", "0A", "6D", "2E", "66", "11", "0D"],
    ["F2", "FA", "36", "18", "1B", "20", "43", "92", "5F", "22", "49", "8D", "1C", "48", "69", "BF"],
    ["6B", "59", "3F", "96", "6E", "FC", "4D", "9D", "97", "2A", "06", "D5", "A6", "03", "D9", "E6"],
    ["6F", "47", "F7", "05", "5A", "B1", "33", "38", "44", "90", "24", "4E", "B4", "F6", "8E", "42"],
    ["C5", "F0", "CC", "9A", "A0", "5B", "85", "F5", "17", "88", "5C", "A9", "C6", "0E", "94", "68"],
    ["30", "AD", "34", "07", "52", "6A", "45", "BC", "C4", "46", "C2", "6C", "E8", "61", "9B", "41"],
    ["01", "D4", "A5", "12", "3B", "CB", "F9", "B6", "A7", "EE", "D3", "56", "DD", "35", "1E", "99"],
    ["67", "A2", "E5", "80", "D6", "BE", "02", "DA", "7E", "B8", "AC", "F4", "74", "57", "87", "2D"],
    ["2B", "AF", "F1", "E2", "B3", "39", "7F", "21", "3D", "14", "62", "EA", "1F", "B9", "E9", "0F"],
    ["FE", "9C", "71", "EB", "29", "4A", "50", "10", "64", "DE", "91", "65", "4B", "86", "CE", "B0"],
    ["D7", "A4", "D8", "27", "E3", "4C", "3C", "FF", "5D", "5E", "95", "7A", "BD", "C1", "55", "54"],
    ["AB", "72", "31", "B2", "2F", "58", "9F", "F3", "19", "0B", "E4", "AE", "8B", "1D", "28", "BB"],
    ["76", "C0", "15", "75", "84", "CF", "A8", "D2", "73", "DB", "79", "08", "8A", "9E", "DF", "16"]
]

Rcon = [
    ["01", "00", "00", "00"],
    ["02", "00", "00", "00"],
    ["04", "00", "00", "00"],
    ["08", "00", "00", "00"],
    ["10", "00", "00", "00"],
    ["20", "00", "00", "00"],
    ["40", "00", "00", "00"],
    ["80", "00", "00", "00"],
    ["1B", "00", "00", "00"],
    ["36", "00", "00", "00"],
]

def padding(inputData):
    # Variable for input in hex code
    inputHex = []
    while True:
        # Write hex code of the input to the array
        # If lenght of input is less than 16, than hex code is only in one array and while lenght of array is less than 16 is use padding 
        if len(inputData) < 16:
            outputData = []
            for i in range(len(inputData)):
                outputData.append(hex(ord(inputData[i])))
            add = 16 - len(inputData)
            for i in range(add):
                outputData.append(hex(add))
            inputHex.append(outputData)
            break
        # If lenght of input is less 16, than hex code is in two array and in the second array is use padding 
        elif len(inputData) == 16:
            outputData = []
            for i in range(len(inputData)):
                outputData.append(hex(ord(inputData[i])))
            inputHex.append(outputData)
            outputData = []
            for i in range(16):
                outputData.append(hex(16))
            inputHex.append(outputData)
            break
        # If lenght of input is more than 16, than hex code is in more array devide in lenght 16 and in the last array is use padding 
        elif len(inputData) > 16:
            outputData = []
            for i in range(16):
                outputData.append(hex(ord(inputData[0])))
                inputData = inputData.replace(inputData[0], "", 1)
            inputHex.append(outputData)
    # Devide hex code of input to the 4x4 matrixes
    inputHexMatrix = []
    for i in range(len(inputHex)):
        oneMatrix = []
        oneRow = []
        x = 3
        for j in range(len(inputHex[i])):
            oneRow.append(inputHex[i][j])
            if j == x:
                x += 4
                oneMatrix.append(oneRow)
                oneRow = []
        inputHexMatrix.append(oneMatrix)

    return inputHexMatrix