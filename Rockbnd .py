# Rock Band Name Generator build by sumit Thakur

print("Hi, I am your Bot and I'll help you in generating your Rockband name \n press Enter answer me some question and I'll generate that for you")
name = input("Please Enter your Name - ")
song = input("Great Name ,so what's your favorite song " +name + " ? " )
animal = input("yeah that's an amazing song ,so what's your favorite animal " + name + " ? " )
print("Thanks for these inputs " + name + "press any key to generate your band name")
print("your Band Name is generated ,press any key to view ")
print(name + song[0:5] + animal[0:5] )
