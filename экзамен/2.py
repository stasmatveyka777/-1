import random
a=int(input('количество= '))
b=[random.randint(0,15) for i in range(a)]
print(b[0],b[-1])
print(b)
s=1
for i in b:
 s*=i
print(f'Множина:',{s})
