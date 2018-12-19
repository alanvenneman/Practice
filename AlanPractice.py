try:
    numS = float(raw_input("How Many"))
except ValueError as e:
    print("Please use numerals for your answer - {}.").format(e)
