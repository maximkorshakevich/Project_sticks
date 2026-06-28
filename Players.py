def players():
    if sticks == 0:
        return True
    return False


sticks = 21  
current_player = 1  

while sticks > 0:
    print(f"Палочек осталось: {sticks}")
    
    
    try:
        take = int(input(f"Игрок {current_player}, сколько палочек взять (1-3)? "))
    except ValueError:
        print("Пожалуйста, введите число.")
        continue
        
    if take < 1 or take > 3 or take > sticks:
        print("Некорректный ход. Попробуйте еще раз.")
        continue
        
    sticks -= take
    
    
    if players():
        print(f"Игрок {current_player} проиграл!")
        break
        
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
