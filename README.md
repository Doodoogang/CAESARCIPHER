Rayat Rahman



This project was based on Caesar Cypher which could be a method of either encryption or decryption by moving around letters in a hidden message. I managed to make this style of encryption/decryption using Python. In the AlsoCaesar.py file, the code looks like this:
import string
plain_text = ("hello world")
shift = 7
shift %= 26
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet [:shift]
table = str.maketrans(aplhabet, shifted)
encrypted = plain_text.translate(table)
print(enccrypted)


The first action we took was to import the string module in python which would give us functions that would allow us to play around with strings and make different patterns. After that we added the variable "plain_text" which is going to contain the message we are either trying to encrypt or decrypt. The shift is the number of letters we move up by for each and every letter in the plain_text.Here we moved it up by 7.The shift %= 26 line uses mod function to get the remainder of the number of shifts from the number of the letters in the alphabet, which is 26. 

For this caesar project we only focused on lowercase letters, so we declared this by specifying that we only wanted string.ascii_lowercase characters for our alphabet.
the alphabet [shift:] + alphabet [:shift] represents the letters after and before the particular letter in the message still adding up to 26. This way even if you shifted a letter which went past z, the letter would just restart at a and continue to go where it is supposed to be. So if we shifted the letter h 7 times, the alphabet would start at o and be opqrstuvwxyzabcdefghijklmn.
The next line after this makes a translating table which switches out the original letter in the plain_text with the shifted counterpart letter. So for h in "hello world", the h would transform into an o, and all the other letters will be switched out with the letter 7 letters above.
Inside the encrypted variable is the plain_text message with every letter shifted the amount of times labeled in the shift= line using the translating table.
After that we simply print out the encrypted message and that is all it takes!
The plain_text = ("hello world") would come out as "olssv dvysk"

But lets say you wanted to decrypt a message. All you have to do then is make a few small changes. If you want to decrypt a message, all you would need to do is paste the encrypted message instead of the actual message in the plain_text line and instead of just the number of shifts you need, it would be 26 - (the number of shifts you need). This is an example of decryption:

import string
plain_text = ("olssv dvysk")
shift= 26-7
shift %= 26
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
encrypted = plain_text.translate(table)
print(encrypted)

And this will revert back to "hello world"

So using python, I managed to make a Caesar Cypher which could encrypt and decrypt code at the same time with only small changes. I recently learned about the modular algorithm and didn't know that this algorithm could be used to shift letters multiple times. This was a very fun project to do and I am actually looking forward to doing more projects like these with Python or potentially other languages like C++ and Java.
