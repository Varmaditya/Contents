#Program: Count word frequency (case-insensitive)

print("===== WORD FREQUENCY COUNTER =====")

# Given sentence and target word
sentence = "Python is great and learning Python makes programming easier"
word = "python"

count = 0  # counter

# Convert to lowercase and split into words
for w in sentence.lower().split():
    if w == word:
        count += 1

print(f"'{word}' appears", count, "times")
