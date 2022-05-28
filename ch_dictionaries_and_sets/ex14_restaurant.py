MENU = {'Chicken Espetada': 28, 'Curried Chicken': 21, \
        'Sea Bass': 46, 'Butter Chicken': 22,\
        'Peli Peli Shrimp': 34, 'Cape Town Skillet': 49, \
        'Ribeye': 70, 'Lamb Chops': 40}

def restaurant():
    '''Asks the user to enter an order:
    Rule: - If the user enters the name of a dish on the menu, the function
    prints the price and the running total. It then asks the user again for
    their order.
    - If the user enters the name of a dish not on the menu, the program scolds
    the user. It then asks the uer again for their order.
    - If the user enters an empty string, the program stops prompting and
    prints the total amount.'''
    total = 0
    while True:
        order = input('Order:').strip()
        if order == '':
            print(f"Your total is {total}.")
            break
        elif order not in MENU.keys():
            print(f"Sorry, we are fresh out of {order} today.")
        else:
            total += MENU[order]
            print(f"{order} cost {MENU[order]}, total is {total}.")

if __name__ == "__main__":
    print("Today Menu:")
    print("-"*40)
    print(MENU)
    print("-"*40)
    restaurant()

