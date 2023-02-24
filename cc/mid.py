import time
import logging
import logging.config
from ccxt import Exchange

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


class Mid:
    def __init__(self, symbol, exchange: Exchange):
        self.ticker = {}
        self.balances = {}
        self.exchange = exchange
        self.init_timestamp = time.time()
        self.name = self.exchange.name
        self.jyd = self.exchange.currencies
        self.symbol = symbol
        logger.info(self.name)

    def get_balance(self):
        try:
            balance_info = self.exchange.fetch_balance()
            self.balances = balance_info["free"]
            return True
        except:
            return False

    def get_ticker(self):
        try:
            ticker = self.exchange.fetch_ticker(self.symbol)
            self.ticker = ticker
            return True
        except:
            return False

    def create_limit_order(self, hand_type, amount, price):
        try:
            return self.exchange.create_limit_order(self.symbol, hand_type, amount, price)
        except:
            time.sleep(1)
            return self.exchange.create_limit_order(self.symbol, hand_type, amount, price)

    def create_market_order(self, hand_type, amount):
        try:
            return self.exchange.create_market_order(self.symbol, hand_type, amount)
        except:
            time.sleep(1)
            return self.exchange.create_market_order(self.symbol, hand_type, amount)

    def cancel_order(self, order_id):
        try:
            return self.exchange.cancel_order(order_id)
        except:
            time.sleep(1)
            return self.exchange.cancel_order(order_id)

    def renovate_data(self):
        if not self.get_balance():
            logger.error("get_balance error")
            return False
        time.sleep(0.1)
        if not self.get_ticker():
            logger.error("get_ticker error")
            return False
        time.sleep(0.1)
