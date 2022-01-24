![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x08. Python - More Classes and Objects
<div style="text-align: justify">

In this project, you should to learn and practice about `Object Oriented Programming` using `classes` and `objects` in Python. Learn how to use the `class methods`, and
`static methods`, differences between `class vs instance attributes`, and how to use the special `__str__` and `__repr__` methods.

Don't forget to fully meet the following development requirements.
	
# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents :clipboard:

* [Requirements](#requirements)
* [Tasks](#tasks-page_with_curl)
* [Credits](#credits)

	
## Requirements 

### Resources

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=programing+in+python&hl=es&ei=bUHBYY7XBrCNwbkP15C0qAk&oq=programing+in+py&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQhBdYjxxg4C1oAnACeACAAbUBiAGsApIBAzAuMpgBAKABAcgBCsABAQ&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=programing+python)

* [Object Oriented Programming](https://python.swaroopch.com/oop.html)((Read everything until the paragraph “Inheritance” (excluded))
* [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)((Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The `__init__` Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “`__str__`- and `__repr__`-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”))
* [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
* [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)(Mainly the last part “Public instead of Private Attributes”)
* [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)

	
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

	
## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.
		
## Tasks :page_with_curl:

* **0. Simple rectangle**
  	* [0-rectangle.py](./0-rectangle.py): Empty Python class that defines a rectangle.

* **1. Real definition of a rectangle**
  	* [1-rectangle.py](./1-rectangle.py): Python class that defines a rectangle. Builds on
  	[0-rectangle.py](./0-rectangle.py) with:
    		* Private instance attribute `width`.
    		* Property getter `def width(self):` to get `width`.
    		* Property setter `def width(self, value):` to set `width`.
    		* Private instance attribute `height`.
    		* Property getter `def height(self):` to get `height`.
    		* Property setter `def height(self, value):` to set `height`.
    		* Instantiation with optional `width` and `height`: `def __init(self,
    		width=0, height=0):`
  		* If either of `width` or `height` is not an integer, a `TypeError` is
  		raised with the message `width must be an integer` or `height must be an integer`.
  		* If either of `width` or `height` is less than `0`, a `ValueError` is
  		raised with the message `width must be >= 0` or `height must be >= 0`.

* **2. Area and Perimeter**
  	* [2-rectangle.py](./2-rectangle.py): Python class that defines a rectangle. Builds on
  	[1-rectangle.py](./1-rectangle.py) with:
    		* Public instance method `def area(self):` that returns the area of
    		the rectangle.
    		* Public instance attribute `def perimeter(self):` that returns the
    		permiter of the rectangle (if either of `width` or `height` equals `0`, the
    		perimeter is `0`).

* **3. String representation**
  	* [3-rectangle.py](./3-rectangle.py): Python class that defines a rectangle. Builds on
  	[2-rectangle.py](./2-rectangle.py) with:
    		* Special method `__str__` to print the rectangle with the `#` character
    		(if either of `width` or `height` equals `0`, the method returns an empty
    		string.).

* **4. Eval is magic**
  	* [4-rectangle.py](./4-rectangle.py): Python class that defines a rectangle. Builds on
  	[3-rectangle.py](./3-rectangle.py) with:
    		* Special method `__repr__` to return a string representation of the
    		rectangle.

* **5. Detect instance deletion**
  	* [5-rectangle.py](./5-rectangle.py): Python class that defines a rectangle. Builds on
  	[4-rectangle.py](./4-rectangle.py) with:
    		* Special method `__del__` that prints the message `Bye rectangle...`
    		when a `Rectangle` is deleted.

* **6. How many instances**
  	* [6-rectangle.py](./6-rectangle.py): Python class that defines a rectangle. Builds on
  	[5-rectangle.py](./5-rectangle.py) with:
    		* Public class attribute `number_of_instances` that is initialized to `0`,
    		incremented for each new instantiation, and decremened for each instance deletion.

* **7. Change representation**
  	* [7-rectangle.py](./7-rectangle.py): Python class that defines a rectangle. Builds on
  	[6-rectangle.py](./6-rectangle.py) with:
    		* Public class attribute `class_symbol` that is initialized to `#` but can
    		be any type - used as the symbol for string representation.

* **8. Compare rectangles**
  	* [8-rectangle.py](./8-rectangle.py): Python class that defines a rectangle. Builds on
  	[7-rectangle.py](./7-rectangle.py) with:
    		* Static method `def bigger_or_equal(rect_1, rect_2):` that returns the
    		rectangle with the greater area (returns `rect_1` if both areas are equal).
    		* If either of `rect_1` or `rect_2` is not a `Rectangle` instance, a
    		`TypeError` is raised with the message `rect_1 must be an instance of
    		Rectangle` or `rect_2 must be an instance of Rectangle`.

* **9. A square is a rectangle**
  	* [9-rectangle.py](./9-rectangle.py): Python class that defines a rectangle. Builds on
  	[8-rectangle.py](./8-rectangle.py) with:
    		* Class method `def square(cls, size=0):` that returns a new `Rectangle`
    		instance with `width == height == size`.

		
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
