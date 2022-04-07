<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>

</p>

---

# 0x0B. Python - Input/Output
<div style="text-align: justify">

In this project, you should to learn, practice file handling in Python. Do you use the builtin with, `open`, and `read` functions with the `json` module to `read` and `write` files and serialize and deserialize objects with `JSON`. 

Don't forget to fully meet the following development requirements.
	
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
	
## Resources :books:
Read or watch:

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=programing+in+python&hl=es&ei=bUHBYY7XBrCNwbkP15C0qAk&oq=programing+in+py&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEENKBAhBGABKBAhGGABQhBdYjxxg4C1oAnACeACAAbUBiAGsApIBAzAuMpgBAKABAcgBCsABAQ&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=programing+python)

* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)(until “11.4 Binary Files” (included))
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)(ch. 8 p 180-183 and ch. 14 p 326-333)

	
## Requirements
### General
	
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
* All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'`
	and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method
	<div style="text-align: justify">
	(the length of it will be verified)

	
## More Info
	
### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-higher_level_programming.git`	
- Access to directory: `cd 0x0B-python-input_output`
- `Compile` accord to `instructions` of each task.	

## Files :file_folder:
		
Prototypes and functions written in this project:

| File        | Prototype               |
| ----------- | ----------------------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-write_file.py` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |		
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `12-pascal_triangle.py` | `def pascal_triangle(n):` |
| `100-append_after.py` | `def append_after(filename="", search_string="", new_string=""):` |

		
## Test :heavy_check_mark:		
		
* [tests](./tests): Folder of main files. Provided by Holberton School.
	
## Tasks

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): Python function that prints the contents of a UTF8 text
  file to standard output.

* **1. Write to a file**
  * [1-write_file.py](./1-write_file.py): Python function that writes a string to a UTF8 text
  file and returns the number of characters written.

* **2. Append to a file**
  * [2-append_write.py](./2-append_write.py): Python function that appends a string to the end of a
  UTF8 text file and returns the number of characters appended.

* **3. To JSON string**
  * [3-to_json_string.py](./3-to_json_string.py): Python function that returns the JSON string
  representation of an object.

* **4. From JSON string to Object**
  * [4-from_json_string.py](./4-from_json_string.py): Python function that returns the Python object
  represented by a JSON string.

* **5. Save Object to a file**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): Python function that writes an object to a text
  file using JSON representation.

* **6. Create object from a JSON file**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): Python function that creates an object from a
  `.json` file.

* **7. Load, add, save**
  * [7-add_item.py](./7-add_item.py): Python script that stores all command line arguments to a
  Python list saved in the file `add_item.json`.

* **8. Class to JSON**
  * [8-class_to_json.py](./8-class_to_json.py): Python function that returns the dictionary
  description for simple Python data structures (lists, dictionaries, strings,
  integers and booleans).

* **9. Student to JSON**
  * [9-student.py](./9-student.py): Python class `Student` that defines a student. Includes:
    * Public instance attributes `first_name`, `last_name`, and `age`.
    * Instantiation with `first_name`, `last_name`, and `age`:
    `def __init__(self, first_name, last_name, age):`.
    * Public method `def to_json(self):` that returns the dictionary
    representation of a `Student` instance.

* **10. Student to JSON with filter**
  * [10-student.py](./10-student.py): Python class `Student` that defines a student. Builds on
  [9-student.py](./9.student.py) with:
    * Public method `def to_json(self, attrs=None):` that returns the
    dictionary representation of a `Student` instance.
    * If `attrs` is a list of strings, only the attributes listed are
    represented in the dictionary.

* **11. Student to disk and reload**
  * [11-student.py](./11-student.py): Python class `Student` that defines a student. Builds on
  [10-student.py](./10-student.py) with:
    * Public method `def reload_from_json(self, json):` that replaces all
    attributes of the `Student` instance using the key/value pairs listed in `json`.
    * The method assumes `json` is a dictionary containing attributes with
    name/value corresponding to key/value.

* **12. Pascal's Triangle**
  * [12-pascal_triangle.py](./12-pascal_triangle.py): Python function that returns a list of lists of
  integers representing Pascal's triangle of size `n`.
  * Assumes the size parameter `n` is an integer.
  * If `n` is less than or equal to `0`, returns an empty list.

* **13. Search and update**
  * [100-append_after.py](./100-append_after.py): Python function that inserts a line of text to a
  file after each line containing a specified string.

		
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
