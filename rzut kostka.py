import random

print("Rzut Kostką")
a = int(input("Wpisz ile razy chcesz rzucic "))
for i in range(a):
    print(random.randint(1, 6))