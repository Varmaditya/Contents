# Control Flow in Python - JUMP STATEMENTS (break, continue, pass)

# ---------------- Introduction ----------------
print("\n===== JUMP STATEMENTS IN PYTHON =====")
print("""
Jump statements alter the normal flow of loops.
They allow you to:
  • stop a loop immediately (break)
  • skip the current iteration and move to the next (continue)
  • place a placeholder where code will be added later (pass)

We will demonstrate each one with clear examples using both 'for' and 'while' loops.
""")

# ---------------- Types of Jump Statements ----------------
print("Types of Jump Statements:")
print("1. break    → Exit the loop immediately")
print("2. continue → Skip the rest of the current iteration and continue with the next")
print("3. pass     → Do nothing (placeholder)")

# ---------------- Example 1: break in a for loop ----------------
print("\n---- Example 1: break in a for loop ----")
print("Find the first multiple of 7 between 1 and 50 and stop when found:")
found = False
for num in range(1, 51):
    if num % 7 == 0:
        print("First multiple of 7 found:", num)
        found = True
        break   # stops the loop immediately
# After break, loop ends and execution continues here
if not found:
    print("No multiple of 7 found in the range.")
print("Loop finished using break.\n")

# ---------------- Example 2: break in a while loop ----------------
print("---- Example 2: break in a while loop ----")
print("Ask the user repeatedly for a secret word; stop when correct word entered.")
secret = "open_sesame"
attempt = ""
while True:
    attempt = input("Enter secret word (type 'quit' to give up): ")
    if attempt == "quit":
        print("User chose to quit.")
        break
    if attempt == secret:
        print("Correct! Access granted.")
        break
    print("Wrong word. Try again.")
print("Exited the while loop after break.\n")

# ---------------- Example 3: continue in a for loop ----------------
print("---- Example 3: continue in a for loop ----")
print("Print numbers 1 to 10 but skip multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        # skip this iteration (do not run the print below for this i)
        continue
    print(i, end=" ")
print("\nCompleted for loop with continue.\n")

# ---------------- Example 4: continue in a while loop ----------------
print("---- Example 4: continue in a while loop ----")
print("Read numbers and display only positive numbers; stop when user enters 0.")
while True:
    val = float(input("Enter a number (0 to stop): "))
    if val == 0:
        print("Stopping input loop.")
        break
    if val < 0:
        # negative number: skip printing and go to next iteration
        print("Negative number entered — skipping display.")
        continue
    print("Positive number:", val)
print("While loop with continue finished.\n")

# ---------------- Example 5: pass as placeholder ----------------
print("---- Example 5: pass as a placeholder ----")
print("Using pass in an if statement and inside a loop:")
for ch in "Py":
    if ch == "y":
        # placeholder: we plan to add code here later
        pass
    print("Character:", ch)
print("pass did nothing but kept the code syntactically correct.\n")

# ---------------- Example 6: Practical example combining break & continue ----------------
print("---- Example 6: Small practical scanner ----")
print("User enters words; show only words longer than 3 letters; stop if 'stop' entered:")
while True:
    w = input("Enter word: ")
    if w == "stop":
        print("Stopping scanner.")
        break               # finish scanning entirely
    if len(w) <= 3:
        # skip short words
        print("Word too short — skipped.")
        continue
    print("Accepted word:", w)  # only runs for words length > 3
print("Practical scanner ended.\n")

# ---------------- Important Notes ----------------
print("===== IMPORTANT NOTES =====")
print("""
• break:
    - Immediately exits the innermost loop (for or while).
    - If used inside nested loops, only the current loop is exited.

• continue:
    - Skips the rest of the current loop iteration and continues with the next iteration.
    - Useful for ignoring certain cases while keeping the loop running.

• pass:
    - Does nothing. It's a no-op (placeholder).
    - Helpful when a statement is syntactically required but you have nothing to do yet.

• Use jump statements carefully:
    - Overuse can make code harder to read.
    - Prefer clear logic; use break/continue for simple, readable control flow.
""")

# ---------------- Summary ----------------
print("\n===== SUMMARY =====")
print("jump statements (break, continue, pass) let you control loop execution precisely.")
print("Practice these examples interactively to see how flow changes with each statement.")
