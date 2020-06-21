import random
import string

print("Welcome to password generator")


def main():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    length = int(input("How long your will your password be?: "))
    letter_count = int(input("How many letters?: "))
    number_count = int(input("How many numbers?: "))
    symbol_count = int(input("How many symbols?: "))

    if length != letter_count + number_count + symbol_count:
        letter_list = random.choices(letters, k=letter_count)
        number_list = random.choices(numbers, k=number_count)
        symbol_list = random.choices(symbols, k=symbol_count)
        
        add = random.choice([letter_list, number_list, symbol_list])
        fin = random.choices(add, k=length - letter_count - number_count - symbol_count)

        output = letter_list + number_list + symbol_list + fin
        random.shuffle(output)

        password = ""
        for char in output:
            password += char

    else:
        letter_list = random.choices(letters, k=letter_count)
        number_list = random.choices(numbers, k=number_count)
        symbol_list = random.choices(symbols, k=symbol_count)

        output = letter_list + number_list + symbol_list
        random.shuffle(output)

        password = ""
        for char in output:
            password += char

    print(f"Your password is: {password}")


main()
