import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

try:
    choose_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors ==> "))
    if choose_user < 0 or choose_user > 2:
        print("Invalid choice! Please choose 0, 1, or 2.")
    else:
        print(f"You chose:\n{choices[choose_user]}")

        # Escolha do computador
        choose_computer = random.randint(0, 2)
        print(f"Computer chose:\n{choices[choose_computer]}")

        # Determinar o vencedor
        if choose_user == choose_computer:
            print("It's a tie!")
        elif (choose_user == 0 and choose_computer == 2) or \
             (choose_user == 1 and choose_computer == 0) or \
             (choose_user == 2 and choose_computer == 1):
            print("You win!")
        else:
            print("You lose!")
except ValueError:
    print("Invalid input! Please enter a number (0, 1, or 2).")
