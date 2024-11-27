import random

print("****************BINGO****************")


def sortear_bola():
    bola = random.randint(1, 90)  
    print(f"Número sorteado: {bola}")
    return bola

def criar_cartela():
    b1 = random.randint(1, 15)
    b2 = random.randint(1, 15)
    b3 = random.randint(1, 15)
    b4 = random.randint(1, 15)
    b5 = random.randint(1, 15)

    i1 = random.randint(16, 30)
    i2 = random.randint(16, 30)
    i3 = random.randint(16, 30)
    i4 = random.randint(16, 30)
    i5 = random.randint(16, 30)

    n1 = random.randint(31, 45)
    n2 = random.randint(31, 45)
    n3 = "*"  
    n4 = random.randint(31, 45)
    n5 = random.randint(31, 45)

    g1 = random.randint(46, 60)
    g2 = random.randint(46, 60)
    g3 = random.randint(46, 60)
    g4 = random.randint(46, 60)
    g5 = random.randint(46, 60)

    o1 = random.randint(61, 75)
    o2 = random.randint(61, 75)
    o3 = random.randint(61, 75)
    o4 = random.randint(61, 75)
    o5 = random.randint(61, 75)

  
    print("\nSua cartela:")
    print(f"{b1:2}  {i1:2}  {n1:2}  {g1:2}  {o1:2}")
    print(f"{b2:2}  {i2:2}  {n2:2}  {g2:2}  {o2:2}")
    print(f"{b3:2}  {i3:2}   {n3}   {g3:2}  {o3:2}")
    print(f"{b4:2}  {i4:2}  {n4:2}  {g4:2}  {o4:2}")
    print(f"{b5:2}  {i5:2}  {n5:2}  {g5:2}  {o5:2}")

    return [b1, b2, b3, b4, b5, i1, i2, i3, i4, i5, n1, n2, n4, n5, g1, g2, g3, g4, g5, o1, o2, o3, o4, o5]

cartela = criar_cartela()

bola = sortear_bola() 

if bola in cartela:
        print("Você acertou!")
else:
        print("você errou!")