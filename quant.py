from cryptoquant.api.okex.okex_spot_exchange import OkexSpotApi
#导入交易所接口密钥
from cryptoquant.config.config import ok_api_key, ok_seceret_key, ok_passphrase
from cryptoquant.api.okex.spot_api import SpotAPI
from cryptoquant.api.api_gateway.apigateway import ApiGateway

# 实例化OKEX接口的类
api = SpotAPI(ok_api_key, ok_seceret_key, ok_passphrase, True)
# 实例化自己封装好接口类
api_gateway = OkexSpotApi(api)
# 实例化策略与交易所接口之间的中间通道类
exchange = ApiGateway(api_gateway)
kline_df = exchange.get_kline_data(symbol, minutes)
print(kline_df)
ticker = exchange.get_ticker(symbol)
print(ticker)

# 买单
order_data = exchange.buy(symbol,3,1)
# 卖单
# order_data = exchange.sell(symbol, 6, 1)