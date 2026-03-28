# # LIST COMPEHENSION

# # l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# # toqlar = []
# # for i in l:
# #     if i % 2 == 1:
# #         toqlar.append(i*2)
# #
# #
# # toqlar = [i*2 for i in l if i%2==1]


# # 1-misol
# # regions = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"],
# #            ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]
# #
# # from_city = [l[1] for l in regions]
# # print(from_city)


# # # 2-misol
# # sonlar = [1, 2, 3, 4, 5]
# # # Ushbu listdagi toq sonlarni 2ga ko'paytirib yangi listga o'tkazing.


# # # # 3-misol
# # lst = ['Alice', 1, 2, 3, 'Alice', 'Alice']
# # # # listdagi ma'lum elementning ilk uchragan indexini topish
# # indice = lst.index('Alice')
# # # print(indice)
# #
# # # # listdagi ma'lum elementning barcha indexlarini topish
# # indicies = [i for i in range(len(lst)) if lst[i] == 'Alice']
# # print(indicies)


# # 4-misol
# # (ism, $-pul) Miilionerni toping.
# # people = [("John", 240_000), ("Alice", 120_000), ("Ann", 1_100_000), ("Zach", 44_000), ("Doe", 2_300_000)]
# # millioners = [name for name,money in people if money >= 1_000_000]
# # print(millioners)
# #
# # def find_millioneer(people):
# #     return [name for name, money in people.items() if money >= 1_000_000]
# #
# # # find millionaeer funksiya yozib, uni quyidagi qiymatlar bilan testlang
# # people_data1 = {'Alice': 1_000_000, 'Bob': 998_170, 'Carol': 1_229_080, 'Frank': 881_230, 'Eve': 93_121}
# # people_data2 = {'Alice': 1_000_000, 'Bob': 998_170, 'Frank': 1_881_230, 'Eve': 93_121}
# #
# # def test():
# #     assert find_millioneer(people_data1) == ['Alice', 'Carol']
# #     assert find_millioneer(people_data2) == ['Alice', 'Frank']
# #
# # test()


# # 5-misol: Quyidagi listni ichma ich sikl orqali yarating:
# # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# # l = []
# # for x in range(3):
# #     for y in range(3):
# #         l.append((x, y))

# # print([(x,y) for x in range(3) for y in range(5)])

# # Bundan boshqa optimal yo'lini ko'rsating

# # 6-misol
# # Matndani uzulnigi 5 ta harfdan ortiq bo'lgan so'zlarni toping
# text = '''Call me Ishmael. Some years ago - never mind how long precisely - having little
# or no money in my purse, and nothing particular to interest me on shore, I thought I would
# sail about a little and see the watery part of the world. It is a way I have of driving off
# the spleen, and regulating the circulation. - Moby Dick '''
# # print([[i for i in line.split() if len(i)>7] for line in text.split("\n")])

# # ziplash
# lst_1 = ['ism', 'familiya', 'yosh']
# lst_2 = ['Akmal', 'Tohirov', 16]

# for i,j in zip(lst_1, lst_2):
#     print(i, j)


# # #
# # # # unziplash
# # lst_1_new, lst_2_new = zip(*zipped)
# # print(list(lst_1_new))
# # print(list(lst_2_new))


# # # # 7-misol
# # ustun_nomlari = ['name', 'salary', 'job']
# #
# #
# # qatorlar = [('Alice', 180_000, 'data scientist'),
# #             ('Bob', 99_000, 'project manager'),
# #             ('Frank', 87_000, 'backend developer')]
# # db = [dict(zip(ustun_nomlari, row)) for row in qatorlar]
# # print(db)


# # #lambda()
# f = lambda a: a * 2
# # ==
# def f(a):
#     return a * 2


# # # 8-misol: 3 ta son yig'indisini toping
# #
# # # 1-usul
# # summa = lambda a, b, c: a + b + c
# # print(summa(1,2,3))
# #
# # # 2-usul
# # print((lambda a, c, b: a + b+c)(1,2,4))
# #
# # def summa(a,b,c):
# #     return a+b+c
# # print(summa(1,2,3))

# # print((lambda x: x + 3)(9))

# # map()
# # 9-misol: sonlarni integerga o'tkazing
# # str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
# # int_nums = map(int, str_nums)
# # print(list(int_nums))

# # 10-misol: sonlarni kvadratga ko'taring
# numbers = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x ** 2, numbers)))

# # # 11-misol: listdagi elementlarni mos indexi bo'yicha ayiring.
# # print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))

# # # 12-misol: Listdagi elementlarni katta harfga o'tkazing
# # string_it = ["processing", "strings", "with", "map"]
# # print(list(map(str.upper, string_it)))


# # # Reduce()
# # 13-misol: faktorialni toping: !4 = 1*2*3*4
# from functools import reduce

# n = 3
# print(reduce(lambda x, y: x * y, range(1, n + 1)))
# # https://www.geeksforgeeks.org/reduce-in-python/

# # filter
