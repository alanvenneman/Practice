def getAllTheLetters(begin, end):
    beginNum = ord(begin)
    endNum = ord(end)
    for number in range(beginNum, endNum + 1):
        yield chr(number)
alphabet = getAllTheLetters('a', 'z')
intab = (''.join(alphabet))
outtab = (intab.strip("ab")) + "ab"
print("Mapping {} to {}.".format(intab, outtab))
trantab = str.maketrans(intab, outtab)
phrase = input("Enter phrase to be translated: ")

print (phrase.translate(trantab))
