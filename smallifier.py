import pyperclip
import sys
import random


text = pyperclip.paste()
text = text.lower()



bigs   = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
smalls = ["ᵃ","ᵇ","ᶜ","ᵈ","ᵉ","ᶠ","ᵍ","ʰ","ᶦ","ʲ","ᵏ","ˡ","ᵐ","ⁿ","ᵒ","ᵖ","ᵠ","ʳ","ˢ","ᵗ","ᵘ","ᵛ","ʷ","ˣ","ʸ","ᶻ","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹","⁰"]




def random_case():
    print("Try again when -c is updated")



def random_size():
    smallified = ""
    for letter in range(0, len(text)):
        if random.randint(0, 10) % 2 == 0:
            if text[letter].isalnum():
                if text[letter] in smalls:
                    smallified += text[letter]
                else:
                    smalls_index = bigs.index(text[letter])
                    smallified += smalls[smalls_index]
            else:
                smallified += text[letter]
        else:
            smallified += text[letter]
    print(smallified)
    pyperclip.copy(smallified)



def smallify():
    smallified = ""
    for letter in range(0, len(text)):
        if text[letter].isalnum():
            if text[letter] in smalls:
                smallified += text[letter]
            else:
                smalls_index = bigs.index(text[letter])
                smallified += smalls[smalls_index]
        else:
            smallified += text[letter]
    pyperclip.copy(smallified)
    print(smallified)



def main():
    if len(sys.argv) != 2:
        smallify()
        sys.exit(0)
    elif sys.argv[1] == "-r":
        random_size()
        sys.exit(0)
    elif sys.argv[1] == "-c":
        random_case()
    



main()
