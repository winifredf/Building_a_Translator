def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "D"
            else:
                translation = translation + "d"
        else:
            translation = translation + letter
    return translation
    
print(translate(input("Enter a phrase: ")))