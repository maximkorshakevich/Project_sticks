from utils import check_winner
from app_logic import human_turn, computer_turn
import time

print("Приветствуем вас в игре Sticks")
print("В данной игре вам предстоит сыграть в 21 спичку")
print("Правила игры: ")
print("1)По очередно ходят игрок и компьютер (вы можете выбрать кто сделает первый ход")
print("2)Каждой ход игрок должен брать от 1 до 3 спичек")
print("3)Проигравшим считается тот кто вытянет последнюю спичку")
print("---------------------------------------------------------")

def start_game():
    sticks=21
    turn=input("Хотите ходить первым? (да/нет): ").strip().lower()
    
    if turn=="да":
        human_first=True
    else:
        human_first=False
        
    play_game(human_first,sticks)

def play_game(human_first,sticks):
    current_player=human_first
    while sticks>0:
        if current_player:
            taken=human_turn(sticks)
        else:
            taken=computer_turn(sticks)
        sticks-=taken
        current_player=not current_player
        if check_winner(sticks):
            winner="Вы победили!" if current_player else "Победил компьютер!"
            print(winner)
            break
if __name__ == "__main__":
    import random
    while True:
        start_game()
        replay = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if replay != "да":
            print("Спасибо за игру!")
            break

time.sleep(3)
