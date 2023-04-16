def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "AEIOUaeiou":
            translation = translation + "d"
        else:
            translation = translation + letter
    return translation
    
print(translate(input("Enter a phrase: ")))