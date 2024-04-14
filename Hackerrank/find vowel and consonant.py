re = input()
ch = "aeiouAEIOU"
if re in ch:
    print("This is Vowel")
elif "a" <= re <= "z" or "A" <= re <= "Z":
    print("This is Consonant")
else:
    print("This is Not a Alphabet")
