class Stock:
    def __init__(self):
        self.symbol = ''
        self.name = ''
        self.previous_closing_price = 0.0
        self.current_price = 0.0

    def set_stock_name(self, name):
        self.name = name

    def get_stock_name(self):
        return self.name

    def set_stock_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def set_previous_closing_price(self, previous_price):
        self.previous_closing_price = previous_price

    def get_previous_closing_price(self):
        return self.previous_closing_price

    def set_current_price(self, current_price):
        self.current_price = current_price

    def get_current_price(self):
        return self.current_price

    def get_change_percent(self, previous_price, current_price):
        previous_price_num = float(previous_price)
        current_price_num = float(current_price)
        if previous_price_num >= current_price_num:
            increase = previous_price_num - current_price_num
            percent_increase = increase / previous_price_num * 100
            return str(round(percent_increase, 2))
        else:
            decrease = current_price_num - previous_price_num
            percent_decrease = decrease / current_price_num * 100
            return '-' +  str(round(percent_decrease, 2))
