# Program: Roman Numeral Converter, Integer <-> Roman Numeral

# Ordered list of Roman numeral values
ROMAN_VALUES = [
    (1000, 'M'), (900, 'CM'),
    (500, 'D'),  (400, 'CD'),
    (100, 'C'),  (90, 'XC'),
    (50, 'L'),   (40, 'XL'),
    (10, 'X'),   (9, 'IX'),
    (5, 'V'),    (4, 'IV'),
    (1, 'I')
]

ROMAN_TO_INT = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100,
    'D': 500, 'M': 1000
}


def int_to_roman(number):
    roman_result = ""

    for value, symbol in ROMAN_VALUES:
        while number >= value:
            roman_result += symbol
            number -= value

    return roman_result


def roman_to_int(roman):
    total = 0
    prev_value = 0

    for char in reversed(roman.upper()):
        current_value = ROMAN_TO_INT[char]

        # Subtraction rule
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total


while True:
    print("=== Roman Numeral Converter ===")
    print("1. Integer to Roman Numeral")
    print("2. Roman Numeral to Integer")
    print("3. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        number = int(input("Enter an integer (1 - 3999): "))
        if 1 <= number <= 3999:
            print("Roman Numeral:", int_to_roman(number))
        else:
            print("Number out of range!")

    elif choice == '2':
        roman = input("Enter a Roman numeral: ")
        print("Integer Value:", roman_to_int(roman))

    elif choice == '3':
        break

    else:
        print("Invalid choice!")
