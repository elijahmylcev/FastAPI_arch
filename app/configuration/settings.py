import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ALL_CURRENCY_PAIRS_KEYS = os.getenv('ALL_CURRENCY_PAIRS_KEYS')
CURRENCY_PAIR_KEY = os.getenv('CURRENCY_PAIR_KEY')
REDIS_HOST = os.getenv('REDIS_HOST')
