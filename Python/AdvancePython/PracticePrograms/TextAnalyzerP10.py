# Program: Text Analyzer (Palindrome + Frequency + Reverse)

def clean_text(text):
    # Remove spaces and convert to lowercase
    return text.replace(" ", "").lower()


def is_palindrome(text):
    # Check if cleaned text is same as reverse
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]


def char_frequency(text):
    # Count frequency of each character
    freq = {}

    for char in text:
        if char != " ":   # ignore spaces
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    return freq


def reverse_text(text):
    # Reverse the string
    return text[::-1]


while True:
    print("\n=== Text Analyzer ===")
    print("1. Check Palindrome")
    print("2. Character Frequency")
    print("3. Reverse Text")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text: ")

        if is_palindrome(text):
            print("It is a palindrome!")
        else:
            print("Not a palindrome.")

    elif choice == "2":
        text = input("Enter text: ")
        freq = char_frequency(text)

        print("Character Frequency:")
        for char, count in freq.items():
            print(char, "->", count)

    elif choice == "3":
        text = input("Enter text: ")
        print("Reversed Text:", reverse_text(text))

    elif choice == "4":
        break

    else:
        print("Invalid choice!")