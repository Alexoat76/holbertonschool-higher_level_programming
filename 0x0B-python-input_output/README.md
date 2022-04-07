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

<p align="center">
  <img width="300"  
        src="https://cdn-wordpress-info.futurelearn.com/info/wp-content/uploads/1-3-IPO-Star-1.gif"
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
		
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3`.
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- The code should use the pycodestyle (version 2.7).
- All files must be executable.
- The length of files will be tested using `wc`.
	
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
	<div style="text-align: justify">
	(the length of it will be verified)

	
## More Info
	
### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-higher_level_programming.git`	
- Access to directory: `cd 0x0B-python-input_output`
- `Compile` accord to `instructions` of each task.	

## Files :file_folder:
		
Prototypes and functions written in this project:

| File                       | Prototype                                                         |
| ---------------------------| ------------------------------------------------------------------|
| `0-read_file.py`           | `def read_file(filename=""):`                                     |
| `1-write_file.py`          | `def write_file(filename="", text=""):`                           |
| `2-append_write.py`        | `def append_write(filename="", text=""):`                         |
| `3-to_json_string.py`      | `def to_json_string(my_obj):`                                     |
| `4-from_json_string.py`    | `def from_json_string(my_str):`                                   |
| `5-save_to_json_file.py`   | `def save_to_json_file(my_obj, filename):`                        |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):`                              |		
| `8-class_to_json.py`       | `def class_to_json(obj):`                                         |
| `12-pascal_triangle.py`    | `def pascal_triangle(n):`                                         |
| `100-append_after.py`      | `def append_after(filename="", search_string="", new_string=""):` |

		
## Test :heavy_check_mark:		
		
* [tests](./tests): Folder of main files. Provided by Holberton School.
	
## Tasks

+ [x] 0\. **Read file**

+ **[0-read_file.py](./0-read_file.py)**

* Write a function that reads a text file (`UTF8`) and prints it to stdout:
	* Prototype: `def read_file(filename=""):` 
	* Use the `with` statement
	* Don’t need to manage `file permission` or `file doesn't exist` exceptions.
	* Not allowed to import any module

```bash
$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, 
collaborate with your peers. 

A school every software engineer would have dreamt of!
$ 
```
+ No test cases needed
---
 
+ [x] 1\. **Write to a file**

+ **[1-write_file.py](./1-write_file.py)**

* Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:
	* Prototype: `def write_file(filename="", text=""):` 
	* Use the `with` statement
	* Don’t need to manage file permission exceptions.
	* The function should create the file if doesn’t exist.
	* The function should overwrite the content of the file if it already exists.
	* Not allowed to import any module

```bash
$ ./1-main.py
24
$ cat my_first_file.txt
This School is so cool!
$ 
```
+ No test cases needed
---

+ [x] 2\. **Append to a file**

+ **[2-append_write.py](./2-append_write.py)**

* Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:
	* Prototype: `def append_write(filename="", text=""):` 
	* If the file doesn’t exist, it should be created
	* Use the `with` statement
	* Don’t need to manage `file permission` or `file doesn't exist` exceptions.
	* Not allowed to import any module

```bash
$ ./2-main.py
29
$ cat file_append.txt
This School is so cool!
This School is so cool!
$ 
```
+ No test cases needed
---

+ [x] 3\. **To JSON string**

+ **[3-to_json_string.py](./3-to_json_string.py)**

* Write a function that returns the JSON representation of an object (string):
	* Prototype: `def to_json_string(my_obj):` 
	* Don’t need to manage exceptions if the object can’t be serialized.

```bash
$ ./3-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, 
"places": ["San Francisco", "Tokyo"]}
<class 'str'>
[TypeError] {3, 132} is not JSON serializable
$ 
```
+ No test cases needed
---
 
+ [x] 4\. **From JSON string to Object**

+ **[4-from_json_string.py](./4-from_json_string.py)**

* Write a function that returns an object (Python data structure) represented by a JSON string:
	* Prototype:  ` def from_json_string(my_str): ` 
	* Don’t need to manage exceptions if the JSON string doesn’t represent an object.

```bash
$ ./4-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 
'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[JSONDecodeError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
$ 
```
+ No test cases needed
---
 
+ [x] 5\. **Save Object to a file**

+ **[5-save_to_json_file.py](./5-save_to_json_file.py)**

* Write a function that writes an Object to a text file, using a JSON representation:
	* Prototype: `def save_to_json_file(my_obj, filename):` 
	* Use the `with` statement
	* Don’t need to manage exceptions if the object can’t be serialized.
	* Don’t need to manage file permission exceptions.

```bash
$ ./5-main.py
[TypeError] Object of type set is not JSON serializable
$ cat my_list.json ; echo ""
[1, 2, 3]
$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, 
"info": {"average": 3.14, "age": 36}, "is_active": true}
$ cat my_set.json ; echo ""
$ 
```
+ No test cases needed
---

+ [x] 6\. **Create object from a JSON file**

+ **[6-load_from_json_file.py](./6-load_from_json_file.py)**

* Write a function that creates an Object from a “JSON file”:
	* Prototype: `def load_from_json_file(filename):` 
	* Use the `with` statement
	* Don’t need to manage exceptions if the JSON string doesn’t represent an object.
	* Don’t need to manage file permissions / exceptions.

```bash
$ cat my_list.json ; echo ""
[1, 2, 3]
$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, 
"info": {"average": 3.14, "age": 36}, "is_active": true}
$ cat my_fake.json ; echo ""
{"is_active": true, 12 }
$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 
'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
$ 
```
+ No test cases needed
---

