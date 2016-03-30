import random


pruefung = 0

primzahl = []
 
for a in range (0, 100):
 
    for i in range (2, a):
 
        if a * 1.0 % i == 0:
            pruefung = 1
            break
 
    if pruefung == 1:
        pruefung = 0
    else:
        primzahl.append(a)
        
p = random.choice(primzahl)
q = random.choice(primzahl)

N = p*q
Nw = (p - 1)*(q -1)
e = random.choice(primzahl)

for d in range(10000000):
    if d * e % Nw == 1:
        break

print(e)
print(d)
print(N)
    
    










       



        
