![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x01. Python - if/else, loops, functions.
<div style="text-align: justify">

In this project, you should continue to learn and practice the basic concepts of python language.
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

* [lists.h](./lists.h): Header file containing definitions and prototypes for the types
and functions written for `task 10` in this project.
		

| Type/File                  | Definition/Prototype                                                             |
| -------------------------- | -------------------------------------------------------------------------------- |
| `0-run`        	     | `$PYFILE`                                          				|
| `1-run_inline`             | `$PYCODE`                                        				|
| `2-print.py`        	     | `print`                                          				|
| `3-print_number.py`        | `number`                                        					|		
| `4-print_float.py`         | `float`                                          				|
| `5-print_string.py`        | `str`                                        					|		
| `6-concat.py`        	     | `str1` and  `str2`                                        			|
| `7-edges.py`               | `word_first_3` ,  `word_last_2` , `middle_word`                                	|		
| `8-concat_edges.py`        | `object-oriented programming with Python`                                        |
| `9-easter_egg.py`          | ` “The Zen of Python”, by Tim Peters`                                		|		
| `10-check_cycle.c`         | `int check_cycle(listint_t *list);`                                        	|
| `100-write.py`             | `write`                                						|		
		
## Tasks :page_with_curl:

* **0. Positive anything is better than negative nothing**
  * [0-positive_or_negative.py](./0-positive_or_negative.py): Write a Shell script that runs a Python script.
    The Python file name will be saved in the environment variable `$PYFILE`.

* **1. The last digit**
  * [1-last_digit.py](./1-last_digit.py): Write a Shell script that runs Python code.
    The Python code will be saved in the environment variable `$PYCODE`.
		
* **2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game**
  * [2-print_alphabet.py](./2-print_alphabet.py): Write a Python script that prints exactly `"Programming is like building a multilingual puzzle,` followed by a new line.
    	* Use the function `print`.

* **3. When I was having that alphabet soup, I never thought that it would pay off**
  * [3-print_alphabt.py](./3-print_alphabt.py): Prints the `integer` stored in the variable `number`, followed by `Battery street`, followed by a new line.

* **4. Hexadecimal printing**
  * [4-print_hexa.py](./4-print_hexa.py): Prints the `float` stored in the variable `number` with a precision of `2 digits`.
		
* **5. 00...99**
  * [5-print_comb2.py](./5-print_comb2.py): Prints `3 times` a `string` stored in the variable `str`, followed by its first 9 characters.

* **6. Inventing is a combination of brains and materials. The more brains you use, the less material you need**
  * [6-print_comb3.py](./6-print_comb3.py): Print `Welcome to Holberton School!`
		
* **7. islower**
  * [7-islower.py](./7-islower.py): Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py).

* **8. To uppercase**
  * [8-uppercase.py](./8-uppercase.py): Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.
		
* **9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important**
  * [9-print_last_digit.py](./9-print_last_digit.py): Write a Python script that prints `“The Zen of Python”, by Tim Peters`, followed by a new line.
		* Your script should be maximum `98` characters long (please check with `wc -m 9-easter_egg.py`)

* **10. a + b**
  * [10-add.py](./10-add.py): Write a C function that checks if a singly linked list has a `cycle` in it.
		
* **11. a ^ b**
  * [11-pow.py](./11-pow.py): Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

* **12. Fizz Buzz**
  * [12-fizzbuzz.py](./12-fizzbuzz.py): Write a script that compiles a Python script file.
		* The Python file name will be stored in the environment variable `$PYFILE`.
		** The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)
		
* **13. Insert in sorted linked list**
  * [13-insert_number.c](./13-insert_number.c): Write the Python function `def magic_calculation(a, b)`.
	
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
