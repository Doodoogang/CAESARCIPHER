import string

def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

plain_text = input("Enter plain text: ")
shift = int(input("Enter shift: "))
print(caesar(plain_text, 7, [string.ascii_uppercase, string.ascii_lowercase, string.punctuation]))
