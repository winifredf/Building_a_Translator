def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            traslation = translation + "d"
        else:
            translation = translation + letter
        return translation
    
print(translate(input("Enter a phrase:")))