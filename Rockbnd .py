# Rock Band Name Generator build by sumit Thakur

print("Hi, I am your Bot and I'll help you in generating your Rockband name \n press Enter and answer me some question and I'll generate that for you")
name = None 
song = None
animal = None
name = input("Please Enter your Name:")
if name:
    song = input("Great Name ,so what's your favorite song " +name + " ? " )
else:
    print("Name can't be empty.")
if song:
    animal = input(f"yeah that's an amazing song ,so what's your favorite animal {name}?")
else:
    print("Song can't be empty.")
print("Thanks for these inputs " + name + "press Enter to generate your band name.")
input()
print("your Band Name is generated ,press Enter to view.")
input()
if len(song) >= 5 and len(animal) >= 5:
    print(name + song[0:5] + animal[0:5] )
else:
    print("Your entered song or animal name is too short to generate!")
