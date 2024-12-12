import string


plain_text = ("hello world")
shift = 7
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]


table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)
print(encrypted)

