![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x04. Python - More Data Structures: Set, Dictionary.
<div style="text-align: justify">

In this project, you should to learn and practice the concepts about `sets` and `dictionaries` in python language, using them
with the `lambda`, `map`, `filter`, and `reduce` methods.
	
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

* [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
* [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)
	
**man or help**:

`python3`
	
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

| File                           | Prototype                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `0-square_matrix_simple.py`    | `def square_matrix_simple(matrix=[]):`                                                                    |
| `1-search_replace.py`          | `def search_replace(my_list, search, replace):`                                                           |
| `2-uniq_add.py`                | `def uniq_add(my_list=[]):`                                                                               |
| `3-common_elements.py`         | `def common_elements(set_1, set_2):`                                                                      |
| `4-only_diff_elements.py`      | `def only_diff_elements(set_1, set_2):`                                                                   |
| `5-number_keys.py`             | `def number_keys(a_dictionary):`                                                                          |
| `6-print_sorted_dictionary.py` | `def print_sorted_dictionary(a_dictionary):`                                                              |
| `7-update_dictionary.py`       | `def update_dictionary(a_dictionary, key, value):`                                                        |
| `8-simple_delete.py`           | `def simple_delete(a_dictionary, key=""):`                                                                |
| `9-multiply_by_2.py`           | `def multiply_by_2(a_dictionary):`                                                                        |
| `10-best_score.py`             | `def best_score(a_dictionary):`                                                                           |
| `11-mutiply_list_map.py`       | `def mutiply_list_map(my_list=[], number=0):`                                                             |
| `12-roman_to_int.py`           | `def roman_to_int(roman_string):`                                                                         |
| `100-weight_average.py`        | `def weight_average(my_list=[]):`                                                                         |
| `101-square_matrix_map.py`     | `def square_matrix_map(matrix=[]):`                                                                       |
| `102-complex_delete.py`        | `def complex_delete(a_dictionary, value):`                                                                |

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.
		
## Tasks :page_with_curl:

* **0. Squared simple**
  	* [0-square_matrix_simple.py](./0-square_matrix_simple.py): Python function that computes
  	the square value of all integers of a matrix.
  		* The parameter `matrix` is a two-dimensional array.
 		* Returns a matrix of the same size as `matrix` where each value is the
  		square of the input value.
  		* The initial matrix is not modified.
  		* Without importing modules.

* **1. Search and replace**
  	* [1-search_replace.py](./1-search_replace.py): Python function that replaces all occurences
  	of an element by another in a new list.
 		* The parameter `my_list` is the initial list.
  		* The parameter `search` is the element to replace in the list.
  		* The parameter `replace` is the new element.
  		* Without importing modules.

* **2. Unique addition**
  	* [2-uniq_add.py](./2-uniq_add.py): Python function that adds all unique integers in
  	a list (once for each integer).
  		* Without importing modules.

* **3. Present in both**
  	* [3-common_elements.py](./3-common_elements.py): Python function that returns a
  	set of common elements in two sets.
  		* Without importing modules.

* **4. Only differents**
  	* [4-only_diff_elements.py](./4-only_diff_elements.py): Python function that returns a
  	set of all elements present in only one set.
  		* Without importing modules.

* **5. Number of keys**
  	* [5-number_keys.py](./5-number_keys.py): Python function that returns the number of
  	keys in a dictionary.
  		* Without importing modules.

* **6. Print sorted dictionary**
  	* [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py): Python function that
  	prints a dictionary by ordered keys.
 		* The function assumes all keys are strings.
  		* Keys are printed in alphabetic order.
  		* Keys are only sorted on the first level.
  		* Dictionary values can have any type.
  		* Without importing modules.

* **7. Update dictionary**
  	* [7-update_dictionary.py](./7-update_dictionary.py): Python function that replaces or
  	adds key/value pairs in a dictionary.
  		* The parameter `key` is always a string.
  		* The parameter `value` is any type.
  		* If a key exists in the dictionary, the value is replaced.
  		* If a key does not exist in the dictionary, it is created.
  		* Without importing modules.

* **8. Simple delete by key**
  	* [8-simple_delete.py](./8-simple_delete.py): Python function that deletes a key
  	in a dictionary.
  		* The paramter `key` is always a string.
  		* If the key does not exist, the dictionary does not change.
  		* Without importing modules.

* **9. Multiply by 2**
  	* [9-multiply_by_2.py](./9-multiply_by_2.py): Python function that returns a
  	new dictionary with all values multiplied by 2.
  		* The function assumes all values are integers.
  		* Without importing modules.

* **10. Best score**
  	* [10-best_score.py](./10-best_score.py): Python function that returns a key value
  	with the biggest integer value.
  		* The function assumes all values are integers.
  		* The function assumes all students have a different score.
  		* If no score is found, the functino returns `None`.
  		* Without importing modules.

* **11. Multiply by using map**
  	* [11-mutiply_list_map.py](./11-multiply_list_map.py): Python function that returns a
  	list with all values multiplied by a number using `map`.
  		* Returns a new length of the same length has `my_list` with each value
  		multiplied by `number`.
  		* The initial list is not modified.
  		* Without using loops or importing modules.

* **12. Roman to Integer**
  	* [12-roman_to_int.py](./12-roman_to_int.py): Python function that converts a roman
  	numeral to an integer.
  		* The function assumes the number will be between 1-3999.
  		* If the parameter `roman_string` is not a string or `None`, the function returns `0`.

* **13. Weighted average!**
  	* [100-weight_average.py](./100-weight_average.py): Python function that returns the
 	weighted average of all integers in a list of tuples.
  		* Tuple format: `(<score>, <weight>)`.
  		* If the list is empty - returns `0`.
  		* Without importing modules.

* **14. Squared by using map**
  	* [101-square_matrix_map.py](./101-square_matrix_map.py): Python function that computes
  	the square value of all integers of a matrix using `map`.
  		* The parameter `matrix` is a two-dimensional array.
  		* Returns a new matrix of the same size as `matrix` with each value squared.
  		* The initial matrix is not modified.
  		* Without using loops or importing modules.

* **15. Delete by value**
  	* [102-complex_delete.py](./102-complex_delete.py): Python function that deletes keys with
  	a specific value in a dictionary.
  		* If the value does not exists, the dictionary is not changed.
  		* All keys having the searched value are deleted.
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
