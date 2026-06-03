import time

x = "banana"
z = 1
Omgange = 1
Fruit = ""
FruitIsBanana = False
programRunning = True

while programRunning == True:
    for y in x:
        time.sleep(1.0)
        print(x[0:z])
        z = z+1
        if z == 7:
            FruitIsBanana = True
            z = 1
            Omgange = Omgange+1
            time.sleep(1.0)

    if FruitIsBanana == True:
        print("YES BABY THATS WHAT I LIKE TO SEE, THATS THE", str(Omgange),"TH TIME I SPELLED BANANA")
        time.sleep(1.0)
        FruitIsBanana = False
        print("updatetest")
    else:
        print("Wrong fruit, very sad!")

    def fruit_help(self):
        """
        Du skal skrive en frugt, der er kun en række frugter der er korrekt
        """

