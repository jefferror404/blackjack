############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
import random
from replit2 import clear

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play == "y":
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  yourcards = []
  compcards = []
  
  firstcard = cards[random.randint(0,len(cards)-1)]
  yourcards.append(firstcard)
  secondcard = cards[random.randint(0,len(cards)-1)]
  yourcards.append(secondcard)
    
  compfirstcard = cards[random.randint(0,len(cards)-1)]
  compcards.append(compfirstcard)
  compsecondcard = cards[random.randint(0,len(cards)-1)]
  compcards.append(compsecondcard)
  
  sumscore = 0
  for i in yourcards:
    sumscore += i
    
  def replaceA():
    checkA = yourcards.count(11)
    if checkA >= 2:
      yourcards[yourcards.index(11)] = 1   
    if checkA == 1 and sumscore > 21:
      yourcards[yourcards.index(11)] = 1
  replaceA()
  
  sumscore = 0
  for i in yourcards:
    sumscore += i
  print(f"Your cards: {yourcards}, current score: {sumscore}")
  print(f"Computer's first hand: {compfirstcard}")
  
  to_continue = True
  while to_continue:
    more = input("Type 'y' to get another card, type 'n' to pass: ")
    if more == "y":
      yourcards.append(cards[random.randint(0,len(cards)-1)])
      sumscore = 0
      for i in yourcards:
        sumscore += i
      replaceA()
      sumscore = 0
      for i in yourcards:
        sumscore += i
      print(f"Your cards: {yourcards}, current score: {sumscore}")
      print(f"Computer's first hand: {compfirstcard}")
      if sumscore > 21:
        print("You went over. You lose")
        to_continue = False
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        clear()
    else:
      to_continue = False
      
      compscore = 0
      def compreplaceA():
        checkA = compcards.count(11)
        if checkA >= 2:
          compcards[compcards.index(11)] = 1   
        if checkA == 1 and compscore > 21:
          compcards[compcards.index(11)] = 1
      compreplaceA()
      for n in compcards:
        compscore += n
      while compscore < 17: 
        compscore = 0
        compcards.append(cards[random.randint(0,len(cards)-1)])
        compreplaceA()
        compscore = 0
        for n in compcards:
          compscore += n
      print(f"Your final hand: {yourcards}, final score: {sumscore}")
      print(f"Computer's final hand: {compcards}, final score: {compscore}")
      if compscore > 21:
        print("You win!")
      elif sumscore > compscore:
        print("You win!")
      elif sumscore == compscore:
        print("It's a draw")
      else:
        print("You lose")
      play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
      clear()





