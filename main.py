import random
from replit import clear
cards = [11 , 2, 3, 4, 5, 6, 7 ,8, 9 ,10 ,10, 10 ,10]
def blackjack():
  end = False
  while end == False:
    start = input("Do you want to play the game of BlackJyack/21? Type 'y' to play to 'n' to exit or restart the game.\n ")
    from art import logo
    print(logo)
    if start == 'y':
      user_card1 = random.choice(cards)
      user_card2 = random.choice(cards)
      score = user_card1 + user_card2
      print(f"Your card [{user_card1},{user_card2}] , score : {score}")
      computer_card1 =random.choice(cards) 
      computer_card2 = random.choice(cards)
      print(f"computer's first card: {computer_card1}")
      user_choice = input("Type 'y' to get another card , or type 'n' to pass.")
      if user_choice == 'y':
        user_card3 = random.choice(cards)
        if user_card3 == '11':
          ask = input("you card is ace what do you to want to count '1' or '11' type 'y' for 1 and 'n' for 11")
          if ask == 'y':
            user_card3 = 1
          else:
            user_card3 = 11
        total_score = score + user_card3
        print(f"You hand :[{user_card1},{user_card2},{user_card3}] , final score : {total_score}")
        computer_score = computer_card1 + computer_card2
        if computer_score < 17:
          computer_card3 = random.choice(cards)
          computer_score = computer_score + computer_card3
          print(f"computer's final score [{computer_card1},{computer_card2},{computer_card3}] , final score : {computer_score}")
        else:
            print(f"computer's final score [{computer_card1},{computer_card2}] , final score : {computer_score}")
      elif user_choice == 'n':
        total_score = user_card1 + user_card2
        print(f"You hand :[{user_card1},{user_card2}] , final score : {total_score}")
        computer_score = computer_card1 + computer_card2
        if computer_score < 17 :
          computer_card3 = random.choice(cards)
          computer_score = computer_score + computer_card3
          print(f"computer's final score [{computer_card1},{computer_card2},{computer_card3}] , final score : {computer_score}")
        else:
          computer_score = computer_card1 + computer_card2
          print(f"computer's final score [{computer_card1},{computer_card2}] , final score : {computer_score}")
      if total_score == computer_score:
        print("Draw")
      elif total_score > 21:
        print("Brust!. You Lose...")
      elif total_score > computer_score:
        print("You Won")
      elif computer_score > 21 :
        print("You won")
    elif start == 'n':
      end = True
      clear()
      blackjack()

blackjack()
    


      






    