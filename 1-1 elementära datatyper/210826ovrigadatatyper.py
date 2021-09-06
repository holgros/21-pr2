# strängar och tipplar (tuples)
s = "Hejsan på dejsan!"
print(len(s))               # 17
print(s[0])                 # "H"
print(s[10])                # "d"
print(s.index("dejsan"))    # 10
print(s.upper())            # "HEJSAN PÅ DEJSAN"
tuple = s.partition("på")
print(tuple)                # ('Hejsan' ,'på', 'dejsan!')
print(tuple[2])             # "dejsan"
#tuple[2] = "mejsan!"        # fel - kan inte ändra en tuppel!

# en dictionary (associativt fält) förknippar varje nyckel med ett värde
dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
print(dic["Sverige"])               # "Stockholm"
print(dic["Norge"])                 # "Oslo"
print(dic["Finland"])               # "Helsingfors"
#print(dic["Danmark"])               # KeyError

# nycklar till dictionaries behöver inte vara strängar
dic = {1: "Foo", "Bar": "Baz", True: False}
print(dic[1])                       # "Foo"
print(dic["Bar"])                   # "Baz"
print(dic[True])                    # False

# i logiska (booleska) sammanhang utvärderas siffran 0 och tom sträng som falska, övriga siffror och strängar som sanna
bool = True or 0
print(bool)         # True
bool = True and 1
print(bool)         # 1
bool = not False or ""
print(bool)         # True
bool = False and ""
print(bool)         # False
bool = True and ""
print(bool)         # tom sträng

# mängd (set) är en datakollektion som är oordnad och där varje element är unikt
s = set()
s.add("Äpple")
s.add("Banan")
s.add("Päron")
s.add("Äpple")      # Vi har redan ett äpple, element måste vara unika, så vi kan inte lägga till ett till äpple
print(s)            # {"Banan", "Päron", "Äpple"}
