import random


# if x in range(1, 8):
    # if x == 1:
    #     print("Понедельник")
    # elif x == 2:
    #     print("Вторник")
    # elif x == 3:
    #     print("Среда")
    # elif x == 4:
    #     print("Четверг")
    # elif x == 5:
    #     print("Пятница")
    # elif x == 6:
    #     print("Суббота")
    # elif x == 7:
    #     print("воскресенье")
# else:
#     print("Такого дня НЕ существует!!!!!!!!!!!!!!!!!!!!!!")

дни = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "воскресенье"   
}
for i in range(0,  1001):
    print("цикл №",i)
    x = random.randrange(0, 15)
    print("день №",x)
    if x in дни.keys():
        print(дни.get(x))
    else:
        print("Такого дня НЕ существует!!!!!!!!!!!!!!!!!!!!!!")
    print()
print("Конец")

