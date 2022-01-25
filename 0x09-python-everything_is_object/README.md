![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x09. Python - Everything is object
<div style="text-align: justify">

In this project, you should to respond basic questions about `types` and `objects` in python, and learn that `"Everything is object"` in python.

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

* [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
* [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
* [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
* [Mutation](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects)(Only this chapter)
* [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
* [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

	
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

### `.txt ` Answer Files :pushpin:
* Only one line
* No Shebang
* All your files should end with a new line
	

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.
		
## Tasks :page_with_curl:

* **0. Who am I?**
  * [0-answer.txt](./0-answer.txt): What function would you use to print the type of an object?


* **1. Where are you?**
  	* [1-answer.txt](./1-answer.txt): How do you get a variable's identifier
	(which is the memory address in the CPython implementation)?

* **2. Right count**
  	* [2-answer.txt](./2-answer.txt): In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 100
```

* **3. Right count =**
  	* [3-answer.txt](./3-answer.txt): In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 89
```

* **4. Right count =**
  	* [4-answer.txt](./4-answer.txt): In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a
```

* **5. Right count =+**
  	* [5-answer.txt](./5-answer.txt): In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a + 1
```

* **6. Is equal**
  	* [6-answer.txt](./6-answer.txt): What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

* **7. Is the same**
  	* [7-answer.txt](./7-answer.txt): What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

* **8. Is really equal**
  	* [8-answer.txt](./1-answer.txt): What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

* **9. Is really the same**
  	* [9-answer.txt](./9-answer.txt): What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

* **10. And with a list, is it equal**
  	* [10-answer.txt](./10-answer.txt): What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```

* **11. And with a list, is it the same**
  	* [11-answer.txt](./11-answer.txt): What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```

* **12. And with a list, is it really equal**
  	* [12-answer.txt](./12-answer.txt): What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

* **13. And with a list, is it really the same**
  	* [13-answer.txt](./13-answer.txt): What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

* **14. List append**
  	* [14-answer.txt](./14-answer.txt): What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

* **15. List add**
  * [15-answer.txt](./15-answer.txt): What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

* **16. Integer incrementation**
  	* [16-answer.txt](./16-answer.txt): What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

* **17. List incrementation**
  	* [17-answer.txt](./17-answer.txt): What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

* **18. List assignation**
  	* [18-answer.txt](./18-answer.txt): What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

* **19. Copy a list object**
  	* [19-copy_list.py](./19-copy_list.py): Python function `def copy_list(l):` that returns
a copy of a list.

* **20. Tuple or not?**
  	* [20-answer.txt](./20-answer.txt): Is `a` a tuple?
```
a = ()
```

* **21. Tuple or not?**
 	* [21-answer.txt](./21-answer.txt): Is `a` a tuple?
```
a = (1, 2)
```

* **22. Tuple or not?**
  	* [22-answer.txt](./22-answer.txt): Is `a` a tuple?
```
a = (1)
```

* **23. Tuple or not?**
  	* [23-answer.txt](./23-answer.txt): Is `a` a tuple?
```
a = (1, )
```

* **24. Who I am?**
  	* [24-answer.txt](./24-answer.txt): What does this script print?
```
a = (1)
b = (1)
a is b
```

* **25.  Tuple or not**
  	* [25-answer.txt](./25-answer.txt): What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```

* **26. Empty is not empty**
  	* [26-answer.txt](./26-answer.txt): What does this script print?
```
a = ()
b = ()
a is b
```

* **27.  Still the same?**
  	* [27-answer.txt](./27-answer.txt): Will the last line of this script print `139926795932424`?
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

* **28.  Same or not?**
  	* [28-answer.txt](./28-answer.txt): Will the last line of this script print `139926795932424`?
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

* **30. #pythonic**
  	* [100-magic_string.py](./100-magic_string.py): Python function `magic_string()` that returns the
	string `"BestSchool"` n times the number of iteration.

* **31. Low memory cost**
  	* [101-locked_class.py](./101-locked_class.py): Python class `LockedClass` with no attributes that
	prevents the user from dynamically creating any new instance attributes not
	called `first_name`.

		
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
