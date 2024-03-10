#this is a code that generates madlibs
#have fun learning
#declare variables for the inputs
city = (input("City: ")).upper()
name = input("Name: ").upper()
noun = input("Noun: ").upper()
adjective = input("Adjective: ").upper()
verb1 = input("Verb in past tense: ").upper()
verb2 = input("Verb in past tense:").upper()
furniture = input("Furniture: ").upper()
algorithm = input("Algorithm: ").upper()
programming_language = input("Programming language: ").upper()

#create the madlib sentence
madlib = f"In the heart of {city} City, {name}, a brilliant programmer, sat hunched over his keyboard.\
    His fingers danced like binary fireflies, weaving spells in {programming_language}.\
    Late one night, he whispered an incantation: sudo make magic happen.\
    Suddenly, screens {verb1}, and pixels {verb2}.\
    The coffee machine brewed {algorithm} algorithms, and the office {furniture} swirled in delight.\
    Eli grinned—the code had come alive! But beware: every bug fixed was a star lost in the digital sky.\
    And so, dear coders, remember: behind every line of code lies a touch of {noun} !"

#display final result
print(madlib)