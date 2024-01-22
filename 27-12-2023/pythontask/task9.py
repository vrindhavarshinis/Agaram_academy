character=input("Enter any character:")
if ((character>="a")and (character<="z") )or(( character>="A") and (character<="Z")):
    print(character, "is an Alphabet")
    
elif (character>="0"and character<="9"):
    print(character,"is a Digit")
else:
    print(character,"is a Special character")
    