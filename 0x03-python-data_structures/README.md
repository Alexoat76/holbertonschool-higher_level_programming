![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x03. Python - Data Structures: Lists, Tuples
<div style="text-align: justify">

In this project, you should to learn and practice the concepts about of Data Structures (Lists and Tuples) in python language.
Don't forget to fully meet the following development requirements.
	
# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents :clipboard:

* [Requirements](#requirements)
* [Files](#files)
* [Credits](#credits)

	
## Requirements 

### Resources

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=programing+in+python&hl=es&ei=bUHBYY7XBrCNwbkP15C0qAk&oq=programing+in+py&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQhBdYjxxg4C1oAnACeACAAbUBiAGsApIBAzAuMpgBAKABAcgBCsABAQ&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=programing+python)

* [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
* [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (until `5.3. Tuples and Sequences` included)
* [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)
	
## General :page_with_curl:
<div style="text-align: justify">
	
### Python Scripts: :pushpin:
		
* Allowed editors: `vi`, `vim`, `emacs`. </div>
<div style="text-align: justify">

* All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3`.
* All your files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/python3`.
* A `README.md` file at the root of the repo, containing a description of the repository.
* A `README.md` file, at the root of the folder of this project, is mandatory.
* Your code should use the pycodestyle (version 2.7).
* All your files must be executable.
* The length of your files will be tested using `wc`.

### C Scripts: :pushpin:
		
* Allowed editors: `vi`, `vim`, `emacs`. </div>
<div style="text-align: justify">

* All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using using gcc, using the options.
	`-Wall -Werror -Wextra -pedantic -std=gnu89`. </div>
	* All your files should end with a new line.
	* Your code should use the `Betty`. 
	It will be checked using `betty-style.pl` and `betty-doc.pl`.</div>
	
		* Please visit the [Betty style](https://github.com/holbertonschool/Betty/wiki) for the full specifications of Betty coding and documentation styles.
		* You are not allowed to use global variables.
		* No more than 5 functions per file.
	<div style="text-align: justify">
		
	* In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples.
		
	* The prototypes of all your functions should be included in your header file called `lists.h`.
	* All your header files should be include guarded.
	
	
	
## Files

| File                               | Prototype                                      |
| ---------------------------------- | ---------------------------------------------- |
| `0-print_list_integer.py`          | `def print_list_integer(my_list=[]):`          |
| `1-element_at.py`                  | `def element_at(my_list, idx):`                |
| `2-replace_in_list.py`             | `def replace_in_list(my_list, idx, element):`  |
| `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):` |
| `4-new_in_list.py`                 | `def new_in_list(my_list, idx, element):`      |
| `5-no_c.py`                        | `def no_c(my_string):`                         |
| `6-print_matrix_integer.py`        | `def print_matrix_integer(matrix=[[]]):`       |
| `7-add_tuple.py`                   | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| `8-multiple_returns.py`            | `def multiple_returns(sentence):`              |
| `9-max_integer.py`                 | `def max_integer(my_list=[]):`                 |
| `10-divisible_by_2.py`             | `def divisible_by_2(my_list=[]):`              |
| `11-delete_at.py`                  | `def delete_at(my_list=[], idx=0):`            |
| `100-print_python_list_info.c`     | `void print_python_list_info(PyObject *p);`    |

## Tasks :page_with_curl:

* **0. Print a list of integers**
	* [0-print_list_integer.py](0-print_list_integer.py) - Write a function that prints all integers of a list.
		- Prototype: `def print_list_integer(my_list=[]):`
		- Format: one integer per line
		- You are not allowed to import any module
		- You can assume that the list only contains integers
		- You are not allowed to cast integers into strings
		- You have to use `str.format()` to print integers

* **1. Secure access to an element in a list**		
	* [1-element_at.py](1-element_at.py) - Write a function that retrieves an element from a list like on C.
		- Prototype: `def element_at(my_list, idx):`
		- If `idx` is negative, the function should return `None`
		- If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
		- You are not allowed to import any module
		- You are not allowed to use `try/except`

* **2. Replace element**		
	* [2-replace_in_list.py](2-replace_in_list.py) - Write a function that replaces an element of a list at a specific position (like in C).
		- Prototype: `def replace_in_list(my_list, idx, element):`
		- If `idx` is negative, the function should not modify anything, and returns the original list
		- If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
		- You are not allowed to import any module
		- You are not allowed to use `try/except`

* **3. Print a list of integers... in reverse!**
	* [3-print_reversed_list_integer.py](3-print_reversed_list_integer.py) - Write a function that prints all integers of a list, in reverse order.
		- Prototype: `def print_reversed_list_integer(my_list=[]):`
		- Format: one integer per line. See example
		- You are not allowed to import any module
		- You can assume that the list only contains integers
		- You are not allowed to cast integers into strings
		- You have to use `str.format()` to print integers

* **4. Replace in a copy**
	* [4-new_in_list.py](4-new_in_list.py) - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
		- Prototype: `def new_in_list(my_list, idx, element):`
		- If `idx` is negative, the function should return a copy of the original `list`
		- If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
		- You are not allowed to import any module
		- You are not allowed to use `try/except`

* **5. Can you C me now?**
	* [5-no_c.py](5-no_c.py) - Write a function that removes all characters `c` and `C` from a string.
		- Prototype: `def no_c(my_string):`
		- The function shoud return the new string
		- You are not allowed to import any module
		- You are not allowed to use `str.replace()`
		
* **6. Lists of lists = Matrix**
	* [6-print_matrix_integer.py](6-print_matrix_integer.py) - Write a function that prints a matrix of integers.
		- Prototype: `def print_matrix_integer(matrix=[[]]):`

* **7. Tuples addition**
	* [7-add_tuple.py](7-add_tuple.py) - Write a function that adds 2 tuples.
		- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
		- Returns a tuple with 2 integers:
  			- The first element should be the addition of the first element of each argument
  			- The second element should be the addition of the second element of each argument
		- You are not allowed to import any module
		- You can assume that the two tuples will only contain integers
		- If a tuple is smaller than 2, use the value 0 for each missing integer
		- If a tuple is bigger than 2, use only the first 2 integers
		
* **8. More returns!**
	* [8-multiple_returns.py](8-multiple_returns.py) - Write a function that returns a tuple with the length of a string and its first character.
		- Prototype: `def multiple_returns(sentence):`
		- If the sentence is empty, the first character should be equal to `None`
		- You are not allowed to import any module

* **9. Find the max**
	* [9-max_integer.py](9-max_integer.py) - Write a function that finds the biggest integer of a list.
		- Prototype: `def max_integer(my_list=[]):`
		- If the list is empty, return `None`
		- You can assume that the list only contains integers
		- You are not allowed to import any module
		- You are not allowed to use the builtin `max()`

* **10. Only by 2**	
	* [10-divisible_by_2.py](10-divisible_by_2.py) - Write a function that finds all multiples of 2 in a list.
		- Prototype: `def divisible_by_2(my_list=[]):`
		- Return a new list with `True` or `False`, depending on wether the integer at the same position in the original list is a multiple of 2
		- The new list should have the same size as the original list
		- You are not allowed to import any module

* **11. Delete at**		
	* [11-delete_at.py](11-delete_at.py) - Write a function that deletes the item at a specific position in a list.
		- Prototype: `def delete_at(my_list=[], idx=0):`
		- If `idx` is negative or out of range, nothing change
		- You are not allowed to use `pop()`
		- You are not allowed to import any module
		
* **12. Switch**
	* [12-switch.py](./12-switch.py): Python program that switches the values of variable `a` and `b`.
  		* Completion of [this source code](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py).

* **13. Linked list palindrome**
	* [13-is_palindrome.c](./13-is_palindrome.c): C function that checks if a singly-linked list is a palindrome.
  		* If the function is not a palindrome - returns `0`.
  		* If the function is a palindrome - returns `1`.
  		* An empty list is considered a palindrome.
  		* Helper files:
    			* [linked_lists.c](./linked_lists.c): C functions handling linked lists for testing 
			[13-is_palindrome.c](./13-is_palindrome.c) (provided by Holberton School).
			* [lists.h](./lists.h): Header file containing definitions and prototypes for all types and functions used in 
			[linked_lists.c](./linked_lists.c) and [13-insert_number.c](./13-insert_number.c).

* **14. CPython #0: Python lists**
  * [100-print_python_list_info.c](./100-print_python_list_info.c): C function that prints basic information about Python lists.
	- Prototype: `void print_python_list_info(PyObject *p);`
	- Your shared library will be compiled with this command line: 

	``` gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c ```
		
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
