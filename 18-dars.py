# 18-dars
# Rekursiv funksiya
# Faktorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

# Fibonnachi 
def fibonacci(n): 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))
# Fibonacci sonlari kattaroq bolsa kompyuterda juda kop vaqt oladi
# Buni optoimozatsiya qilish uchun kesh qoshish kerak
def fibonacci(n, cache = {}): #cache = {2:1, 4:3} ya'ni 2-fibo son bu 1 4-fibo son bu 3 deb aytib ketayabmiz 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(9))
# Sorting
arr = [1,26,7,8,0,3,6]
arr.sort() #Tim Sort

#Quick Sort
lst = [1,3,5,0,7,3,9]
def quick_sort():
    if len(lst) <= 1:
        return lst
    else:
        privot = lst[0]
        left = [x for x in lst[1:] if x <= privot]
        right = [x for x in lst[1:] if x > privot]
        return quick_sort(left) + [privot] + quick_sort(right)
# Uyga Vazifa
# Tower of Hanoi
def tower_hanoi(n,from_rod,to_rod, aux_rod):
    if n == 1:
        print('Move disk 1 from rod', from_rod , 'to', to_rod)
        return
    tower_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print('Move disk', n, 'from rod', from_rod, 'to', to_rod)
    tower_hanoi(n - 1, aux_rod, to_rod, from_rod)
tower_hanoi(3, 'A', 'C', 'B')
# tower_hanoi(1,A,C,B)