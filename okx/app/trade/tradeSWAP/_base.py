from okx.app.account import AccountSWAP
from okx.app.market import MarketSWAP
from okx.api import Trade as TradeAPI


class TradeBase():
    def __init__(
            self,
            key: str,
            secret: str,
            passphrase: str,
            flag: str = '0',
            timezone: str = 'Asia/Shanghai',
            account=None,
            market=None,
            posmode: str = 'long_short_mode',
            proxies={},
            proxy_host: str = None,
    ):
        # SWAP账户
        if not account:
            self._account = AccountSWAP(key=key, secret=secret, passphrase=passphrase, flag=flag, proxies=proxies,
                                        proxy_host=proxy_host)
        else:
            self._account = account

        # SWAP行情
        if not market:
            self._market = MarketSWAP(key=key, secret=secret, passphrase=passphrase, flag=flag, timezone=timezone, proxies=proxies,
                                      proxy_host=proxy_host)
        else:
            self._market = market

        # 设置持仓方向
        set_position_mode_result = self._account.set_position_mode(
            posMode=posmode
        )
        if set_position_mode_result['code'] == '0':
            print('设置持仓方式为双向持仓成功' if posmode == 'long_short_mode' else '设置持仓方式为单向持仓成功')
        else:
            print("设置持仓方式失败。请先取消所有未成交订单，平掉所有持仓，并停止交易机器人。")

        # 时区
        self.timezone = timezone
        # TRADE API
        self.api = TradeAPI(key=key, secret=secret, passphrase=passphrase, flag=flag, proxies=proxies,
                            proxy_host=proxy_host)
