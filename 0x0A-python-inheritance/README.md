<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>

</p>

---

# 0x0A. Python - Inheritance
<div style="text-align: justify">

In this project, you should to learn and practice about Python class `inheritance` and recognize the differences 
	between **`super-`** and **`sub-classes`**.

<p align="center">
  <img width="600"  
        src="https://tudip.com/wp-content/uploads/2019/09/Blog-Header-Inheritance-in-Python-1900x600-1900x600.jpg"
  >
</p>
		
# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents
* [About](#about)
* [Resources](#resources-books)
* [Requirements](#requirements)
* [Files](#files-file_folder)
* [Tasks](#tasks)
* [Credits](#credits)

## About

This project, holds some tasks about how to use super- and sub-classes, practicing inheritance, definining classes with multiple base classes, and overiding inherited methods and attributes.

## Resources :books:
Read or watch:

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=programing+in+python&hl=es&ei=bUHBYY7XBrCNwbkP15C0qAk&oq=programing+in+py&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQhBdYjxxg4C1oAnACeACAAbUBiAGsApIBAzAuMpgBAKABAcgBCsABAQ&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=programing+python)

* [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
* [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://hub.packtpub.com/inheritance-python/)
* [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## Requirements
### General
	
### Python Scripts: :pushpin:
		
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3`.
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` (version 2.7).
- All files must be executable.
- The length of your files will be tested using `wc`.
	
### Python Test Cases: :pushpin:

- Allowed editors: `vi`, `vim`, `emacs`.
- All files should end with a new line.
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'`
	and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method
	(the length of it will be verified)

## More Info
	
### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-higher_level_programming.git`	
- Access to directory: `cd 0x0A-python-inheritance`
- `Compile` accord to `instructions` of each task.
	
## Files :file_folder:
	
Prototypes and functions for this project:
	
| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `1-my_list.py`          | `def print_sorted(self):`             |		
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |

## Test :heavy_check_mark:		
		
* [tests](./tests): Folder of main files. Provided by Holberton School.	
	
## Tasks

+ [x] 0\. **Lookup**
	
+ **[0-lookup.py](./0-lookup.py)** 
	
* Python function that returns a list of available attributes and methods of an objects.
	
---

+ [x] 1\. **My list**

+ **[1-my_list.py](./1-my_list.py)**
	* Python class `MyList` that inherits from `list`
	
	Includes:
    	
	* Public instance method `def print_sorted(self):` that prints the list in
    		ascending sorted order (assumes all list elements are `int`s).

---
	
+ [x] 2\. **Exact same object**
	
+ **[2-is_same_class.py](./2-is_same_class.py)**
	
	* Python function that returns `True` if an object is
  	exactly an instance of a specified class; otherwise `False`.
	
---

+ [x] 3\. **Same class or inherit from**
 
+ **[3-is_kind_of_class.py](./3-is_kind_of_class.py)**
	
	* Python function that returns `True` if an object is
  	an instance or inherited instance of a specified class; otherwise `False`.

---	
	
+ [x] 4\. **Only sub class of**
  	
+ **[4-inherits_from.py](./4-inherits_from.py)**
	
	* Python function that returns `True` if an object is
  	an inherited instance (either directly or indirectly) from a specified class;
  	otherwise `False`.

---
	
+ [x] 5\. **Geometry module**
  	
+ **[5-base_geometry.py](./5-base_geometry.py)**
	
	* An empty Python class `BaseGeometry`.

---	
	
+ [x] 6\. **Improve Geometry**
  	
+ **[6-base_geometry.py](./6-base_geometry.py)** 
	* Python class `BaseGeometry`. Builds on
  	[5-base_geometry.py](./5-base_geometry.py) with:
    		
		* Public instance method `def area(self):` that raises an `Exception` with
    		the message `area() is not implemented`.

---	
	
+ [x] 7\. **Integer validator**
	
+ **[7-base_geometry.py](./7-base_geometry.py)** 
	* Python class `BaseGeometry`. Builds on
  	[6-base_geometry.py](./6-base_geometry.py) with:
    		
		* Public instance method `def integer_validator(self, name, value):` that
    		validates the parameter `value`.
    		- Assumes the parameter `name` is always a string.
    		- The parameter `value` must be an `int`, otherwise, a `TypeError` exception
    		is raised with the message `<name> must be an integer`.
    		- The parameter `value` must be greater than `0`, otherwise, a
    		`ValueError` exception is raised with the message `<value> must be greater
    		than 0`.
	
---

+ [x] 8\. **Rectangle**
	
+ **[8-rectangle.py](./8-rectangle.py)** 
	* Python class `Rectangle` that inherits from `BaseGeometry`
  	([7-base_geometry.py](./7-base_geometry.py)). 
	
	- Includes:
    	- Private attributes `width` and `height` , validated with `integer_validator`.
    	- Instantiation with `width` and `height`: `def __init__(self, width, height):`

---	
	
+ [x] 9\. **Full rectangle**

+ **[9-rectangle.py](./9-rectangle.py)** 
	* Python class `Rectangle` that inherits from `BaseGeometry`
  	([7-base_geometry.py](./7-base_geometry.py)). 
	
	Builds on [8-rectangle.py](./8-rectangle.py) with:
	
    * Implementation of the method `area()`.
    * Special method `__str__` to print `Rectangle`s in the format `[Rectangle]
    		<width>/<height>`.
---
			
+ [x] 10\. **Square #1**
			
+ **[10-square.py](./10-square.py)** 
	* Python class `Square` that inherits from `Rectangle`
  	([9-rectangle.py](./9-rectangle.py)). 
			
	Includes:
			
    * Private attribute `size` - validated with `integer_validator`.
    * Instantiation with `size`: `def __init__(self, size):`.
    * Implementation of the `area()` method.

---		
			
+ [x] 11\. **Square #2**
+ **[11-square.py](./11-square.py)**
	* Python class `Square` that inherits from `Rectangle`
  	([9-rectangle.py](./9-rectangle.py)). 
			
Builds on [10-square.py](./10-square.py) with:
	
* Special method `__str__` to print squares in the format `[Square]
    		<width>/<height>`.
			
---

+ [x] 12\. **My integer**			
+ **[100-my_int.py](./100-my_int.py)** 
	* Python class `MyInt` that inherits from `int`.
			
	Includes:
    * Inversion of the `==` and `!=` operators.

---

+ [x] 13\. **Can I?**
+ **[101-add_attribute.py](./101-add_attribute.py)** 
	* Python function that adds a new attribute to an object if possible.
    * If an attribute cannot be added, a `TypeError` exception is raised with the message `can't add new attribute`.			
						
---
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
![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)
