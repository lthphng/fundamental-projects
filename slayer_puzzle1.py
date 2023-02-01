print("Solve: SLAYER + SLAYER + SLAYER = LAYERS")

a = int(input("What is your guess? "))
b = a//100000 + (a-a//100000*100000)*10

if b == a*3:
    print(b, "==", a*3, "-> True")
else:
    print(b, "==", a*3, "-> False")
