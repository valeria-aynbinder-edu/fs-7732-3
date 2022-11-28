stocks_data = {
    'TSLA': {
        'ticker': 'TSLA',
        'company_name': 'Tesla',
        'employees_number': 5000,
        'address': 'Claifornia',
        'CEO_name': 'Elon Musk',
        'stock_data':{
            '14.11.2021': {
                'open': 1001.5,
                'close': 1020,
                'volume': 50000000
            },
            '15.11.2021':{
                'open': 1067.7,
                'close': 1045.5,
                'volume': 45000345
            }
        },
    },

    'AAPL': {
        'ticker': 'AAPL',
        'company_name': 'Apple',
        'employees_number': 10000,
        'address': 'New York',
        'CEO_name': 'Tim Cook',
        'stock_data': {
            '14.11.2021': {
                'open': 320.7,
                'close': 322.8,
                'volume': 5_345_333
            },
            '15.11.2021': {
                'open': 300.7,
                'close': 320.5,
                'volume': 4_000_345
            }
        }
    }
}

{'TSLA' : {'open_avg': 34534,
           'close_avg': 456,
           'volume_avg': 45684598}}


def get_stocks_stats(stocks_dict: dict) -> dict:
    # for ticker in stocks_dict:
    #     print(ticker)
    #     print(stocks_dict[ticker])
    ret_dict = {}
    for ticker, company_dict in stocks_dict.items():
        ret_dict[ticker] = {}
        open_sum = 0
        close_sum = 0
        volume_sum = 0
        for date, stock_prices in company_dict['stock_data'].items():
            open_sum += stock_prices['open']
            close_sum += stock_prices['close']
            volume_sum += stock_prices['volume']
        ret_dict[ticker]['open_avg'] = open_sum / len(company_dict['stock_data'])
        ret_dict[ticker]['close_avg'] = close_sum / len(company_dict['stock_data'])
        ret_dict[ticker]['volume_avg'] = volume_sum / len(company_dict['stock_data'])
    return ret_dict

ret_val = get_stocks_stats(stocks_data)
print(ret_val)
