import random
import string

print("Welcome to password generator")

def main():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    number_list = None
    letter_list = None
    symbol_list = None
    length = int(input("How many characters in your password?: "))

    letter_input = int(input("How many letters?: "))
    number_input = int(input("How many numbers?: "))
    symbol_input = int(input("How many symbols?:"))

    if length != letter_input + number_input + symbol_input:
        print("password length and preference length do not match")
        main()
    else:
        number_list = random.choices(numbers, k= number_input)
        symbol_list = random.choices(symbols, k= symbol_input)
        letter_list = random.choices(letters, k= letter_input)

    output = number_list + symbol_list + letter_list
    random.shuffle(output)
    password = ""
    for char in output:
        password += char
    print(f"Your password is: {password}")

main()
