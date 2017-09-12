# encoding: utf-8

import random
import operator

config = {
    'init_price': 12.0,
    'buy_ratio': 0.9,  # buy when the price is 70% of the last trading price
    'sell_ratio': 1.2, # sell when the price is 150% of the last trading price
}
br_list = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
sr_list = [1.95, 1.9, 1.85, 1.8, 1.75, 1.7, 1.65, 1.6, 1.55, 1.5, 1.45, 1.4, 1.35, 1.3, 1.25, 1.2, 1.15, 1.1, 1.05]

class Trader(object):
    def __init__(self, cash=999999):
        self.cash = cash    # total
        self.market_value = 0
        self.market_volume = 0
        self.trade_record = []
    
    @property
    def total_fund(self):
        return self.cash + self.market_value
    
    def buy(self, p, v):# p --> price   v --> volume
        if self.cash < p*v:
            print 'not enough money,cant buy', p , v
            return
        self.cash -= p*v
        self.cash - p*v*0.01
        self.market_volume += v
        self.market_value += p*v
        self.trade_record.append(('B', p, v))
    
    def sell(self, p, v):
        if self.market_volume < v:
            print 'not enough volume to sell'
            return
        self.market_value = self.market_volume * p
        self.cash += p*v
        self.cash - p*v*0.01
        self.market_volume -= v
        self.market_value -= p*v
        self.trade_record.append(('S', p, v))
    
    def fake_trading(self, price_list, buy_ratio, sell_ratio):
        
        #print 'b s ratio', br, sr
        if len(self.trade_record) == 0:
            self.buy(config['init_price'], 1000)
        for p in price_list:
            if p <= 0:
                print 'price < 0 '
                return
            last_trade = self.trade_record[-1]
            last_trade_price = last_trade[1]
            last_trade_volume = last_trade[2]
            if p >= last_trade_price * sell_ratio:
                
                #volume = last_trade_volume
                volume = int(self.market_volume / 4)
                self.sell(p, volume)
            elif p <= last_trade_price * buy_ratio:
                volume = int(last_trade_price * last_trade_volume / p)
                #volume = last_trade_volume  # no
                self.buy(p, volume)

def __random_in_range(num, low, high):
    '''sample  low = 0.9  high = 1.1  返回一个num的90%到110%'''
    return round(random.random() * (high*num - low*num) + low*num, 2)

def get_price_sequence(length, low, high):
    '''产生一个数列，后一项是前一项的low到high之间的值'''
    init_price = 10
    sequence = [init_price]
    for n in range(1, length):
        sequence.append(__random_in_range(sequence[n-1], low, high))
        print sequence[n]
    return sequence

sequence2 = [10, 10.76, 9.93, 7.95, 7.71, 7.61, 8.7, 9.61, 9.47, 9.23, 10.81, 11.02, 10.66, 9.37, 8.61, 8.67, 10.64, 10.53, 10.09, 10.06, 10.19, 8.24, 10.12, 11.97, 10.98, 13.11, 13.39, 13.84, 17.02, 20.6, 24.74, 28.82, 34.68, 40.96, 44.69, 54.33, 62.9, 58.09, 55.86, 45.28, 44.91, 49.71, 39.96, 33.86, 39.23, 48.7, 57.47, 57.38, 50.88, 52.02, 59.42, 68.67, 85.03, 73.46, 70.21, 71.14, 68.62, 69.48, 69.5, 86.25, 76.58, 94.79, 85.73]
sequence3 = [10, 8.58, 9.12, 10.72, 10.51, 9.88, 12.07, 14.47, 16.66, 17.84, 21.59, 23.64, 22.34, 22.15, 17.74, 20.32, 20.4, 16.74, 19.68, 18.12, 18.94, 18.33, 17.77, 14.31, 15.02, 16.85, 19.45, 19.08, 23.12, 22.84, 21.93, 21.65, 22.06, 22.09, 22.33, 24.5, 19.99, 21.98, 24.37, 22.48, 18.03, 14.98, 12.97, 14.56, 11.68, 13.11, 10.52, 12.72, 12.39, 10.52, 9.84, 8.88, 8.8, 10.19, 9.77, 11.58, 12.48, 10.24, 10.69, 9.87, 9.99, 10.6]
sequence4 = [10, 8.42, 9.51, 10.37, 9.94, 9.54, 8.69, 8.46, 10.19, 10.03, 8.92, 8.21, 7.71, 7.78, 8.71, 9.89, 10.44, 10.87, 8.74, 8.55, 8.56, 9.69, 7.91, 8.23, 6.82, 6.87, 7.27, 8.4, 8.42, 7.55, 6.38, 7.22, 8.5, 7.84, 6.96, 6.09, 6.33, 6.34, 7.26, 8.95, 9.47, 11.36, 12.75, 14.01, 12.31, 11.49, 9.85, 8.12, 6.79, 7.78, 8.06, 7.56, 6.33, 7.57, 7.6, 8.75, 10.77, 10.54, 10.59, 9.72, 10.25, 9.23, 8.56, 7.13, 6.61, 7.13, 6.89, 7.84]
sequence5 = [10, 8.99, 9.38, 10.63, 12.11, 10.05, 11.31, 13.7, 13.15, 15.88, 15.37, 12.87, 15.73, 13.97, 13.7, 12.59, 10.21, 12.5, 14.8, 15.95, 16.92, 13.6, 14.52, 13.17, 10.96, 12.32, 13.06, 14.01, 16.01, 16.23, 14.66, 14.1, 14.75, 13.74, 11.81, 13.95, 15.28, 14.12, 16.43, 20.22, 20.53, 16.95, 14.78, 16.61, 16.16, 12.96, 10.91, 13.31, 15.04, 12.55, 15.1, 18.47, 19.89, 20.98, 17.08, 17.72, 17.47, 19.39, 20.91, 16.95, 17.48, 16.21, 17.09, 15.11, 13.33, 13.31, 11.47, 14.2, 11.77, 12.27]

def test__random_in_range():
    result = []
    for n in range(99999):
        result.append(__random_in_range(10, 0.5, 1.5))
    print max(result), min(result) # should be 1.5 0.5
#test__random_in_range()

def test_get_price_sequence():
    print get_price_sequence(70, 0.8, 1.238)
#test_get_price_sequence()


results = []

for br in br_list:
    for sr in sr_list:
        
        trader = Trader()
        
        #br = config['buy_ratio']
        #sr = config['sell_ratio']
        #trader.fake_trading(price_list(9999), br, sr)
        trader.fake_trading(sequence5, br, sr)
        #print 'total fund:', trader.total_fund
        results.append((trader.total_fund, br, sr))

s_results = sorted(results, key=operator.itemgetter(0))
print s_results[-5:]

'''
    print 'current cash: ', trader.cash
    print 'current market value: ', trader.market_value
    print 'current market volume: ', trader.market_volume
    print 'total fund:', trader.total_fund
    '''
