# encoding: utf-8
import random
import xlrd

#book = xlrd.open_workbook('/Users/myc/Desktop/aa.xlsx')
#sheet = book.sheet_by_index(0)
#
## read
#row = sheet.row(0)
#row_values = sheet.row_values(0)
#cell = sheet.cell(0, 0).value
#print type(row[1])
#print row_values
#print cell
#print sheet.nrows,'nrows'
'''

'''

class ExcelApp(object):
    def __init__(self, path, sheet_index=0):
        book = xlrd.open_workbook(path)
        self.sheet = book.sheet_by_index(sheet_index)
        self.sheet_rows = self.sheet.nrows


class Bar(object):
    def __init__(self, row_index):
        values = app.sheet.row_values(row_index)
        self.date = values[0]
        self.open = values[1]
        self.high = values[2]
        self.low = values[3]
        self.close = values[4]
        #self.cjl = values[5]  # 成交量
        #self.ccl = values[6]  # 持仓量
        
    def is_yin(self):
        return self.open > self.close

    def is_yang(self):
        return self.close < self.open


app = ExcelApp('/Users/myc/Desktop/work_note/myCoding/back_testing/bars.xlsx')


class Bars(object):
    def __init__(self):
        self.bars = []
        for n in range(app.sheet_rows):
            if n == 0: continue
            self.bars.append(Bar(n))

    def __getitem__(self, i):
        if not isinstance(i, int):
            return
        if not 0 <= i <= len(self.bars):
            return
        return self.bars[i]

    def ma(self, bar_index, bar_num):
        #for n in range()
        #closes = 
        start_bar_index = bar_index - bar_num + 1
        if start_bar_index < 0:
            print 'in Bars ---- MA :there is no MA'
            return None
        if bar_index > len(self.bars) - 1:
            print 'in Bars ---- MA : the bar index out of range'
            return None
        index_range = range(start_bar_index, bar_index + 1)
        close_sum = 0
        for n in index_range:
            close_sum += self.bars[n].close
        return close_sum / bar_num
#bars = []
#for n in range(app.sheet_rows):
#    if n == 0: continue
#    bars.append(Bar(n))
#print bars[15].open

#print bars[16].open


class Trader(object):
    def __init__(self, available=40000):
        self.available = available
        self.market_value = 0
        self.market_volume = 0
        self.position_list = []

    def whole_capital(self, current_bar):
        capital = self.available
        for position in self.position_list:
            capital + position.floating_profit(current_bar)
        return capital

    def buy(self, current_bar):
        pass

    def sell(self, current_bar):
        pass


class Position(object):
    '''
    仓位
    保证金为买卖价
    一手一个单位
    '''
    def __init__(self, price, bs):
        self.price = price  # 开仓价格
        self.bs = bs  # 买或卖
    
    def floating_profit(self, current_bar): 
        '''
        Floating profit(返回负数就是亏损 loss)
        开仓以开盘价  平仓以收盘价
        浮盈浮亏都简单相加减, 而不以平均价
        '''
        if self.bs == 'b':
            return current_bar.close - self.price
        if self.bs == 's':
            return self.price - current_bar.close

    
if __name__ == '__main__':
    pass

    bars = Bars()
    print type(bars[15].open)
    print bars.ma(15,5)
    trader = Trader(40000)


