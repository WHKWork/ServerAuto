x = input("Write a fruit ")
z = 1
FruitIsBanana = False

for y in x:
    print(x[0:z])
    z = z+1
    if x == "banana":
        FruitIsBanana = True

if FruitIsBanana == True:
    print("YES BABY THATS WHAT I LIKE TO SEE")
else:
    print("Wrong fruit, very sad!")

def fruit_help(self):
    """
    Du skal skrive en frugt, der er kun en række frugter der er korrekt
    """

