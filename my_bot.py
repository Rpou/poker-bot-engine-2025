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
    # Your code here
    return 0;

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
