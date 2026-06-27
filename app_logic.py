def human_turn(sticks_left):
    while True:
        try:
            take=int(input(f"Ваш ход. Осталось ходова {stick_left} спичек. Сколько возьмете? (1-3)"))
            if 1<= take <= min(3, sticks_left):
                return take
            else:
                print("Ошибк! Можно взять от 1 до 3 спичек")
            except ValueError:
                print("Ошибка, введите целое число")
