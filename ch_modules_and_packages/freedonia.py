class HourOutOfBoundsError(Exception): pass

def calculate_tax(purchase_amt:float, province:str, hour:int):
    """Calculate the final price as a float
    purchase_amt: A float that represents the amount of the purchase
    province: a string that represents the province in which the purchase takes place
    hour: an integer from 0-24 that represents when the purchase happened
    The 4 provinces with their tax rates are:
        Chico: 50%
        Groucho: 70%
        Harpo: 50%
        Zeppo: 40%
    The tax percentage is also multipled by the hour at which the purchase is made.
    For example, if the hour is 11pm, the tax percentage will be multiplied by 23/24.
    """
    province_rates_dict = {'Chico': 0.5, 'Groucho': 0.7, 'Harpo': 0.5, 'Zeppo': 0.4}
    if hour < 0 or hour >=24:
        raise HourOutOfBoundsError(f'Hour must be >= 0 and < 24')
    return purchase_amt * (1 + province_rates_dict[province] * hour / 24)


