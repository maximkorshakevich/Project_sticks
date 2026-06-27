from utils import check_winner
from app_logic import human_turn, computer_turn

def start_game():
    sticks=21
    turn=input("Хотите ходить первым? (да/нет): ").strip().lower()
    
    if turn=="да":
        human_first=True
    else:
        human_first=False
        
    play_game(human_first,sticks)

def plat_game(human_first,sticks):
    current_player=human_first
    while sticks>0:
        if current_player:
            taken=human_turn(sticks)
        else:
            taken=computer_turn(sticks)
        sticks-=taken
        current_player=not current_player
        if check_winner(sticks):
            winner="Вы победили!" if current_playerelse else "Победил компьютер!"
            print(winner)
            break
if __name__=="__main__":
    import random
    start_game()
