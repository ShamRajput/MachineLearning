# Translate vowels to g
character = "g"
def translator(phrase):
    translated_phrase = ""
    print(phrase)
    for ch in phrase:
        if ch.lower() in "aeiou":
            if ch.isupper():
                translated_phrase+="G"
            else:
                translated_phrase+=character
        else:
            translated_phrase+=ch

    return translated_phrase


print(translator(input("Enter a phrase")))