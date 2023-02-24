import time

from cc.mid import Mid
from exchange.okex5 import okex5
from cc.average import Average

if __name__ == '__main__':
    exchange = okex5()
    symbol = "BLUR/USDT"
    mid = Mid(symbol, exchange)
    mid.renovate_data()
    average = Average(mid)

    while True:
        time.sleep(5)
        average.make_need_account_info()
        average.if_need_trade(2)
