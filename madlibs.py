#declare variables for the inputs
city = input("City: ")
name = input("Name: ")
noun = input("Noun: ")
adjective = input("Adjective: ")
verb1 = input("Verb in past tense: ")
verb2 = input("Verb in past tense:")
furniture = input("Furniture: ")
algorithm = input("Algorithm: ")
programming_language = input("Programming language: ")

#create the madlib sentence
madlib = f"In the heart of {city} City, {name}, a brilliant programmer, sat hunched over his keyboard.\
    His fingers danced like binary fireflies, weaving spells in {programming_language}.\
    Late one night, he whispered an incantation: sudo make magic happen.\
    Suddenly, screens {verb1}, and pixels {verb2}.\
    The coffee machine brewed {algorithm} algorithms, and the office {furniture} swirled in delight.\
    Eli grinned—the code had come alive! But beware: every bug fixed was a star lost in the digital sky.\
    And so, dear coders, remember: behind every line of code lies a touch of {noun} !"

print(madlib)

