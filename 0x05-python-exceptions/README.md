![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x05. Python - Exceptions.
<div style="text-align: justify">

In this project, you should to learn the difference between errors and exceptions, and how to use the exceptions in Python language with `try`
and `except`.

Don't forget to fully meet the following development requirements.
	
# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents :clipboard:

* [Requirements](#requirements)
* [Files](#files-floppy_disk)
* [Credits](#credits)

	
## Requirements 

### Resources

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=programing+in+python&hl=es&ei=bUHBYY7XBrCNwbkP15C0qAk&oq=programing+in+py&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQhBdYjxxg4C1oAnACeACAAbUBiAGsApIBAzAuMpgBAKABAcgBCsABAQ&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=programing+python)

* [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)
	

## General :page_with_curl:
<div style="text-align: justify">
	
### Python Scripts: :pushpin:
		
* Allowed editors: `vi`, `vim`, `emacs`. </div>
<div style="text-align: justify">

* All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3`.
* All your files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/python3`.
* A `README.md` file at the root of the repo, containing a description of the repository.
* Your code should use the pycodestyle (version 2.7).
* All your files must be executable.
* The length of your files will be tested using `wc`.

	
## Files :floppy_disk:

Prototypes for functions written in this project:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |
| `100-safe_print_integer_err.py`  | `def safe_print_integer_err(value):`                    |
	
## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.
		
## Tasks :page_with_curl:

* **0. Safe list printing**
  	* [0-safe_print_list.py](./0-safe_print_list.py): Python function that prints `x` elements
  	of a list on the same line, followed by a new line.
  		* The parameter `x` represents the number of elements to print - can be
  		bigger than the length of `my_list`.
  		* Returns the real number of elements printed.
  		* Without importing modules or using `len()`.

* **1. Safe printing of an integers list**
  	* [1-safe_print_integer.py](./1-safe_print_integer.py): Python function that prints an integer in `"{:d}".format()` format.
  		* The parameter `value` can be any type.
  		* Returns `True` if `value` was printed correctly (ie. was an integer),
  		`False` otherwise.
  		* Without importing modules or using `type()`.

* **2. Print and count integers**
  	* [2-safe_print_list_integers.py](./2-safe_print_list_integers.py): Python function that prints the first `x` elements of a list that are integers on the same line, 		followed by a new line.
  		* The parameter `my_list` can contain any type.
 		* The parameter `x` represents the number of elements to print - can be
  		bigger than the length of `my_list`.
  		* Reutnrs the real number of integers printed.
  		* Without importing modules or using `len()`.

* **3. Integers division with debug**
  	* [3-safe_print_division.py](./3-safe_print_division.py): Python function that divides two integers and prints the result using `finally:`.
  		* The function assumes that the arguments are integers.
  		* Upon success, returns the value of the division; otherwise - returns `None`.
  		* Without importing modules.

* **4. Divide a list**
  	* [4-list_division.py](./4-list_division.py): Python function that divides two lists element by element.
  		* Returns a new list of length `list_length` with all divisions.
  		* The lists `my_list_1` and `my_list_2` can contain any type.
  		* The parameter `list_length` can be larger than the lengths of either list.
  		* If an element is not an integer or float, the function prints `wrong type`.
  		* If the division cannot be done, the result of the division is `0` and the
  		function prints: `division by 0`.
  		* If either of `my_list_1` or `my_list_2` are too short, the function prints:
  		`out of range`.
  		* Without importing modules.

* **5. Raise exception**
  	* [5-raise_exception.py](./5-raise_exception.py): Python function that raises
  	a type exception.
  		* Without importing modules.

* **6. Raise a message**
  	* [6-raise_exception_msg.py](./6-raise_exception_msg.py): Python function that raises a
  	name exception with a message.
  		* Without importing modules.

* **7. Safe integer print with error message**
  	* [100-safe_print_integer_err.py](./100-safe_print_integer_err.py): Python function that
  	prints an integer with type-checking in `"{:d}".format())` format.
  		* The paramter `value` can be any type.
  		* Returns `True` if `value` was printed correctly (ie. was an integer).
  		* Otherwise, prints an exception error to `stderr` and returns `False`.
  		* Without importing modules.	
		
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
