def get_rainfall():
    '''Ask the user to enter the name of a city, if the city's name is not
    blank, the program asks the user how much rain has fallen in that city.
    Continue until the city's name is blank or the user presses enter. Then the
    program prints a report that details how much total rainfall there was in
    each city'''
    rainfall_report = {}
    while True:
        city = input("Please enter the name of a city:\n").strip()
        if city == '':
            print(10*"-" + "Rainfall Report" + 10*"-")
            for city, rainfall in rainfall_report.items():
                print(f"{city}: {rainfall}")
            break
        else:
            rainfall = int(input(f"How much rain has fallen in {city}?\n"))
            rainfall_report[city] = rainfall_report.get(city, 0) + rainfall




if __name__ == "__main__":
    get_rainfall()
