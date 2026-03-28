#11-dars Konspekt
#X_O o'yini
g=[1,2,3,4,5,6,7,8,9]
print(f"""
             {g[0]} | {g[1]} | {g[2]} 
            -----------
             {g[3]} | {g[4]} | {g[5]}
            -----------
             {g[6]} | {g[7]} | {g[8]} 
"""
      )
while True:
    x = int(input('x='))
    g[x - 1] = 'X'
    print(f"""
                 {g[0]} | {g[1]} | {g[2]} 
                -----------
                 {g[3]} | {g[4]} | {g[5]}
                -----------
                 {g[6]} | {g[7]} | {g[8]} 
    """
          )
    if g[0]==g[1] and g[1]==g[2] or g[3]==g[4] and g[4]==g[5] or g[6]==g[7] and g[7]==g[8] or g[0]==g[3] and g[3]==g[6] or g[1]==g[4] and g[4]==g[7] or g[2]==g[5] and g[5]==g[8] or g[0]==g[4] and g[4]==g[8] or g[2]==g[4] and g[4]==g[6]:
        print('X yutdi! tamom')
        break
    o = int(input('o='))
    g[o - 1] = 'O'
    print(f"""
                 {g[0]} | {g[1]} | {g[2]} 
                -----------
                 {g[3]} | {g[4]} | {g[5]}
                -----------
                 {g[6]} | {g[7]} | {g[8]} 
    """
          )
    if g[0]==g[1] and g[1]==g[2] or g[3]==g[4] and g[4]==g[5] or g[6]==g[7] and g[7]==g[8] or g[0]==g[3] and g[3]==g[6] or g[1]==g[4] and g[4]==g[7] or g[2]==g[5] and g[5]==g[8] or g[0]==g[4] and g[4]==g[8] or g[2]==g[4] and g[4]==g[6]:
        print('0 yutdi! tamom')
        break
#hangman o'yini
from ast import While
import pprint
import random
word_list = ["olma", "banan", "nok", "behi", "gilos", "uzum", "malina"]
word = random.choice(word_list)
guesses = set()
while True:
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("Tbriklaymiz, siz yutdingiz!")
        break
    guess = input("Harf o'ylang: ")
    guesses.add(guess)
    if guess not in word:
        print("Xato")
    else:
        print("To'g'ri")
    if len(guesses) == 10:
        print("Uzr, siz barcha urinishlardan foydalanib bo'ldingiz!", word)
        break
#11-dars Uyga vazifa
#1. Tasodifiy Sonni Topish O'yini:
import random
x = random.randint(1, 11)
while True:
    y = int(input('Guess the number: '))
    if x == y:
        print('Tabriklayman topdingiz')
        break
    else:
        print('Noto\'g\'ri, qayta urinibko\'ring')
#2. Do'stlar ro'yhatini yaratish:
dostlar =[]
while True:
    dost = input('Dostlaringizni kiriting yoki stop deb yozing: ')
    if dost.lower() == 'stop':
        break
    dostlar.append(dost)
print(f"Sizning dostlaringiz ro'yhati: {dostlar}")
#3.Valyuta kalkulyatori:
doll1 = 11300
while True:
    dollar = float(input('Dollor miqdorini kiriting: '))
    som = dollar * doll1
    print(f"{dollar} dollor {som} somga teng.")
    if input('Yana bir marta hisoblashni xohlaysizmi? (ha/exit): ').lower() == 'ha':
        continue
    else:
        break
#4.Yarim archa:
n = int(input('Yarim archani balandligini kiriting: '))
i = 1  

while i <= n:
    print(str(i) * i)
    i += 1