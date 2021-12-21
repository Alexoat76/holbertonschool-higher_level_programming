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
and functions written for `task 13`.
		

| Type/File                  | Definition/Prototype                                                             |
| -------------------------- | -------------------------------------------------------------------------------- |
| `0-positive_or_negative.py`| `number`                                          				|
| `1-last_digit.py`          | `number`                                        					|
| `2-print_alphabet.py`      | `print`                                          				|
| `3-print_alphabt.py`       | `print`                                        					|		
| `4-print_hexa.py`          | `print`                                          				|
| `5-print_comb2.py`         | `print`                                        					|		
| `6-print_comb3.py`         | `print`                                        					|
| `7-islower.py`             | `def islower(c):`                                				|		
| `8-uppercase.py`           | `def uppercase(str):`                                        			|
| `9-print_last_digit.py`    | `def print_last_digit(number):`                                			|		
| `10-add.py`                | `def add(a, b):`                                        				|
| `11-pow.py`                | `def pow(a, b):`                                					|		
| `12-fizzbuzz.py`    	     | `def fizzbuzz():`                                				|		
| `13-insert_number.c`       | `listint_t *insert_node(listint_t **head, int number);`                          |
		
## Tasks :page_with_curl:

* **0. Positive anything is better than negative nothing**
  * [0-positive_or_negative.py](./0-positive_or_negative.py): This program will assign a `random` signed `number` to the variable number each time it is executed.
		Complete the source code in order to print whether the number stored in the variable number is `positive or negative`.
* **1. The last digit**
  * [1-last_digit.py](./1-last_digit.py): This program will assign a random signed `number` to the variable `number` each time it is executed. 
		Complete the source code in order to print the last digit of the `number` stored in the variable number.
		
* **2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game**
  * [2-print_alphabet.py](./2-print_alphabet.py): Write a program that prints the `ASCII` alphabet, in lowercase, not followed by a new line.

* **3. When I was having that alphabet soup, I never thought that it would pay off**
  * [3-print_alphabt.py](./3-print_alphabt.py): Write a program that prints the `ASCII` alphabet, in lowercase, not followed by a new line.

* **4. Hexadecimal printing**
  * [4-print_hexa.py](./4-print_hexa.py): Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal.
		
* **5. 00...99**
  * [5-print_comb2.py](./5-print_comb2.py): Write a program that prints numbers from `0` to `99`.

* **6. Inventing is a combination of brains and materials. The more brains you use, the less material you need**
  * [6-print_comb3.py](./6-print_comb3.py): Write a program that prints all possible different `combinations of two digits`.
		
* **7. islower**
  * [7-islower.py](./7-islower.py): Write a function that `checks` for `lowercase` character.

* **8. To uppercase**
  * [8-uppercase.py](./8-uppercase.py): Write a function that `prints` a string in `uppercase` followed by a new line.
		
* **9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important**
  * [9-print_last_digit.py](./9-print_last_digit.py): Write a function that prints the `last digit` of a number.

* **10. a + b**
  * [10-add.py](./10-add.py): Write a function that `adds` two integers and returns the result.
		
* **11. a ^ b**
  * [11-pow.py](./11-pow.py): Write a function that computes `a` to the power of `b` and return the value.

* **12. Fizz Buzz**
  * [12-fizzbuzz.py](./12-fizzbuzz.py): Write a function that prints the numbers from `1` to `100` separated by a space.
		
* **13. Insert in sorted linked list**
  * [13-insert_number.c](./13-insert_number.c): Write a function in C that inserts a number into a sorted singly linked list.
	
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
