#12-Dars Konspekt
#Funksiyalar
def qoldiqsiz_3_5():
    for i in range(1,41):
        if i % 3 == 0 and i % 5 ==0:
            print(i)
qoldiqsiz_3_5()
def add(a,b):#(a,b)parametr
    return a + b
yigindi = add(5,7)#(5,7)argument
print(yigindi) #12
# Uyga vzifa
#1.User funksiyasi:
def user_data(first_name,last_name,age):
    print(f"Ism: {first_name}\nFamiliya: {last_name}\nYosh: {age}")
user_data('Alisher','Olimov',27)
#2.Find_max:
def find_max(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(find_max(5,7,3))
#3.Find_letter_count:
def find_letter_count(word,letter):
    count = 0
    for letter in word:
        if letter == letter:
            count += 1
    return count
print(find_letter_count('Programing','r'))
#4.List_sum:
def list_sum(myList):
    yigindi = sum(myList)
    print(f"Listning elementlar yig'indisi = {yigindi}")
sonlar = [10, 5, 7, 10]
list_sum(sonlar)
#5.Daraja:
def daraja(a,b):
    return a ** b
print(daraja(2,3))
#6.Daraja4:
def daraja4(a,b,c,d):
    return a **b, c ** d
print(daraja4(2,3,4,5))
#7.digit_count_and_sum(word):
def digit_count_and_sum(word):
    for raqam in word:
        if raqam.isdigit():
            count = 0
            count += 1
            sum = 0
            sum += int(raqam)
    return count, sum
print(digit_count_and_sum('P4r0gr4m1ng'))
#8.add_right():
def add_right(a,b):
    a,b = str(a),str(b)
    return a + b
print(add_right(123,456))
#9.add_left():
def add_left(a,b):
    a,b = str(a),str(b)
    return b + a
print(add_left(123,456))
#10.work_with_list(a):
def work_with_list(a):
    min_num = min(a)
    for i in range(len(a)):
        a[i] *= min_num
    return a
print(work_with_list([1,2,3,4,5]))
#11.big_sales:
sales = {
  "yanvar": 12000,
  "mart": 6000,
  "aprel": 15000,
  "sentabr": 9000,
  "dekabr": 10000,
}
def big_sales(sales):
    max_sales = max(sales.values())
    for month, sale in sales.items():
        if sale == max_sales:
            return month, sale
print(big_sales(sales))
#12.min_max:
def min_max(numbers, max_num, min_num):
    is_max = max(numbers) == max_num
    is_min = min(numbers) == min_num
    return is_max, is_min
nums = [10, 2, 45, 67, 1]
print(min_max(nums, 67, 1))