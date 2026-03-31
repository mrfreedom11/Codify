# Immutable = int, float, str, touple, bool
# Mutable = list, dict, set 

#Global Scope - o’zgaruvchi funksiyadan tashqarida yaratilganda-
#u o’sha fayldagi barcha funksiyalar uchun acessable bo’ladi.

a = 4  #global

def f1():
	print(a)

def f2():
	global a #global o'zgaruvchini chaqirish uchun
	a+=1

#Local Scope - o’zgaruvchi funksiya ichida e’lon qilinganda,- 
# u faqat o’sha funksiya uchun acessable bo’ladi.
def f1():
	a = 4  #local
	print(a)

#Nonlocal Scope - funksiya ichida yaratilgan o’zgaruvchi,
#  funksiya ichidagi boshqa funksiyalar(inner functions) 
# uchun ham acessable bo’ladi.

def f1():
	a = 4  
	def f2(): #inner function
		print(a) #nonlocal

#Global o’zgaruvchi funksiya ichida qayta yaratilsa u o’sha funksiya uchun local bo’ladi. 
a = 4
def f1():
	global a
	a = 5 #bu yerda mavjud global ozgaruvchini boshqa qiymatga o'zgartirsak funksiya ichida u o'zgaradi
	print(a) # local -> 5

print(a) #global -> 4

#Ichki funksiya nonlocal o'zgaruvchiga murojaat qila oladi, lekin o'zgartira olmaydi.
#Agar o’zgartirmoqchi bo'lsa, **nonlocal** so'zidan foydalanadi.
def f1():
	a = 4  
	def f2(): #inner function 
		nonlocal a
		a += 2
	print(a)  # -> 6

f1() 
f2() # -> ishlamaydi!
# Biz f2() ni f1() dan tashqarida chaqirsak u ishlamaydi.
#  Agar ishlagan taqdirda ham u nonlocal bo’lgan a ni topa olmasdan xatolik berardi. 

# Shu holatda bizga **Closures** yordamga keladi.
#  Closures ichki funksiyani tashqaridan chaqirish imkonini va nonlocal o’zgaruvchilariga murojaat qilish imkonini beradi.

#Pythonda funksiyani biz o’zgaruvchiga tenglay olamiz,
#  boshqa funksiyaga argument sifatida bera olamiz va funksiya ichida return qilib qaytara olamiz.

def f1():
	a = 4  
	return a 
x= f1() #1
f2(f1()) #2 

# 1-yolda funksiyani o'zgaruvchiga tenglab olayabmiz
# 2-yolda funksiyani boshqa bir funksiya ichiga olib qoyayabmiz


def f(x):  # 3-yol
    def g(y): # <-here
        return y # <-here
    return g # <-here
a = 5
b = 1

h=f(a) # bu yerda h ni return g ga tenglayabmiz
natija = h(b) # return g ni g(y) ga tenglayabmiz
print(natija )  # Output is 1

# yoki 
natija = f(a)(b) # bunday yozganimizda f(a) deganimizda a orniga g ni beradi va uni yoniga b ni qiymatini ham beradi
print(natija )  # Output is 1

# Agar return g(y) desak bu ishlamaydi

def f(x):
    def g(y):
        return y
    return g("""y""") # bu yerda returnga g ni qiymatini bersak y ni topa olmaydi shuning uvhun foim funksiyani ozini berish kerak
a = 5
b = 1
h=f(a)  # Xatolik beradi: NameError: name 'y' is not defined

def f(x):
    def g(y):
        def h(z):
            return z
        return h
    return g
a = 5
b = 2
c = 1
f(a)(b)(c)  # Output is 1
# yuqoridagi holatda avval (a) deb f(x) funksiyani keyin b deb g(y) ni keyin esa (c) deb  h(z) ni chiqarayabdi

#Agar biz nonlocal o’zgaruvchidan foydalansakchi:
def f(x):
    z = 2
    def g(y):
        return z*x + y
    return g
a = 5
b = 1
h = f(a)
print(h(b))  # Output is 11

#Biz h=f(a) ni ishlatganimizda f() funksiyadan chiqib ketamiz va g() ga kiramiz. ammo hali ham f ning o’zgaruvchilari **accessable!** Qanday qilib g() hali ham f() ning o’zgaruvchilarini ishlata olyabdi?! 
#Chunki endi ichki funkisa g() -CLOSURE
#CLOSURE - tashqi funksiyaning nonlocal o’zgaruvchilarini ishlata olish imkoniyatiga ega ichki funksyadir.
#“closure” atamasi “close” so’zidan olingan bo’lib,
#  u free (nonlocal) variable larni ushlab qolgan holda open term ni yopish natijasida vujudga kelgani uchun shunday nomlangan
def f(x):
    z = 2
    def g(y): # g hali closure emas
        return z*x + y
    return g
a = 5
b = 1
h = f(a) # endi h closure bo'ldi, qaysiki g ga teng bo'lgan.
print(h(b))  # Output is 11

# Bu closure emas: 
def f(x):
    z = 2
    def g(y):
        return y # Chunki ichki funksiya ota funksiyadan hech narsa ishlatmagan
    return g
a = 5
b = 1
h = f(a)
print(h(b))  # Output is 1
print(h.__code__.co_freevars) # Output is ()

# Bu esa closure

def f(x): #Grandparent
    def g(y): #Parent    #closure chunki g(y) f(x) dan h(z) ga tashib berayandi
        def h(z): #child    #closure  
            return x * y * z
        return h
    return g
a = 5
b = 2
c = 1
f(a)(b)(c)  # Output is 10

#Bu holatda g() ham, h() ham closure.
#  Nega g() closure? U free variable ishlatmaganku.
#  Ammo uning ichidagi h() ishlatmoqda, va x h() ga g() orqali o’tadi.
#  O’tkazib berish vaqtida g() x ni ishlatgan hisoblanadi. 
###################################################################################

# Closure sifatida biz lambda funksiya ham ishlata olamiz:
def f(x):
    z = 2
    return lambda y: z*x+y
a = 5
b = 1
f(a)(b)  # Output is 11
# Vazifa
# Composer - 2ta funksiyani qo’shib beruvchi funksiya.**
# Composer yaratamiz:**

def compose(g, f):
    def h(*args, **kwargs): #closure funksiya
        return g(f(*args, **kwargs))
    return h

# Vazifani bajaramiz:
km_to_m= lambda x: x*1000
m_to_sm= lambda x: x * 100

km_to_sm = compose(m_to_sm, km_to_m)
print(km_to_sm(12))   # Output 1 200 000
