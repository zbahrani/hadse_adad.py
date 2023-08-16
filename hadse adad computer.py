import random
a = 1
b = 99
hads = random.randint(a, b)
print(hads)
javab = input(" bozorgtarو kochektarو barabar: ")
while javab != "barabar":
    if javab == "bozorgtar" :
        b = hads 
        hads = random.randint(a, b)
        print(hads)
        javab = input(" bozorgtarو kochektarو barabar: ")
    else:
        a = hads
        hads = random.randint(a, b)
        print(hads)
        javab = input(" bozorgtarو kochektarو barabar: ")
print("yesss, I did it")




