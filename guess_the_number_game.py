import random
num = random.randint(1, 30)
print("Давай поиграем в угадай число!")

print("Но у тебя есть всего 5 попыток", "Вперёд!!!", sep='\n')

counter = 0

while True:
    print("Угадай число от 1 до 30")
    player = int(input())
    if player > 30:
        print("Вводите число от 1 до 30!")
    elif player < num:
        print("Загаданное число больше, попробуй ещё разок")
        counter += 1
    elif player > num:
        counter += 1
        print("Загаданное число меньше, давай ещё разок")
    if player == num:
        print("Молодец!")
        break
    if counter == 5:
        print("Игра окончена, закончились попытки")
        break

