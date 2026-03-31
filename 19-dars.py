tranzaksiyalar = [
    ("Toshkent", 100), 
    ("Samarqand", 500), 
    ("Toshkent", 200), 
    ("Buxoro", 300), 
    ("Toshkent", 50)
]
def toshkent_topar():
    toshkent_summalari = (summa for shahar, summa in tranzaksiyalar if shahar == 'Toshkent')
    kvadratlar = (s ** 2 for s in toshkent_summalari)
    yield from kvadratlar
gen = toshkent_topar()
print(next(gen))
print(next(gen))

def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a,b = b, a+b
fibo = fibonacci_generator()
for i in range(10):
    print(next(fibo))