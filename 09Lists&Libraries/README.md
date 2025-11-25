## a demo in C
- compiled languages!

## Intro to Python
- High-level = human-readable!
- General but!
	- [Modules and libraries can make it more specific](https://wiki.python.org/moin/UsefulModules)
		- Modules: simple .py file that "abstracts out" specific information (functions, variables, other things)
		- libraries (or packages) are a collection of modules
- Interpreted (executed by the interpreter vs. compiled)
  - Easier to debug
  - Runs a little slower
- Scripts are a sequence of definitions and commands executed in the shell
- #nocommentcomment
- Object-oriented

## Object-oriented programming
- Some languages can do it, some languages must do it, e.g. javaScript *can* do it, Python *must* do it
- Almost everything in Python is an object
- **Encapsulation/aggregation**
- object: independent part of the program that manages itself (own rules and ways of doing things); a representation of something that you can control and send messages to
- **Inheritance**
- objects get their functions/methods from classes
- class: template, blueprint for creating objects, specific instances
- superclass is parent, class is child
- class inherits attributes of parent (through abstraction) but modifies, evolves
- classes are reusable
- **Polymorphism**
- produce different results when applied to different objects, e.g. file a paper, file metal

## XCODE

- 
```
xcode-select --install
```

## HomeBrew

- 
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- 
```
/opt/homebrew/bin/brew shellenv
```

## Where is your python3?
	- `which python3`
	- COPY THIS FILE PATH

**CHECK PYTHON BUNDLE IN TEXTMATE**
- TextMate>Settings>Variables
- add the file path you copied from 'which python3', something like:
`TM_PYTHON` and `/opt/homebrew/bin/python3`


## Integrated Development Environments (IDE)
- Most commonly used for interpreted languages
- Interpreter helps you debug within the IDE

**Running Python: world.py**
  - CLI  
  - IDE

## CODE ALONG
```Python
print(type(10)) #integer
print(type(10.)) #float
print(type("hello,world")) #string
print(type(True)) #boolean
```
 
- Python Function Definition + Call
  - definition has to come before call, but call happens where call happens
  
```
# function
def circle_area(x):
  return x * x * 3.14
# call
print(circle_area(3.0))

``` 
 
# Lists
## Lists vs Arrays
- Both are collections of related data in a specific order

**Arrays**
- All the data have to be the same type
- Can handle arithmetic
- They need a module

**Lists**
- Related data can be of different type
- Can't handle arithmetic
- Don't need a module

## Intro to Lists in Python
- Use a ` [ ] ` bracket to enclose
- Lists are ordered, but again, can have different types
- Each item in a list is called an *element*
- Each element is accessed by its numerical index
- The first index starts at 0.

![listanatomy](listanatomy.png)

### Accessing & Amending List Elements
- Reference an element by its index number

```Python

instruments = ['Drum', 'Guitar', 'Bass']

print(instruments[0]) # Drum
print(instruments[1]) # Guitar
print(instruments[2]) # Bass
```

- List Repetition

```python
# Repeat 0 five times. The result is a single list
numbers = [0] * 5
print(numbers) 

# Repeat 1, 2, 3 three times.
numbers = [0, 1, 2] * 3
print(numbers)
```

- List mechanics with an update

```python
old_instruments = ['Drum', 'Guitar', 'Bass']
new_instruments = old_instruments

# Both print out ['Drum', 'Guitar', 'Bass']
print(old_instruments)
print(new_instruments)

new_instruments[0] = 'Percussion'

# Both print out ['Percussion', 'Guitar', 'Bass']
print(old_instruments)
print(new_instruments)
```

- List slicing

```python
menu = ['Drum', 'Guitar', 'Bass']
# Slice indices 1 and 2
print(menu[1:3]) # ['Guitar', 'Bass']
# Slice from index 1 to the end
print(menu[1:]) # ['Guitar', 'Bass']
# Slice index 1
print(menu[1:2]) # ['Guitar']
# Slice nothing
print(menu[1:1]) # []

```

- List manipulation

```python
menu = ['Drum', 'Guitar', 'Bass']
print(menu)
# Append new element to the list
menu.append('Piccolo')
print(menu)
# Insert a new element into the list
# 2 is an index where we insert the new element
menu.insert(2, 'pie')
print(menu)
# Remove an element from the list
menu.remove('Bass')
print(menu)
# Get the length of list
print('The length of list is:', len(menu))
```

### Lists & Loops
- You can use a for loop to iterate through a list
- This is called *list traversal*

```Python
instruments = ['Drum', 'Guitar', 'Bass']

for instrument in instruments:
	print(instrument)
```
- You can also use a counter to iterate through a list with its index value
	- but it has to be data of the same type
```Python

=
```

## Exersize
- Write a program that converts 99 Fahrenheit to Celsius
- Create two variables, **f** and **c**
- Use the equation:
	- Celsius = (Fahrenheit - 32)  5 / 9

## Modules
- Hierarchy: built-ins; packages; writing your own packages
- Extend the capabilities of your program
- Use the keyword *import* to implement
- Access variables and functions in the module using the **.** operator
- Then rename the module, if you like, with the 'as' keyword
```Python
# standard import
import math
print(math.sqrt(16))

# alias
import math as m
print(m.sqrt(16))

# selective import
from math import sqrt
print(sqrt(16))

# selective import with alias
from math import sqrt as square_root
print(square_root(16))
```

### Help!
- See what's inside the module with the help function
- Press *q* to exit
```Python
help('random')
help('random.random')
```

## Writing Text Files in Python
- They're writing to somewhere where the file you're using is
```Python
file = open("LoremIpsum.txt", "w")
file.write(
"Lorem ipsum dolor sit amet "
"consectetur adipiscing elit, sed do "
"eiusmod tempor incididunt ut labore "
"et dolore magna aliqua."
)
file.close()
```
## Reading Text Files in Python
```Python
file = open("LoremIpsum.txt", "r")
print(file.read())
file.close()
```
## Writing CSV Files in Python
```Python
import csv
csv_file = open("People.csv", "w")
# Create a csv writer
csv_writer = csv.writer(csv_file)
# Write the first row (header)
csv_writer.writerow(["Name", "Street", "Number"])
# Add people
csv_writer.writerow(["James", "1st Street", 98])
csv_writer.writerow(["Mary", "10th Street", 271])
csv_file.close()
```
### Reading CSV Files in Python
```Python
import csv
csv_file = open("People.csv", "r")
# Create a csv writer
csv_reader = csv.reader(csv_file)
# Read and print each data row one by one
for row in csv_reader:
  print(row)
csv_file.close()
```
