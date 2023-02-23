import ccxt
import logging


def account():
    # okx
    apikey = 'a6580631-c900-443c-81f3-accf67a4cf6e'
    secretkey = 'D3AD7738AEB904CC00B49C0EE6D01333'
    API_PASSPHRASE = '900730lB@'
    exchange = ccxt.okex5(
        {
            'apiKey': apikey,
            'secret': secretkey,
            'password': API_PASSPHRASE
        })
    print(exchange.urls)

    order_symbol = 'ETH/USDT'
    ETH_Last = exchange.fetch_ticker(order_symbol)['last']
    print('ETH 最新价格:' + str(ETH_Last))


if __name__ == '__main__':
    account()
