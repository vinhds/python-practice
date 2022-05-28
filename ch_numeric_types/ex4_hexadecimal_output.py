def hex_output(hex_number):
   '''Takes a hexadecimal number and returns the decimal equivalent'''
   hex_digits = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
   unpacked_hex_num = enumerate(hex_number)
   s = 0
   l = len(hex_number)-1
   for power,digit in unpacked_hex_num:
       if digit in hex_digits.keys():
           s += hex_digits[digit] * 16**(l - power)
       else:
           s += int(digit) * 16**(l - power)
   return s

if __name__ == "__main__":
    user_input = input("Please enter a hex number: ")
    print(f"The decimal equivalent of {user_input} is {hex_output(user_input)}")

