def future_value(present_value, annual_rate, periods_per_year, years):
   
    """
    Function to calculate future value based on a current investment amount, term structure, and interest rate
    """
    
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    FV = present_value * (1 + rate_per_period) ** periods #calculates future value based on compounding
    return FV

print ("test value is: ", future_value(500, .04, 10, 10))
print ("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))