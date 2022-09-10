import random

'''
This python file is a rock, paper, scissor simulation between two opponents showing how many times each opponent could possibly 
choose rock, paper, or scissors, and how many times each player won and lost
'''

rounds = int(input("How many rounds will be simulated? Please enter a number:"))


#Total counts of when player 1 and player 2 choose rock, paper and scissors will be recorded for future statistics

player1_rock_count = 0
player1_paper_count = 0
player1_scissor_count = 0
player1_win_count = 0
player1_loss_count = 0

player2_rock_count = 0
player2_paper_count = 0
player2_scissor_count = 0
player2_win_count = 0
player2_loss_count = 0

draw_count = 0


# Two players play rock, paper, scissor shoot and options 1, 2, 3 means rock, paper, and scissors respectively

for i in range(0, rounds):
    player1_choice = random.randint(1, 3)
    player2_choice = random.randint(1, 3)

    # Player 1 Choice
    if player1_choice == 1:
        player1_rock_count += 1
    elif player1_choice == 2:
        player1_paper_count += 1
    else:
        player1_scissor_count += 1

    # Player 2 Choice
    if player2_choice == 1:
        player2_rock_count += 1
    elif player2_choice == 2:
        player2_paper_count += 1
    else:
        player2_scissor_count += 1


    # Player 1 Option vs Player 2 Option
    if player1_choice == 1 and player2_choice == 1:
        draw_count +=1
    elif player1_choice == 1 and player2_choice == 2:
        player1_loss_count += 1
        player2_win_count += 1
    elif player1_choice == 1 and player2_choice == 3:
        player1_win_count += 1
        player2_loss_count += 1
    elif player1_choice == 2 and player2_choice == 1:
        player1_win_count += 1
        player2_loss_count += 1
    elif player1_choice == 2 and player2_choice == 2:
        draw_count += 1
    elif player1_choice == 2 and player2_choice == 3:
        player1_loss_count +=1 
        player2_win_count +=1
    elif player1_choice == 3 and player2_choice == 1:
        player1_loss_count +=1
        player2_win_count +=1
    elif player1_choice == 3 and player2_choice == 2:
        player1_win_count += 1
        player2_loss_count += 1
    else:
        draw_count += 1

# Staistics

# Player 1 Stats
print("Amount of times Player 1 chose rock: " + str(player1_rock_count) + " times or chose rock " + str(player1_rock_count) + "%" + " of the time")
print("Amount of times Player 1 chose paper: " + str(player1_paper_count) + " times or chose paper " + str(player1_paper_count) + "%" + " of the time")
print("Amount of times Player 1 chose scissors: " + str(player1_scissor_count) + " times or chose scissors " + str(player1_scissor_count) + "%" + " of the time")
print("Amount of rounds Player 1 won: " + str(player1_win_count) + " times or won " + str(player1_win_count) + "%" + " of the time") 
print("Amount of rounds Player 1 lost: " + str(player1_loss_count) + " times or lost " + str(player1_loss_count) + "%" + " of the time")
print("\n")

# Player 2 Stats
print("Amount of times Player 2 chose rock: " + str(player2_rock_count) + " times or chose rock " + str(player2_rock_count) + "%" + " of the time")
print("Amount of times Player 2 chose paper: " + str(player2_paper_count) + " times or chose paper " + str(player2_paper_count) + "%" + " of the time")
print("Amount of times Player 2 chose scissors: " + str(player2_scissor_count) + " times or chose scissors " + str(player2_scissor_count) + "%" + " of the time")
print("Amount of rounds Player 2 won: " + str(player2_win_count) + " times or won " + str(player2_win_count) + "%" + " of the time")
print("Amount of rounds Player 2 lost: " + str(player2_loss_count) + " times or lost " + str(player2_loss_count) + "%" + " of the time")
print("\n")

# Draws
print("Amount of draws: " + str(draw_count) + " times")
print("\n")

# Final Result
if player1_win_count > player2_win_count:
    print("The final result is Player 1 wins!")
elif player1_win_count < player2_win_count:
    print("The final result is Player 2 wins!")
else:
    print("The final result is a draw!")