+ [x] 7\. **Load, add, save**

+ **[7-add_item.py](./7-add_item.py)**

* Write a script that adds all arguments to a Python list, and then save them to a file:
	* Use your function `save_to_json_file` from `5-save_to_json_file.py` 
	* Use your function `load_from_json_file` from `6-load_from_json_file.py` 
	* The list must be saved as a JSON representation in a file named `add_item.json` 
	* If the file doesn’t exist, it should be created
	* Don’t need to manage file permissions / exceptions.

```bash
$ cat add_item.json
cat: add_item.json: No such file or directory
$ ./7-add_item.py
$ cat add_item.json ; echo ""
[]
$ ./7-add_item.py Best School
$ cat add_item.json ; echo ""
["Best", "School"]
$ ./7-add_item.py 89 Python C
$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]
$ 
```
+ No test cases needed
---
 
+ [x] 8\. **Class to JSON**

+ **[8-class_to_json.py](./8-class_to_json.py)**

* Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) 
	for JSON serialization of an object:
	* Prototype: `def class_to_json(obj):` 
	* `obj` is an instance of a Class
	* All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
	* Not allowed to import any module

```bash
$ ./8-main.py 
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
$ 
$ ./8-main_2.py 
<class '8-my_class_2.MyClass'>
[MyClass] John - 4 => 1
<class 'dict'>
{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
$
```
+ No test cases needed
---

+ [x] 9\. **Student to JSON**

+ **[9-student.py](./9-student.py)**

* Write a class `Student` that defines a student by:
	* Public instance attributes: 
		* `first_name` 
		* `last_name` 
		* `age` 
	* Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):` 
	* Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` 
		instance (same as `8-class_to_json.py`)
	* Not allowed to import any module

```bash
$ ./9-main.py 
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
$ 
```
+ No test cases needed
---
 
+ [x] 10\. **Student to JSON with filter**

+ **[10-student.py](./10-student.py)**

* Write a class `Student` that defines a student by: (based on `9-student.py`)
	* Public instance attributes: 
		* `first_name` 
		* `last_name` 
		* `age` 
	* Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):` 
	* Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student`  
		instance (same as `8-class_to_json.py`):
		- If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
		- Otherwise, all attributes must be retrieved
	* Not allowed to import any module
```bash
$ ./10-main.py 
{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
{'age': 27, 'first_name': 'Bob'}
{'age': 27}
$
```
+ No test cases needed
---

+ [x] 11\. **Student to disk and reload**

+ **[11-student.py](./11-student.py)**

* Write a class `Student` that defines a student by: (based on `10-student.py`)
	* Public instance attributes: 
		* `first_name` 
		* `last_name` 
		* `age` 
	* Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):` 
	* Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student`  
		instance (same as `8-class_to_json.py`):
		- If `attrs` is a list of strings, only attributes name contain in this list must be retrieved. 
		- Otherwise, all attributes must be retrieved
	* Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
		* Assume `json` will always be a dictionary
		* A dictionary key will be the public attribute name
		* A dictionary value will be the value of the public attribute
		* Not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of 
representation of an object to another format, without losing any information and allow us to rebuild 
an object based on this representation)

```bash
$ ./11-main.py student.json
Initial student:
<11-student.Student object at 0x7f832826eda0>
<class '11-student.Student'>
<class 'dict'>
John Doe 23
{"last_name": "Doe", "first_name": "John", "age": 23}
Saved to disk
Fake student:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
Fake Fake 89
Load dictionary from file:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
John Doe 23
$
$ cat student.json ; echo ""
{"last_name": "Doe", "first_name": "John", "age": 23}
$ 
```
+ No test cases needed
---

+ [x] 12\. **Pascal's Triangle**

+ **[12-pascal_triangle.py](./11-student.py)**

* Technical interview preparation : 
* Not allowed to google anything
* Whiteboard first
	Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the 
		Pascal’s triangle of `n`:
* Returns an empty list if `n <= 0` 
* You can assume `n` will be always an integer
* Not allowed to import any module

```bash
$ ./12-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
$ 
```
---

+ [x] 13\. **Search and update**

+ **[100-append_after.py](./100-append_after.py)**

* Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
	* Prototype: `def append_after(filename="", search_string="", new_string=""):` 
	* You must use the `with` statement
	* Don’t need to manage `file permission` or `file does not exist` exceptions.
	* Not allowed to import any module

```bash
$ ./100-main.py
$ cat append_after_100.txt
At School,
Python is really important,
"C is fun!"
But it can be very hard if:
- Do not get all Pythonic tricks
"C is fun!"
- Do not have strong C knowledge.
$ ./100-main.py
$ cat append_after_100.txt
At School,
Python is really important,
"C is fun!"
"C is fun!"
But it can be very hard if:
- Do not get all Pythonic tricks
"C is fun!"
"C is fun!"
- Do not have strong C knowledge.
$ 
```
+ No test cases needed
---

+ [x] 14\. **Log parsing**

+ **[101-stats.py](./101-stats.py)**

* Write a script that reads `stdin` line by line and computes metrics:
	* Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` 
	* Each 10 lines and after a keyboard interruption (`CTRL + C`), prints those statistics since the beginning:
		* Total file size: `File size: <total size>` 
		* where  is the sum of all previous (see input format above)
		* Number of lines by status code: 
			* possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500` 
			* if a status code doesn’t appear, don’t print anything for this status code
			* format: `<status code>: <number>` 
			* status codes should be printed in ascending order

```bash
$ ./101-generator.py | ./101-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./101-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./101-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
$ 
```
+ No test cases needed
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
