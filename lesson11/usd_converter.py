class USDConverter:
    def __init__(self):
        # stores rates FROM usd maps from currency to rate
        self.exchange_rates = {}
        # 'NIS': 3.5,  -> $1 = 3.5NIS
        # 'EURO': 0.98, ->
        # 'USD': 1

    def add_exchange_rate_from_usd(self, currency: str, rate: float):
        self.exchange_rates[currency] = rate

    def convert_from_usd(self, currency, amnt) -> float:
        if currency in self.exchange_rates:
            return amnt * self.exchange_rates[currency]
        else:
            print(f"Currency {self.currency} does not exist")
            return None

    def convert_to_usd(self, currency, amnt):
        if currency in self.exchange_rates:
            return amnt / self.exchange_rates[currency]
        else:
            print(f"Currency {self.currency} does not exist")
            return None

