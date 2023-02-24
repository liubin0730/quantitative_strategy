import ccxt


def bitmex():
    apikey = 'R1ZVd4YlZoQUa91QIX-E_3Fb'
    secretkey = 'bXdd8qE1fac-u_AHFqbm8FpEdEmMXvip8kZKkdNHqBqsTmO2'
    exchange = ccxt.bitmex(
        {
            'apiKey': apikey,
            'secret': secretkey,
        })
    exchange.urls['api'] = exchange.urls['test']

    return exchange
