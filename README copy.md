# holbertonschool-AirBnB_clone

## description of the project

create a console program to emulate a native console that will interpret commands and interact with AirBnB site clone classes and methods
![Alt Text](https://camo.githubusercontent.com/75e4f7d5fb942b29453e3bdbc7b3753aeaae2ed6eae175cb3c97009f19b373df/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f636f6e63657074732f37342f68626e625f73746570322e706e67)

## Learning Objectives

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## description of the command interpreter:

allows the user to interact with the classes and methods of the AirBnB cloned site using commands in the form of lines of text.

## project architecture 

- console.py - command interpreter
- __init__.py - switch to file storage or database storage modes
- __init__ - initialize instance attributes
- __str__ - returns formatted string representation of instance
- user.py - class User
- tests - unit test files

file_storage.py - class FileStorage; serializes instances to JSON file and deserializes from a JSON file
- all : returns the dictionary __objects
- new : sets in __objects the obj with key <obj class name>.id
- save : serializes __objects to the JSON file (path: __file_path)
- reload : deserializes the JSON file to __objects

## how to start it

clone the repository. run the file console.py and this will initiate the interactive mode.
```
/AirBnB_clone$./console.py
```
output
```
(hbnb)
```

## how to use it

- quit

exit the console
- EOF

exit program on EOF signal
- help

displays information about the associated command
- empty line + ENTER

execute anything
- create

Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
- show

Prints the string representation of an instance based on the class name and id
- destroy

Deletes an instance based on the class name and id (save the change into the JSON file)
- all

Prints all string representation of all instances based or not on the class name
- update

Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)

## examples

## Reminder

- OS

OS module provides easy functions that allow us to interact and get Operating System information and even control processes.

- json

allows to work with JSON data

- .items()

The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

- .strptime()

creates a datetime object from the given string.

- setattr()

sets the value of the attribute of an object.

- str()

returns the string representation of a given object.

- f-Strings

“formatted string literals,” f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.

- self

self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python

- .strftime()

returns a string representing date and time using date, time or datetime object.

- {} dictionary 
- [] lists
- () tuple

- __x__

- x__

- __x

### What is an UUID

UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).

Advantages of UUID :
- Can be used as general utility to generate unique random id.
- Can be used in cryptography and hashing applications.
- Useful in generating random documents, addresses etc.

### How to manage datetime
https://www.programiz.com/python-programming/datetime

### What is *args and **kwargs and how to use it

*args :

**kwargs

## sources

- OS

https://www.digitalocean.com/community/tutorials/python-os-module

- json

https://www.w3schools.com/python/python_json.asp

- UUID

https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/
https://docs.python.org/3/library/uuid.html

- *args and **kwargs

https://www.freecodecamp.org/news/args-and-kwargs-in-python/

- .items()

https://www.w3schools.com/python/ref_dictionary_items.asp#:~:text=The%20items()%20method%20returns,the%20dictionary%2C%20see%20example%20below.

- .strptime()

https://www.programiz.com/python-programming/datetime/strptime

- setattr()

https://www.programiz.com/python-programming/methods/built-in/setattr

- str()

https://www.programiz.com/python-programming/methods/built-in/str

- f-Strings

https://realpython.com/python-f-strings/

- manipuling Text, JSON

https://www.geeksforgeeks.org/saving-text-json-and-csv-to-a-file-in-python/

- self

https://www.geeksforgeeks.org/self-in-python-class/#:~:text=self%20represents%20the%20instance%20of,to%20refer%20to%20instance%20attributes.

- .strftime()

https://www.programiz.com/python-programming/datetime/strftime

- super

https://www.stashofcode.fr/comment-marche-fonction-super-de-python/
https://he-arc.github.io/livre-python/super/index.html

- Types natifs

https://docs.python.org/fr/3/library/stdtypes.html

- unittest

https://gayerie.dev/docs/python/python3/unittest.html



ANDRIEUX Guenoel
MURYANGO Chris Monfort 
MISSUD Bastien
