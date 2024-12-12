class Key:
    def __init__(self, value = None):
        self.value = value

    def set(self, value):
        self.value = value

    def __str__(self):
        return f"Ключ: {self.value}"



class KeyTritemia(Key):
    def __init__(self, value = None):
        super(KeyTritemia, self).__init__()


class CryptoSystem:
    def __init__(self, key = None):
        self.key = key

    def setKey(self, key):
        self.key = key

    def encrypt(self, string):
        pass

    def decrypt(self, string):
        pass


class CryptoSystemTritemia(CryptoSystem):
    def __init__(self, key = None):
        super(CryptoSystemTritemia, self).__init__()

    def encrypt(self, string):
        rus_slovar = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ё': 6, 'Ж': 7, 'З': 8, 'И': 9, 'Й': 10, 'К': 11,
                'Л': 12, 'М': 13, 'Н': 14, 'О': 15, 'П': 16,  'Р': 17,  'С': 18,  'Т': 19,  'У': 20,  'Ф': 21,  'Х': 22,
                      'Ц': 23,  'Ч': 24, 'Ш': 25, 'Щ': 26,  'Ъ': 27,  'Ы': 28,  'Ь': 29,  'Э': 30,  'Ю': 31,  'Я': 32,
                      ' ': 33, '.': 34, ',': 35, '!': 36, 'а': 37, 'б': 38, 'в': 39, 'г': 40, 'д': 41, 'е': 42, 'ё': 43,
                      'ж': 44, 'з': 45, 'и': 46, 'й': 47, 'к': 48, 'л': 49, 'м': 50, 'н': 51, 'о': 52, 'п': 53,  'р': 54,
                      'с': 55,  'т': 56,  'у': 57,  'ф': 58,  'х': 59, 'ц': 60,  'ч': 61, 'ш': 62, 'щ': 63,  'ъ': 64,
                      'ы': 65,  'ь': 66,  'э': 67,  'ю': 68,  'я': 69, ':': 70, ';': 71, '&': 72, '$': 73, '#': 74,
                      '№': 75, '@': 76, '"': 77, "'": 78, ')': 79, '(': 80, '+': 81, '-': 82, '*':83, '{': 84, '}': 85,
                      '/': 86, ']': 87, '[': 88, 'a': 89, 'b': 90, 'c': 91, 'd': 92, 'e': 93, 'f': 94, 'g': 95, 'h': 96,
                      'i': 97, 'j': 98, 'k': 99, 'l': 100, 'm': 101, 'n': 102, 'o': 103, 'p': 104, 'q': 105, 'r': 106,
                      's': 107, 't': 108, 'u': 109, 'v': 110, 'w': 111, 'x': 112, 'y': 113, 'z': 114, 'B': 115, 'C': 116,
                      'D': 117, 'E': 118, 'F': 119, 'G': 120, 'H': 121, 'I': 122, 'J': 123, 'K': 124, 'L': 125, 'M': 126,
                      'N': 127, 'O': 128, 'P': 129, 'Q': 130, 'R': 131, 'S': 132, 'T': 133, 'U': 134, 'V': 135, 'W': 136,
                      'X': 137,'Y': 138, 'Z': 139, '1': 140, '2': 141, '3': 142, '4': 143, '5': 144, '6': 145, '7': 146,
                      '8': 147, '9': 148, '0': 149, 'A': 150, '?': 151, '_': 152}
        new_string = str()
        for x in range(len(string)):
            if string[x] == '\x14':
                new_string += '\x14'
                continue
            if string[x] == '\x15':
                new_string += '\x15'
                continue
            if string[x] != '\n':
                    m = rus_slovar[string[x]]
                    k = 2 * x ** 2 + 5 * x + 3
                    l = (m + k) % (len(rus_slovar))
                    for i in rus_slovar.items():
                        if l in i:
                            new_string += i[0]
            else:
                new_string += '\n'
        return new_string

    def decrypt(self, string):
        rus_slovar = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ё': 6, 'Ж': 7, 'З': 8, 'И': 9, 'Й': 10, 'К': 11,
                      'Л': 12, 'М': 13, 'Н': 14, 'О': 15, 'П': 16, 'Р': 17, 'С': 18, 'Т': 19, 'У': 20, 'Ф': 21, 'Х': 22,
                      'Ц': 23, 'Ч': 24, 'Ш': 25, 'Щ': 26, 'Ъ': 27, 'Ы': 28, 'Ь': 29, 'Э': 30, 'Ю': 31, 'Я': 32,
                      ' ': 33, '.': 34, ',': 35, '!': 36, 'а': 37, 'б': 38, 'в': 39, 'г': 40, 'д': 41, 'е': 42, 'ё': 43,
                      'ж': 44, 'з': 45, 'и': 46, 'й': 47, 'к': 48, 'л': 49, 'м': 50, 'н': 51, 'о': 52, 'п': 53, 'р': 54,
                      'с': 55, 'т': 56, 'у': 57, 'ф': 58, 'х': 59, 'ц': 60, 'ч': 61, 'ш': 62, 'щ': 63, 'ъ': 64,
                      'ы': 65, 'ь': 66, 'э': 67, 'ю': 68, 'я': 69, ':': 70, ';': 71, '&': 72, '$': 73, '#': 74,
                      '№': 75, '@': 76, '"': 77, "'": 78, ')': 79, '(': 80, '+': 81, '-': 82, '*': 83, '{': 84, '}': 85,
                      '/': 86, ']': 87, '[': 88, 'a': 89, 'b': 90, 'c': 91, 'd': 92, 'e': 93, 'f': 94, 'g': 95, 'h': 96,
                      'i': 97, 'j': 98, 'k': 99, 'l': 100, 'm': 101, 'n': 102, 'o': 103, 'p': 104, 'q': 105, 'r': 106,
                      's': 107, 't': 108, 'u': 109, 'v': 110, 'w': 111, 'x': 112, 'y': 113, 'z': 114, 'B': 115,
                      'C': 116, 'D': 117, 'E': 118, 'F': 119, 'G': 120, 'H': 121, 'I': 122, 'J': 123, 'K': 124, 'L': 125,
                      'M': 126, 'N': 127, 'O': 128, 'P': 129, 'Q': 130, 'R': 131, 'S': 132, 'T': 133, 'U': 134, 'V': 135,
                      'W': 136, 'X': 137, 'Y': 138, 'Z': 139, '1': 140, '2': 141, '3': 142, '4': 143, '5': 144, '6': 145,
                      '7': 146, '8': 147, '9': 148, '0': 149, 'A': 150, '?': 151, '_': 152}
        new_string = str()
        for x in range(len(string)):
            if string[x] == '\x14':
                new_string += '\x14'
                continue
            if string[x] == '\x15':
                new_string += '\x15'
                continue
            if string[x] != '\n':
                    k = 2 * x ** 2 + 5 * x + 3
                    for i in rus_slovar.items():
                        if string[x] in i:
                            l = i[1]
                    parametr = l - k
                    m = parametr % len(rus_slovar)
                    for i in rus_slovar.items():
                        if m in i:
                            new_string += i[0]
            else:
                new_string += '\n'
        return new_string


class CryptoManager:
    def __init__(self, crypto = None):
        self.crypto = crypto

    def setCrypto(self, crypto):
        self.crypto = crypto

    def encryptFile(self, inputFileName, outputFileName):
        f1 = open(inputFileName, 'r+', encoding='windows-1251')
        f2 = open(outputFileName, 'w+')
        string = f1.readlines()
        for x in string:
            a = self.crypto.encrypt(x)
            f2.write(a)
        f1.close()
        f2.close()

    def decryptFile(self, inputFileName, outputFileName):
        f1 = open(inputFileName, 'r+', encoding='windows-1251')
        f2 = open(outputFileName, 'w+')
        string = f1.readlines()
        for x in string:
            a = self.crypto.decrypt(x)
            f2.write(a)
        f1.close()
        f2.close()

    def encryptString(self, string):
        return self.crypto.encrypt(string)

    def decryptString(self, string):
        return self.crypto.decrypt(string)

cm = CryptoManager()
k = KeyTritemia(4)
cm.setCrypto(CryptoSystemTritemia(k))
cm.encryptFile("C:/Users/rvapv/Downloads/postman.txt_Ascii.txt", "output.txt")
cm.decryptFile("output.txt", "output2.txt")