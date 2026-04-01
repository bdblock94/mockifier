import pyperclip
import sys
import random


text = pyperclip.paste()
output = ""


bigs   = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
smalls = ["ᵃ","ᵇ","ᶜ","ᵈ","ᵉ","ᶠ","ᵍ","ʰ","ᶦ","ʲ","ᵏ","ˡ","ᵐ","ⁿ","ᵒ","ᵖ","ᵠ","ʳ","ˢ","ᵗ","ᵘ","ᵛ","ʷ","ˣ","ʸ","ᶻ","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹","⁰"]


def make_small(ltr):
    ltr = ltr.lower()
    if ltr.isalnum() and ltr not in smalls:
        return smalls[bigs.index(ltr)]
    else:
        return ltr



def random_case(ltr):
    if random.randint(1,2) == 2:
        return ltr.upper()
    else:
        return ltr.lower()



def random_size(ltr):
    if random.randint(1,2) == 2:
        return make_small(ltr)
    else:
        return ltr



def output_one():
    output = ""
    for ltr in text:
        output += make_small(ltr)
    pyperclip.copy(output)
    print(output)



def output_two():
    output = ""
    for ltr in text:
        if sys.argv[1] == "-r":
            output += random_size(ltr)
        elif sys.argv[1] == "-c":
            output += random_case(ltr)
        else:
            sys.exit("Warning: Invalid argument, did you mean to use -r or -c?")
    pyperclip.copy(output)
    print(output)
        


def main():
    if len(sys.argv) >= 2:
        output_two()
    else:
        output_one()



main()