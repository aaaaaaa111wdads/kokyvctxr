def проверка_часа(час):
     if час == 0:
        return "часов"
def сей_хелло(час):
    текст_часа=проверка_часа(час)
    if час in range(0,7):
        print(текст_часа,"Добрий ночи")
    elif час in range(7,11):
        print(текст_часа,"Добрий утра")
    elif час in range(11,18):
        print("Добрий день")
    elif час in range (18,22):
        print("Добрий вечир")
    elif час == 23:
        print("Добрий ночи")
# for i in range(22):
#     сей_хелло(i)
