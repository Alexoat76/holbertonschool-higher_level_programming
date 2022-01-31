![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x07. Python - Test-driven development
<div style="text-align: justify">

In this project, you should to learn and practice about the `doctest` module and unit testing. The goal is to create unit tests before creating the actual program itself.

Don't forget to fully meet the following development requirements.
	
# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents :clipboard:

* [Requirements](#requirements)
* [Files](#files-heavy_check_mark)
* [Tasks](#tasks-page_with_curl)
* [Credits](#credits)

	
## Requirements 

### Resources

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=programing+in+python&hl=es&ei=bUHBYY7XBrCNwbkP15C0qAk&oq=programing+in+py&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQhBdYjxxg4C1oAnACeACAAbUBiAGsApIBAzAuMpgBAKABAcgBCsABAQ&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=programing+python)

* [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)(until “26.2.3.7. Warnings” included)
* [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
* [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

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
	
### Python Test Cases: :pushpin:

* Allowed editors: `vi`, `vim`, `emacs`. </div>
<div style="text-align: justify">

* All your files should end with a new line.
* All your test files should be inside a folder `tests`
* All your test files should be text files (extension: `.txt`)
* All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
* All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
* All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
* All your functions should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)')`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method
	<div style="text-align: justify">
	(the length of it will be verified)

	
## Files :heavy_check_mark:

* [main_files](./main_files): Folder of main files. Provided by Holberton School.
		
| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `6-max_integer_test.py`  | `def max_integer(list=[]):`		  |
		
## Tasks :page_with_curl:

* **0. Integers addition**
  	* [0-add_integer.py](./0-add_integer.py): Python function that returns the integer addition
 	 of two numbers.
 		* If either of `a` or `b` is not an `int` or `float`, a `TypeError` is raised
  		with the message `a must be an integer` or `b must be an integer`.
  		* If either of `a` or `b` is a `float`, it is casted to an `int`
  		before addition.

* **1. Divide a matrix**
  	* [2-matrix_divided.py](./2-matrix_divided.py): Python function that divides all
  	elements of a matrix by a common divisor.
  		* Returns a new matrix representing the division of all elements of `matrix`
  		by `div`.
  		* Quotients are rounded to two decimal places.
  		* If `matrix` is not a list of lists of `int`s or `float`s, a `TypeError`
  		is raised with the message `matrix must be a matrix (list of lists) of
  		integers/floats`.
  		* If `matrix` contains rows of different lengths, a `TypeError` is raised
  		with the message `Each row of the matrix must have the same size`.
  		* If the divisor `div` is not an `int` or `float`, a `TypeError` is raised
 		with the message `div must be a number`.
  		* If `div` is `0`, a `ZeroDivisionError` is raised with the message
  		`division by zero`.

* **2. Say my name**
  	* [3-say_my_name.py](./3-say_my_name.py): Python function that prints a name in
  	the format `My name is <first_name> <last_name>`.
  		* If either of `first_name` or `last_name` is not a `str`, a `TypeError` is
  		raised with the message `first_name must be a string` or `last_name must be a
  		string`.

* **3. Print square**
  	* [4-print_square.py](./4-print_square.py): Python function that prints a square using
  	the `#` character.
  		* The paramter `size` represents the height/width of the square.
  		* If `size` is not an `int`, a `TypeError` is raised  with the message,
  		`size must be an integer`.
  		* If `size` is less than `0`, a `ValueError` is raised with the message `size
  		must be >= 0`.

* **4. Text indentation**
  	* [5-text_indentation.py](./5-text_indentation.py): Python function that prints text with
  	indentation.
  		* Two new lines are printed after any `.`, `?`, or `:` character.
  		* If `text` is not a `str`, a `TypeError` is raised with the message `text
  		must be a string`.
  		* No spaces are printed at the beginning or end of each printed line.

* **5. Max integer - Unittest**
  	* [tests/6-max_integer_test.py](https://github.com/Alexoat76/holbertonschool-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/6-max_integer_test.py): Python class/script
  	that runs unittests for the function `def max_integer(list=[]):`
  	(provided by Holberton School).
		
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
