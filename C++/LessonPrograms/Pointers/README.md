Pointers in C++

Until now, we have worked with variables that store values directly.

For example:

int age = 23;

Here, the variable "age" stores the value "23".

However, every variable is stored somewhere in the computer's memory. Along with storing values, C++ also allows us to work with the memory addresses where those values are stored. This is where pointers come into the picture.

Pointers are one of the most powerful features of C++. They provide direct access to memory and form the foundation for advanced topics such as dynamic memory allocation, data structures, file handling, and object-oriented programming.

Although pointers may seem difficult at first, understanding the basic concepts of addresses and memory makes them much easier to learn.

---

What is a Pointer?

A pointer is a special variable that stores the memory address of another variable.

Unlike normal variables that store actual values, pointers store locations.

For example:

int age = 23;

Suppose the variable "age" is stored at memory address "1000".

A pointer can store this address:

int *ptr = &age;

Now:

age = 23
ptr = 1000

Here:

- "age" stores the value.
- "ptr" stores the address of "age".

---

Why Do We Need Pointers?

Pointers allow programs to:

- Access memory directly
- Share data efficiently between functions
- Work closely with arrays and strings
- Create dynamic memory during program execution
- Build advanced data structures such as linked lists, stacks, queues, and trees

Pointers give programmers greater control over how data is stored and accessed in memory.

---

Memory and Addresses

Every variable occupies a location in memory.

Example:

int num = 50;

Memory representation:

Address      Value
1000         50

The computer keeps track of both:

- The value stored in the variable
- The memory address where the value is stored

Normally we work only with values, but pointers allow us to work directly with addresses.

---

Address Operator (&)

The address operator "&" is used to obtain the memory address of a variable.

Syntax

&variableName

Example

int num = 50;

cout << &num;

Output:

1000

(The actual address will vary on every computer.)

The "&" operator answers the question:

"Where is this variable stored in memory?"

---

Pointer Declaration

Before using a pointer, it must be declared.

Syntax

dataType *pointerName;

Example

int *ptr;

This creates a pointer capable of storing the address of an integer variable.

Assigning an Address to a Pointer

int num = 50;

int *ptr = &num;

Now the pointer stores the address of "num".

---

Dereferencing Operator (*)

The "*" operator is also used to access the value stored at a memory address.

This process is called dereferencing.

Syntax

*pointerName

Example

int num = 50;

int *ptr = &num;

cout << *ptr;

Output:

50

Here:

- "ptr" contains the address of "num"
- "*ptr" accesses the value stored at that address

You can think of dereferencing as:

"Go to the address stored in the pointer and retrieve the value found there."

---

Pointers and Arrays

Pointers and arrays are closely related in C++.

The name of an array itself represents the address of its first element.

Example:

int numbers[5] = {10, 20, 30, 40, 50};

Memory representation:

numbers[0] = 10
numbers[1] = 20
numbers[2] = 30
numbers[3] = 40
numbers[4] = 50

The array name:

numbers

contains the address of:

numbers[0]

Example

cout << numbers;

Displays the address of the first element.

Accessing the First Element

cout << *numbers;

Output:

10

Because:

numbers  → address of first element
*numbers → value of first element

This relationship between arrays and pointers is one of the most important concepts in C++.

---

Notes to Remember

1. A Pointer Stores an Address

Normal variables store values, while pointers store memory locations.

2. The Address Operator (&) Gives the Address

&num

returns the memory address of "num".

3. The Dereferencing Operator (*) Gives the Value

*ptr

returns the value stored at the address.

4. Pointer Type Must Match Variable Type

int *ptr;

stores addresses of integer variables.

5. Array Name Represents an Address

arr

represents the address of the first element of the array.

6. Pointers Work Directly with Memory

This makes them powerful but also requires careful usage.

---

Closing Thought

Pointers introduce a new way of thinking about programs. Until now, we focused on values. With pointers, we begin thinking about where those values live in memory. Understanding the address operator ("&"), dereferencing operator ("*"), and the relationship between pointers and arrays provides a strong foundation for many advanced C++ concepts that follow.