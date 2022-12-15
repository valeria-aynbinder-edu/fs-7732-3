from lesson7.usd_converter import USDConverter

if __name__ == '__main__':
    converter = USDConverter()

    converter.add_exchange_rate_from_usd('NIS', 3.16)
    converter.add_exchange_rate_from_usd('YEN', 113.73)
    converter.add_exchange_rate_from_usd('EURO', 0.89)
    yens = converter.convert_from_usd('YEN', 10000)
    dollars = converter.convert_to_usd('YEN', 10000)
    print(f"10000 USD = {yens}")
    print(f"10000 YEN = {dollars} USD")