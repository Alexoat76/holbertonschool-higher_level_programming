![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x06. Python - Classes and Objects.
<div style="text-align: justify">

In this project, you should to learn and practice about `Object Oriented Programming` using `classes` and `objects` in Python. Learn how to use the `methods`, and
`properties` as well as data `abstraction`, data `encapsulation`, and `information hiding`.

Don't forget to fully meet the following development requirements.
	
# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents :clipboard:

* [Requirements](#requirements)
* [Tasks](#tasks)
* [Credits](#credits)

	
## Requirements 

### Resources

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=programing+in+python&hl=es&ei=bUHBYY7XBrCNwbkP15C0qAk&oq=programing+in+py&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQhBdYjxxg4C1oAnACeACAAbUBiAGsApIBAzAuMpgBAKABAcgBCsABAQ&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=programing+python)

* [Object Oriented Programming](https://python.swaroopch.com/oop.html)(Read everything until the paragraph `“Inheritance”` excluded. You do `NOT have` to learn about class attributes, `classmethod` and `staticmethod` yet)
* [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please **be careful**: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes `(You DON’T have to learn about class attributes)`, Methods, The `__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)	
* [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
* [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## General :page_with_curl:
<div style="text-align: justify">
	
### Python Scripts: :pushpin:
		
* Allowed editors: `vi`, `vim`, `emacs`. </div>
<div style="text-align: justify">

* All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3`.
* All your files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/python3`.
* A `README.md` file, at the root of the folder of the project, is mandatory.
* Your code should use the pycodestyle (version 2.7).
* All your files must be executable.
* The length of your files will be tested using `wc`.
* All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
* All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
* All your functions `(inside and outside a class)` should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c` `'print(__import__("my_module").MyClass.my_function.__doc__)')`

	
## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.
		
## Tasks :page_with_curl:

* **0. My first square**
  	* [0-square.py](./0-square.py): Python class `Square` that defines a square.

* **1. Square with size**
  * [1-square.py](./1-square.py): Python class `Square` that defines a square. Builds on
  [0-square.py](./0-square.py) with:
    * Private instance attribute `size`.
    * Instantiation with `size`.

* **2. Size validation**
  * [2-square.py](./2-square.py): Python class `Square` that defines a square. Builds on
  [1-square.py](./1-square.py) with:
    * Instantiation with optional `size`: `def __init__(self, size=0):`
  * If a provided `size` attribute is not an integer, a `TypeError` exception
  is raised with the message `must be an integer`.
  * If a provided `size` attribute is less than `0`, a `ValueError` exception
  is raised with the message `size must be >= 0`.

* **3. Area of a square**
  * [3-square.py](./3-square.py): Python class `Square` that defines a square. Builds on
  [2-square.py](./2-square.py) with:
    * Public instance attribute `def area(self):` that returns the current
    square area.

* **4. Access and update private attribute**
  * [4-square.py](./4-square.py): Python class `Square` that defines a square. Builds on
  [3-square.py](./3-square.py) with:
    * Property `def size(self):` to retrieve the private instance
    attribute `self`.
    * Property setter `def size(self, value):` to set `self`.

* **5. Printing a square**
  * [5-square.py](./5-square.py): Python class `Square` that defines a square. Builds on
  [4-square.py](./4-square.py) with:
    * Public instance method `def my_print(self):` that prints the square
    with the character `#` to standard output (if `size` == 0 -> prints an empty
    line).

* **6. Coordinates of a square**
  * [6-square.py](./6-square.py): Python class `Square` that defines a square. Builds on
  [5-square.py](./5-square.py) with:
    * Private instance attribute `position`.
    * Property `def position(self):` to retreive `position`.
    * Property setter `def position(self, value):` to set `position`.
    * Instantiation with optional `size` and `position`:
    `def __init__(self, size=0, position=(0, 0)):`
  * If a provided `position` attribute is not a tuple of two integers, a
  `TypeError` exception is raised with the message `position must be a tuple of
  2 positive integers`.

		
## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Alex Orland Arévalo Tribaldos`**  and credits for `group projects` are displayed in the respective `README.md` files.

<3915@holbertonschool.com>
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Alexoat76)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/aoarevalot)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/Alexoat76/)


## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).
