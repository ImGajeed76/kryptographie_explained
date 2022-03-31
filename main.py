import hashlib
import string
import time

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple

result = ""
print(result)


def load(delay=1, repeats=2, length=5):
    for i in range(repeats):
        for j in range(length):
            clear_terminal()
            print("." * j)
            time.sleep(delay)


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


def print_2d(l):
    for row in l:
        print(f"{row}")


def wait():
    input("")


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


class Kryptography:
    chars_to_use = ""

    def __init__(self, chars_to_use=string.ascii_lowercase + string.ascii_uppercase + "0123456789" + "!?$"):
        self.chars_to_use = chars_to_use

    def create_2d_list(self, size):
        result = []

        for i in range(size):
            row = []
            for j in range(size):
                row.append((j + i) % size)

            result.append(row)

        return result

    def print_2d_chars(self):
        tabel = self.create_2d_list(len(self.chars_to_use))

        for row in tabel:
            r = "["
            for number in row:
                c = self.chars_to_use[number]
                r += f"{c}, "

            print(r + "]")

    def encode(self, text, key):
        if len(text) != len(key):
            return

        result = ""
        tabel = self.create_2d_list(len(self.chars_to_use))

        for i in range(len(text)):
            tc = text[i]
            kc = key[i]

            tp = self.chars_to_use.find(tc)
            kp = self.chars_to_use.find(kc)

            if tp == -1:
                print(f"{O}Warning: {tc} character is not in list{W}")

            if kp == -1:
                print(f"{O}Warning: {kc} character is not in list{W}")

            result += self.chars_to_use[tabel[tp][kp]]

        return result


class Hashing:
    def show_diff(self, t1: str, t2: str):
        hash1 = hashlib.sha256(t1.encode('utf-8')).hexdigest()
        hash2 = hashlib.sha256(t2.encode('utf-8')).hexdigest()

        out1 = ""
        out2 = ""

        for i in range(len(hash1)):
            if hash1[i] == hash2[i]:
                out1 += G
                out2 += G

            out1 += hash1[i] + W
            out2 += hash2[i] + W

        print(out1)
        print(out2)


def anim():
    clear_terminal()
    wait()

    # -------------- CesarChiffre --------------
    cc = CesarChiffre(5)
    cc.encode("Kryptographie")

    wait()
    clear_terminal()

    # -------------- Ver- / Endschlüsseln --------------
    krypto = Kryptography()
    print("Kryptographie & JiA$d63PA?cp4")

    wait()
    clear_terminal()

    result = krypto.encode("Kryptographie", "JiA$d63PA?cp4")
    print(f"Kryptographie & JiA$d63PA?cp4 = {G}{result}{W}")

    wait()
    clear_terminal()

    # -------------- tabel --------------
    krypto.print_2d_chars()

    wait()
    clear_terminal()

    # -------------- Hashing --------------
    hashing = Hashing()
    hashing.show_diff("Hallo", "Hello")

    wait()
    clear_terminal()


if __name__ == '__main__':
    anim()
