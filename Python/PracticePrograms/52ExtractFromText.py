# Program: Extract Hashtags

text = input("Enter caption: ")
words = text.split()

hashtags = [w for w in words if w.startswith("#")]
print("Hashtags:", hashtags)
