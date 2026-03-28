# 16-dars
# Setlar
# setlar - pythonni ichida mavjud bolgan build in data type
# Set dagi itemlar unchangable 
# lekin yangi element qoshish va olib tashlash mumkin
# setda hech narsa indexsi yoq har safar index ozgarib turadi
# setda 2 ta bir xil item bolishi mumkin emas va True va 1 ni bitta qiymat deb oladi
# elementlarga murojaat qilish uchun sikl aylantirish kerak
this_set = {'apple','banan'}
#element qoshish
this_set.add('cherry')
print(this_set)
# 2 setni qoshish
a_set = {'brick','home'}
b_set = {'flat','pool'}
a_set.update(b_set)#sest qoshish qismi
print(a_set)
"""setdan tashqari
   2 ta iterable qoshish mumkin
   eng muhimi qoshayotganimizda
   ulardan biri set bolishi kerak"""
# olib tashlash uchun .remove kerak
# agar discard bilan olib tashlansa hech narsa bolmasa ham xatolik bermaydi
# fog songgi elementni olib tashlaydi
# clear butunlay tozalaydi
# del butunlay set ham ochib ketadi
# 2 setni qoshish uchun .union() ishlatiladi 
# intersection_update faqat duplikatlarni qaytaradi
# intersection huddi intersection updatega oxshaydi lekin yangi ozgaruvchiga tenglab oladi
# Uyga vazifa
# 1-topshiriq: 
def str_counter(strs):
    natija = {}
    for soz in strs:
        uzunlik = len(soz)
        if uzunlik not in natija:
            natija[uzunlik] = []
        natija[uzunlik].append(soz)
    return natija
mevalar = ["shaftoli", "olma", "nok", "anor", "uzum"]
print(str_counter(mevalar))
# 2-topshiriq:
x = input("Kalitlarni kiriting : ").split()
y = input("Qiymatlarni kiriting: ").split()
merged = dict(zip(x, y))
print(merged)
# 3-tophiriq
a = input('Ismni kiriting: ').split()
b = input('Raqamni kiriting: ').split()
contacts = dict(zip(a, b))
print("\nSaqlangan kontaktlar:")
print(contacts)
# 4-topshiriq
def counter_dict(nums):
    natija = {}
    for son in nums:
        if son in natija:
            natija[son] += 1
        else:
            natija[son] = 1
    return natija
print(counter_dict([2, 1, 1, 1]))
# 5-topshiriq
def max_ball_students(talabalar):
    natija = {}
    for i in range(2):
        max_ball = -1
        max_ism = ""
        for ism in talabalar:
            if talabalar[ism] > max_ball:
                max_ball = talabalar[ism]
                max_ism = ism
        if max_ism != "":
            natija[max_ism] = max_ball
            del talabalar[max_ism]
    return natija
sinf = {"Akmal": 64, "Tohir": 55, "Nodir": 76, "Zafar": 80}
print(max_ball_students(sinf.copy()))