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
             if obs.my_index == 1 and obs.get_active_players > 4: #bigblind and many players
                winProb += 20
         #if current_bot_hand[]     

    if pot_odds < winProb:
       return 1     
    else:      
      return 0

  def fold_or_check():
    return 0;

  def call_or_check():
    return 1;

  def raise_amount(amount):
    return amount;

  def win_probability(obs: Observation):
    current_bot_hand = obs.get_board_hand_type()

    current_hand_score = 0;

    if current_bot_hand == HandType.HIGHCARD:
      current_hand_score + 1;

  def pot_odds(obs):
    pot_size = obs.get_pot_size  
    call_size = obs.get_call_size  
    try:
        return call_size / pot_size
    except ZeroDivisionError:  #if nothing is betted potodds always 0
        return 0
    

  def cardValue(card):
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
  

