from Stock import Stock


todays_market = Stock()
stock_name = input("Please provide the stock's name:\n")
Stock.set_stock_name(todays_market, stock_name)
stock_symbol = stock_name[:3].upper()
Stock.set_stock_symbol(todays_market, stock_symbol)
current_price = input("What is the current price of {}?\n".format(stock_symbol))
Stock.set_current_price(todays_market, current_price)
closing_price = input("What is the closing price of {}?\n".format(stock_symbol))
Stock.set_previous_closing_price(todays_market, closing_price)

change = Stock.get_change_percent(todays_market, closing_price, current_price)
print("The stock of {} ({}) closed today at ${} which is a {}% change "
      "from it's opening price of ${}.".format(Stock.get_stock_name(todays_market),
                                              Stock.get_symbol(todays_market),
                                              Stock.get_previous_closing_price(todays_market),
                                              change,
                                              Stock.get_current_price(todays_market)))
