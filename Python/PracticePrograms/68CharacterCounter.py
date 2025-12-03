# Program: Recursive Character Counter

print("===== CHARACTER COUNT (RECURSION) =====")

def count_char(text, ch, index=0):
    if index == len(text):     # reached end of string
        return 0
    if text[index] == ch:
        return 1 + count_char(text, ch, index + 1)
    else:
        return count_char(text, ch, index + 1)

string = input("Enter a string: ")
char = input("Character to count: ")

print(f"Occurrences of '{char}':", count_char(string, char))
