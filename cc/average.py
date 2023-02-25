import time
from cc.mid import Mid
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


# 均仓策略
class Average:
    def __init__(self, mid: Mid):
        self.need_sell = 0
        self.need_buy = 0
        self.jys = mid
        self.last_time = time.time()
        self.Buy_count = 0
        self.Sell_count = 0
        f = open("./price", encoding='utf-8')
        line = f.readline()
        self.last_trade_price = float(line)
        f.close()

    def make_need_account_info(self):
        self.jys.renovate_data()
        symbol = self.jys.symbol[:-5]
        self.B = self.jys.balances[symbol] if symbol in self.jys.balances else 0
        self.money = self.jys.balances["USDT"]

        now_price = self.jys.ticker["last"]
        logger.info("%s：%s USDT：%s 【共】：%s USDT", symbol, round(self.B * now_price, 2),
                    round(self.money, 2), round(self.B * now_price+self.money, 2))

        self.total_money = self.B * now_price + self.money
        self.half_money = self.total_money / 2
        self.need_buy = round((self.half_money - self.B * now_price) / now_price, 2)
        self.need_sell = round((self.half_money - self.money) / now_price, 2)
        logger.info("need_buy:%s, need_sell:%s", self.need_buy, self.need_sell)

    def do_average(self):
        self.need_buy = self.need_buy if self.need_buy >= 10 else 10
        self.need_sell = self.need_sell if self.need_sell >= 10 else 10
        if self.need_buy >= 10:
            self.jys.create_limit_order('buy', self.need_buy, self.jys.ticker["ask"])
            self.Buy_count += 1
            logger.info(f"【买入】{self.jys.symbol}:{self.need_buy} 【委托价格】{self.jys.ticker['ask']}")
            return True
        elif self.need_sell >= 10:
            self.jys.create_limit_order('sell', self.need_sell, self.jys.ticker["bid"])
            self.Sell_count += 1
            logger.info(f"【卖出】{self.jys.symbol}:{self.need_buy} 【委托价格】{self.jys.ticker['bid']}")
            return True
        logger.info('Buy_times:%s, Sell_times:%s', self.Buy_count, self.Sell_count)
        return False

    def if_need_trade(self, incr):
        fl = round(((self.jys.ticker["last"] - self.last_trade_price) / self.last_trade_price) * 100, 2)

        logger.info("上次价格：%s, 当前价格：%s, 价格浮动：%s", self.last_trade_price, self.jys.ticker["last"], f"{fl}%")
        if abs(fl) > incr:
            if self.do_average():
                self.last_trade_price = self.jys.ticker["last"]
                f = open("./price", "w", encoding='utf-8')
                f.write(self.jys.ticker["last"])
                f.close()
        logger.info("-----------------------------------------------------------")