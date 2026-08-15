import random

def play_game():
    lucky_num = random.randint(1, 50)
     
while True:
    user_num = int (input("Enter your number: ")) 

    if user_num == lucky_num:
        print("You Won Game!") 
        break
    elif user_num < lucky_num:
        print("Too Low")   
    else:
        print("Too High")    
     
print("Thanks For Playing!")        
        
play_game();        