import pyperclip


to_smallify = pyperclip.paste()
to_smallify = to_smallify.lower()


bigs   = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
smalls = ["ᵃ","ᵇ","ᶜ","ᵈ","ᵉ","ᶠ","ᵍ","ʰ","ᶦ","ʲ","ᵏ","ˡ","ᵐ","ⁿ","ᵒ","ᵖ","ᵠ","ʳ","ˢ","ᵗ","ᵘ","ᵛ","ʷ","ˣ","ʸ","ᶻ","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹","⁰"]
smallified = ""


for letter in range(0, len(to_smallify)):
    if to_smallify[letter].isalnum():
        if to_smallify[letter] in smalls:
            smallified += to_smallify[letter]
        else:
            smalls_index = bigs.index(to_smallify[letter])
            smallified += smalls[smalls_index]
    else:
        smallified += to_smallify[letter]
pyperclip.copy(smallified)
print(smallified)