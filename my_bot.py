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
    self.win_probability(obs)
    return 0;

  def fold_or_check():
    return 0;

  def call_or_check():
    return 1;

  def raise_amount(amount):
    return amount;

  def win_probability(self, obs):
    current_bot_hand = obs.get_board_hand_type()

    current_hand_score = 0;

    if current_bot_hand == HandType.HIGHCARD:
      current_hand_score + 1;
    elif current_bot_hand == HandType.PAIR:
      current_hand_score + 2;
    elif current_hand_score == HandType.TWOPAIR:
      current_hand_score + 4;
    elif current_hand_score == HandType.THREEOFAKIND:
      current_hand_score + 6;
    elif current_hand_score == HandType.STRAIGHT:
      current_hand_score + 8;
    elif current_hand_score == HandType.FLUSH:
      current_hand_score + 10;
    elif current_hand_score == HandType.FULLHOUSE:
      current_hand_score + 12;
    elif current_hand_score == HandType.FOUROFAKIND:
      current_hand_score + 14;
    elif current_hand_score == HandType.STRAIGHTFLUSH:
      current_hand_score + 20
    
    my_hand = obs.my_hand

    card1Rank = my_hand[0][1];
    card2Rank = my_hand[1][1];

    if obs.current_round <= 2:
      if card1Rank == card2Rank:
        board_cards = obs.board_cards
        suits = [card[1] for card in board_cards]

        filtered_suits = [suit for suit in suits if suit == card1Rank]
        if len(filtered_suits) >= 2:
          current_hand_score + 10
      
    return current_hand_score;
      

