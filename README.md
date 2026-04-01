# smallifier

Just a dumb little command line script that does 1 of 3 things to whaever text is currently stored in your clipboard

if you dont use an argument, the script will just replace all text with the lowercase superscript version.
example: "python3 mockifier.py" will make "Hello World" --> "ʰᵉˡˡᵒ ʷᵒʳˡᵈ"


if you use "-r" it will replace your clipboard with text that is randomized between the regular version and the superscript version.
example: "python3 mockifier.py -r" will make "Hello World" --> "Helˡo ʷᵒʳˡᵈ"


if you use "-c" it will randomize between upper/lower case.
example: "python3 mockifier.py -c" will make "Hello World" --> "HELlo wORLD"

NOTE: "pip install pyperclip" before use