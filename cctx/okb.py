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
            'password': API_PASSPHRASE,
            'options': {
                'defaultType': 'swap'
            },
            'headers': {
                'x-simulated-trading': '1'
            }
        })
    print(exchange.urls)
    exchange.load_markets()

    # bitmex = ccxt.bitmex({
    #     "apiKey": "X6hs2-akD2YUePded_Gj1l0X",
    #     "secret": "bDcl0BJ-KkaHUgu38IOjXdf9krHHoSe0EB3SclXNB7I_3MiT"
    # })
    # bitmex = ccxt.bitmex()
    # bitmex.apiKey = "X6hs2-akD2YUePded_Gj1l0X"
    # bitmex.secret = "bDcl0BJ-KkaHUgu38IOjXdf9krHHoSe0EB3SclXNB7I_3MiT"
    # print(bitmex.urls)
    # bitmex.urls['api'] = bitmex.urls['test']
    order_symbol = 'ETH/USDT'
    ETH_Last = exchange.fetch_ticker(order_symbol)['last']
    logging.info('ETH 最新价格:' + str(ETH_Last))


if __name__ == '__main__':
    account()
