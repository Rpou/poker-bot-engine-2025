from poker_game_runner.state import Observation
from poker_game_runner.utils import Range, HandType
import time
import random

BOT_NAME = "Doyle Botson" # Change this to your bot's name

class Bot:
  @classmethod
  def get_name_class(cls, path):
    return BOT_NAME

  def get_name(self):
      return BOT_NAME

  def act(self, obs: Observation):

    winProb = self.win_probability(obs)
    pot_odds = self.pot_odds(obs)
    
    current_bot_hand = obs.my_hand

    if obs.current_round == 0:
      if current_bot_hand[0][0] == current_bot_hand[1][0]: #pair
         winProb = self.cardValue(current_bot_hand[0][0]) + 20
      else: #highcard
         winProb = self.cardValue(current_bot_hand[0][0]) / 2 + self.cardValue(current_bot_hand[1][0]) / 2
         if current_bot_hand[0][1] == current_bot_hand[1][1]:
             winProb += 20
             if obs.my_index == 1 and len(obs.get_active_players()) > 4: #bigblind and many players
                winProb += 20
         if abs(self.difference(obs)) == 1:
           winProb += 20 
         if abs(self.difference(obs)) == 2:
           winProb += 8
         if abs(self.difference(obs)) == 3:
           winProb += 3  

    
    if winProb >= 100:
       return obs.get_max_raise()
    if winProb >= 80:
        return obs.get_pot_size() * 3
    elif winProb >= 70:   
        return obs.get_pot_size() * 2
    
    if pot_odds <= winProb:
       return 1     
    else:      
        return 0

  def fold_or_check():
    return 0;

  def call_or_check():
    return 1;

  def raise_amount(self,amount):
    return amount;

  def pot_odds(self, obs):
    pot_size = obs.get_pot_size()  
    call_size = obs.get_call_size()  
    try:
        return call_size / pot_size * 100
    except ZeroDivisionError:  #if nothing is betted potodds always 0
        return 0
    

  def cardValue(self, card):
    match card:
        case "2":
            return 5
        case "3":
            return 10
        case "4":
            return 15
        case "5":
            return 20
        case "6":
            return 25
        case "7":
            return 30
        case "8":
            return 35
        case "9":
            return 40
        case "T":  # 'T' represents 10
            return 45
        case "J":
            return 50
        case "Q":
            return 55
        case "K":
            return 70
        case "A":  # Ace is the highest
            return 80
  
  def win_probability(self, obs):
    current_bot_hand = obs.get_board_hand_type()

    current_hand_score = 0;

    if current_bot_hand == HandType.HIGHCARD:
      current_hand_score += 0;
    elif current_bot_hand == HandType.PAIR:
      current_hand_score += 30;
    elif current_hand_score == HandType.TWOPAIR:
      current_hand_score += 65;
    elif current_hand_score == HandType.THREEOFAKIND:
      current_hand_score += 70;
    elif current_hand_score == HandType.STRAIGHT:
      current_hand_score += 82;
    elif current_hand_score == HandType.FLUSH:
      current_hand_score += 85;
    elif current_hand_score == HandType.FULLHOUSE:
      current_hand_score += 90;
    elif current_hand_score == HandType.FOUROFAKIND:
      current_hand_score += 100;
    elif current_hand_score == HandType.STRAIGHTFLUSH:
      current_hand_score += 100
    
    my_hand = obs.my_hand

    card1Rank = my_hand[0][1];
    card2Rank = my_hand[1][1];

    if obs.current_round <= 2:
      if card1Rank == card2Rank:
        board_cards = obs.board_cards
        suits = [card[1] for card in board_cards]

        filtered_suits = [suit for suit in suits if suit == card1Rank]
        if len(filtered_suits) >= 2:
          current_hand_score += 30
        elif len(filtered_suits) == 1:
          current_hand_score += 12
      
    return current_hand_score;


  def difference(self, obs: Observation):
    current_bot_hand = obs.my_hand
    cardOne = -1
    cardTwo = -1
    if current_bot_hand[0][0] == 'T':
      cardOne = 10
    if current_bot_hand[1][0] == 'T':
      cardTwo = 10
    if current_bot_hand[0][0] == 'J':
      cardOne = 11
    if current_bot_hand[1][0] == 'J':
      cardTwo = 11
    if current_bot_hand[0][0] == 'Q':
      cardOne = 12
    if current_bot_hand[1][0] == 'Q':
      cardTwo = 12
    if current_bot_hand[0][0] == 'K':
      cardOne = 13
    if current_bot_hand[1][0] == 'K':
      cardTwo = 13
    if current_bot_hand[0][0] == 'A':
      cardOne = 14
    if current_bot_hand[1][0] == 'A':
      cardTwo = 14

    if cardOne != -1 and cardTwo != -1:
      return cardTwo-cardOne
    if cardOne != -1:
      return int(current_bot_hand[1][0])-cardOne
    if cardTwo != -1:
      return cardTwo - int(current_bot_hand[0][0])
    return int(current_bot_hand[1][0]) - int(current_bot_hand[0][0])

      


