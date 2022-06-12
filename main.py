import random

while True:
    user_action = input("Enter a choice ('R' = rock, 'P' = paper, 'S' = scissors): ")
    user_action = user_action.upper()
    possible_actions = ["R", "P", "S"]
    list_action = ['Rock', 'Paper', 'Scissors']
    if user_action in possible_actions:
        user_id = possible_actions.index(user_action)
        computer_action = random.choice(possible_actions)
        computerID = possible_actions.index(computer_action)
        print(f"\nPlayer ({list_action[user_id]}): CPU ({list_action[computerID]})\n")
              
        
    elif user_action not in possible_actions:
        print('You made an invlaid selection, make another choice and play again!!')
        continue
    
    
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        continue
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
            break
    
        else:
            print("Paper covers rock! You lose.")
            break
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
            break
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
            break
    else:
        print("You made an invalid selection, make another choice and play again!! ")
        continue

   