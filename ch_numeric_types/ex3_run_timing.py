# The function run_timing asks how long it took the user to run 10km.
# It continues to ask how long (in minutes) it took for additional runs until
# the user presses Enter. 
# Then the function exits and display the average time that the 10km run took.

def run_timing():
    s = 0
    count = 0
    while True: 
        x = input("Enter 10 km run time:")
        if x!= "":
            s += float(x)
            count += 1
        else:
            print(f"Average of {s / count}, over {count} runs")
            break

if __name__ == "__main__":
        run_timing()
