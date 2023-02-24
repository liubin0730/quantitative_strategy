import ccxt


def okex5():
    apikey = 'a6580631-c900-443c-81f3-accf67a4cf6e'
    secretkey = 'D3AD7738AEB904CC00B49C0EE6D01333'
    API_PASSPHRASE = '900730lB@'
    exchange = ccxt.okex5(
        {
            'apiKey': apikey,
            'secret': secretkey,
            'password': API_PASSPHRASE
        })
    return exchange
