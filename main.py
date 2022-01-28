import string

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple


def clear_terminal():
    print(chr(27) + "[2J")


def get_upper_letters():
    result: list = []
    for i in string.ascii_uppercase:
        result.append(i)

    return result


def get_lower_letters():
    result: list = []
    for i in string.ascii_lowercase:
        result.append(i)

    return result


class CesarChiffre:
    s = 0
    char_list: list = []
    animation: bool = True

    def __init__(self, s: int, char_list=None, animation=True):
        """
            inputs:
            s: shift of characters \n
            char_list: list of characters to use.      (default: letters A-Z)
            animation: if it should run an animation while hashing.
        :param s:
        :param char_list:
        :param animation:
        """
        if char_list is None:
            char_list = get_upper_letters()

        self.s = s
        self.char_list = char_list
        self.animation = animation

    def no_anim(self, w: str):

        encoded_hash = ""
        for char in w.upper():
            # new_char = chr((((ord(char) - 65) + self.s) % 26) + 65)
            new_char = self.char_list[(self.char_list.index(char) + self.s) % len(self.char_list)]
            encoded_hash += new_char

        return encoded_hash

    def encode(self, w: str):
        """
            Encodes the word (w) in the cesar chiffre style with the shift (s) and returns it. Also it has a fancy animation.

        :param w:
        :return:
        """
        if not self.animation:
            return self.no_anim(w)

        clear_terminal()

        encoded_hash = ""
        decoded_hash = ""

        for char in w.upper():
            # new_char = chr((((ord(char) - 65) + self.s) % 26) + 65)
            new_char = self.char_list[(self.char_list.index(char) + self.s) % len(self.char_list)]

            l1 = ""
            for c in self.char_list:
                if c == char:
                    l1 += B + c + W
                else:
                    l1 += c

            l2 = ""
            for c in self.char_list:
                if c == new_char:
                    l2 += R + c + W
                else:
                    l2 += c

            space_count = int((len(self.char_list) - 4 - len(str(self.s))) / 2)

            print((" " * space_count) + str(self.s) + " -> ")
            print(l1)
            print(l2)
            print()
            print(decoded_hash + B + char + W)
            print("|" * (len(decoded_hash) + 1))
            input(encoded_hash + R + new_char + W)

            encoded_hash += new_char
            decoded_hash += char
            clear_terminal()

        return encoded_hash

    def decode(self, w):
        """
                Decodes the word (w) in the cesar chiffre style with the shift (s) and returns it. Also it has a fancy animation.

            :param w:
            :return:
        """
        self.s = -self.s
        h = self.encode(w)
        self.s = -self.s

        return h


clear_terminal()

shift = int(input("Shift: "))
word = input("Word: ")

cesar_chiffre = CesarChiffre(shift, animation=True)

print("Hash: " + O + cesar_chiffre.encode(word) + W)
