import random
secilenler = random.randint(0,49)
sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    kac = int(input("sifre kac haneli olsun?:"))
    secilenler = random.randint(0,49)
    for i in range(kac):
        secilenler = random.randint(0,49)
        print(sifre[secilenler])

		