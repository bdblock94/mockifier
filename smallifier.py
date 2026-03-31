import pyperclip


smallify = pyperclip.paste()
smallify = smallify.lower()


bigs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
smalls = ["ᵃ","ᵇ","ᶜ","ᵈ","ᵉ","ᶠ","ᵍ","ʰ","ᶦ","ʲ","ᵏ","ˡ","ᵐ","ⁿ","ᵒ","ᵖ","ᵠ","ʳ","ˢ","ᵗ","ᵘ","ᵛ","ʷ","ˣ","ʸ","ᶻ","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹","⁰"]
now_small = ""



for ltr in range(0, len(smallify)):
    if smallify[ltr].isalnum():
        if smallify[ltr] in smalls:
            now_small += smallify[ltr]
        else:
            smalls_index = bigs.index(smallify[ltr])
            now_small += smalls[smalls_index]
    else:
        now_small += smallify[ltr]
pyperclip.copy(now_small)
print(now_small)