# Program: Morse Code Translator, Text <-> Morse Code

# Dictionary mapping characters to Morse code
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',
    'X': '-..-',  'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

# Reverse dictionary for Morse to text conversion
REVERSE_MORSE_CODE = {value: key for key, value in MORSE_CODE.items()}


def text_to_morse(text):
    morse_result = []

    for char in text.upper():
        if char == ' ':
            morse_result.append('/')   # Separator for words
        elif char in MORSE_CODE:
            morse_result.append(MORSE_CODE[char])

    return ' '.join(morse_result)


def morse_to_text(morse):
    text_result = []
    words = morse.split(' / ')  # Split words

    for word in words:
        letters = word.split()
        for letter in letters:
            if letter in REVERSE_MORSE_CODE:
                text_result.append(REVERSE_MORSE_CODE[letter])
        text_result.append(' ')

    return ''.join(text_result).strip()

while True:
    print("=== Morse Code Translator ===")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")

    choice = input("Enter your choice (1, 2 or 3): ")

    if choice == '1':
        text = input("Enter text to convert: ")
        result = text_to_morse(text)
        print("Morse Code:")
        print(result)

    elif choice == '2':
        morse = input("Enter Morse code (use / for space between words): ")
        result = morse_to_text(morse)
        print("Translated Text:")
        print(result)

    elif choice == '3':
        break

    else:
        print("Invalid choice!")