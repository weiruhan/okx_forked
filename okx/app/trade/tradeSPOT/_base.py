from okx.app.account import AccountSPOT
from okx.app.market import MarketSPOT
from okx.api import Trade as TradeAPI


class TradeBase():
    def __init__(
            self,
            key: str,
            secret: str,
            passphrase: str,
            flag = '0',
            timezone: str = 'Asia/Shanghai',
            account=None,
            market=None,
            proxies={},
            proxy_host: str = None,
    ):
        # SWAP账户
        if not account:
            self._account = AccountSPOT(key=key, secret=secret, passphrase=passphrase, flag=flag, proxies=proxies,
                                        proxy_host=proxy_host)
        else:
            self._account = account

        # SWAP行情
        if not market:
            self._market = MarketSPOT(key=key, secret=secret, passphrase=passphrase, flag=flag, timezone=timezone, proxies=proxies,
                                      proxy_host=proxy_host)
        else:
            self._market = market

        # 时区
        self.timezone = timezone
        # TRADE API
        self.api = TradeAPI(key=key, secret=secret, passphrase=passphrase, flag=flag, proxies=proxies,
                            proxy_host=proxy_host)
