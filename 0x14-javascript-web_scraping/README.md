<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>
<img src="https://img.shields.io/badge/JavaScript-yellow.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# Javascript - Objects, Scopes and Closures

This project contains some tasks for learning about `objects`, `scopes`, and `closures` in **JavaScript**.

<p align="center">
  <img width="200"  
        src="https://amudhanbala.com/images/javascript/understanding-scope-and-closure-in-javascript/scopeclosure.png"
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
	
The project contains some tasks about how to use Javascript with regards to: objects, classes, super, extends, prototypes, inheritance, and closures.

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=javascript+objects+scopes+closures&oq=javascript+objects+scopes+closures&aqs=chrome..69i57j69i60j69i61.10327j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=javascript+objects+scopes+closures)

- [JavaScript object basics](https://intranet.hbtn.io/rltoken/OJ4pU6uHwfCrAclbZsk_Hg) 
- [Object-oriented JavaScript](https://intranet.hbtn.io/rltoken/vLr7QS9h4-nGFKVn5vsrvQ) 
 (read all examples!)
- [Class - ES6](https://intranet.hbtn.io/rltoken/zMWxOmGWEsOCldCKeDswCA) 
- [super - ES6](https://intranet.hbtn.io/rltoken/DTMKogwFYEgUnpLrNvTcfQ) 
- [extends - ES6](https://intranet.hbtn.io/rltoken/fh2JHfNNa-HLnmfSdOo9TA) 
- [Object prototypes](https://intranet.hbtn.io/rltoken/lrlwnQMM82RimJJcfLao5w) 
- [Inheritance in JavaScript](https://intranet.hbtn.io/rltoken/vLr7QS9h4-nGFKVn5vsrvQ) 
- [Closures](https://intranet.hbtn.io/rltoken/qDa7F8060Jlhe3DZZitY4A) 
- [this/self](https://intranet.hbtn.io/rltoken/ockP7FQKKmTRvfeAHw-XSw) 
- [Modern JS](https://intranet.hbtn.io/rltoken/22mdHf9KeFhRQrLP-e1hPw) 
 
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs` 
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node` 
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should be **`semistandard`** compliant (version 16.x.x). **[Rules of Standard](https://intranet.hbtn.io/rltoken/EK3q1S4Ouo08kTMI42cSig)** + **[semicolons on top](https://intranet.hbtn.io/rltoken/FuXjfOYe18hUXCDoyMxBSg)**. 
- Also as reference: **[AirBnB style](https://intranet.hbtn.io/rltoken/iIDdBVB4HNhPpb_5e5L-Qg)**
- All files must be executable
- The length of files will be tested using `wc`
- Not allowed to use `var`

## More Info
### Install Node 14
 `$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs`
### Install semi-standard
**[Documentation](https://intranet.hbtn.io/rltoken/FuXjfOYe18hUXCDoyMxBSg)**

 `$ sudo npm install semistandard --global` 

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-higher_level_programming.git`	
- Access to directory: `cd 0x13-javascript_objects_scopes_closures`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

+ **Prototypes** for all functions written for the project.
	
| File               | Prototype                                               |
| ------------------ | ------------------------------------------------------- |
| `7-occurrences.js` | `exports.nbOccurences = function (list, searchElement)` |
| `8-esrever.js`     | `exports.esrever = function (list)`                     |
| `9-logme.js`       | `exports.logMe = function (item)`                       |
| `10-converter.js`  | `exports.converter = function (base)`                   |

### Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. Provided by Holberton School.
		
---

## Tasks

+ [x] 0\. **Rectangle #0**

+ **[0-rectangle.js](./0-rectangle.js)**

* Write an empty class `Rectangle` that defines a rectangle:
	* Use the `class` notation for defining your class
 
```bash
$ ./0-main.js
Rectangle {}
[Class: Rectangle]
$ 
```
---
 
+ [x] 1\. **Rectangle #1**

+ **[1-rectangle.js](./1-rectangle.js)**

* Write a class `Rectangle` that defines a rectangle:
	* Use the `class` notation for defining your class
	* The constructor must take 2 arguments `w` and `h` 
	* Initialize the instance attribute `width` with the value of `w` 
	* Initialize the instance attribute `height` with the value of `h`

```bash
$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
$ 
```
---
 
+ [x] 1\. **Rectangle #2**

+ **[2-rectangle.js](./2-rectangle.js)**

* Write a class `Rectangle` that defines a rectangle:
	* Use the `class` notation for defining your class
	* The constructor must take 2 arguments `w` and `h` 
	* Initialize the instance attribute `width` with the value of `w` 
	* Initialize the instance attribute `height` with the value of `h` 
	* If `w` or `h` is equal to 0 or not a positive integer, create an empty object

```bash
$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
$ 
```
---

+ [x] 3\. **Rectangle #3**

+ **[3-rectangle.js](./3-rectangle.js)**

* Write a class `Rectangle` that defines a rectangle:
	* Use the `class` notation for defining your class
	* The constructor must take 2 arguments: `w` and `h` 
	* Initialize the instance attribute `width` with the value of `w` 
	* Initialize the instance attribute `height` with the value of `h` 
	* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
	* Create an instance method called `print()` that prints the rectangle using the character `X`
 
```bash
$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
$ 
```
---

+ [x] 4\. **Rectangle #4**

+ **[4-rectangle.js](./4-rectangle.js)**

* Write a class `Rectangle` that defines a rectangle:
	* Use the `class` notation for defining your class
	* The constructor must take 2 arguments: `w` and `h` 
	* Initialize the instance attribute `width` with the value of `w` 
	* Initialize the instance attribute `height` with the value of `h` 
	* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
	* Create an instance method called `print()` that prints the rectangle using the character `X` 
	* Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
	* Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

```bash
$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ 
```
---
 
+ [x] 5\. **Square #0**

+ **[5-square.js](./5-square.js)**

* Write a class `Square` that defines a square and inherits from  `Rectangle` of `4-rectangle.js`:
	* Use the `class` notation for defining your class and `extends` 
	* The constructor must take 1 argument: `size` 
	* The constructor of `Rectangle` must be called (by using `super()`)

```bash
$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
$ 
```
---

+ [x] 6\. **Square #1**

+ **[6-square.js](./6-square.js)**

* Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:
	* Use the `class` notation for defining your class and `extends` 
	* Create an instance method called `charPrint(c)` that prints the rectangle using the character `c` 
		* If `c` is `undefined` , use the character `X` 

```bash
$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
$ 
```
---
 
+ [x] 7\. **Occurrences**

+ **[7-occurrences.js](./7-occurrences.js)**

* Write a function that returns the number of occurrences in a list:
	* Prototype: `exports.nbOccurences = function (list, searchElement)`
 
```bash
$ ./7-main.js
1
4
2
$ 
```
---
 
+ [x] 8\. **Esrever**

+ **[8-esrever.js](./8-esrever.js)**

* Write a function that returns the reversed version of a list:
	* Prototype: `exports.esrever = function (list)` 
	* You are not allow to use the built-in method `reverse`
 
```bash
$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'School' ]
$ 
```
---

+ [x] 9\. **Log me**

+ **[9-logme.js](./9-logme.js)**

*Write a function that prints the number of arguments already printed and the new argument value. (see example below)
	* Prototype: `exports.logMe = function (item)` 
	* Output format: `<number arguments already printed>: <current argument value>`

```bash
$ ./9-main.js
0: Hello
1: Best
2: School
$ 
```
---

+ [x] 10\. **Number conversion**

+ **[10-converter.js](./10-converter.js)**

* Write a function that converts a number from base 10 to another base passed as argument:
	* Prototype: `exports.converter = function (base)` 
	* Not allowed to import any file
	* Not allowed to declare any new variable (`var`, `let`, etc..)

```bash
$ ./10-main.js
2
12
89
2
c
59
$ 
```
---

+ [x] 11\. **Factor index**

+ **[100-map.js](./100-map.js)**

* Write a script that imports an array and computes a new array.
	* The script must import `list` from the file `100-data.js` 
	* Use a `map`. **[Tips](https://intranet.hbtn.io/rltoken/aWmgrzMUMiiuFI_ivcgfKw)**

	* A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
	* Print both the initial list and the new list

```bash
$ ./100-map.js 
[ 1, 2, 3, 4, 5 ]
[ 0, 2, 6, 12, 20 ]
$ 
```
---

+ [x] 12\. **Sorted occurences**

+ **[101-sorted.js](./101-sorted.js)**

* Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
	* Your script must import `dict` from the file `101-data.js` 
	* In the new dictionary:
		* A key is a number of occurrences
		* A value is the list of user ids
	* Print the new dictionary at the end

```bash
$ ./101-sorted.js 
{ '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
$ 
```
---

+ [x] 13\. **Concat files**

+ **[102-concat.js](./102-concat.js)**

* Write a script that concats 2 files.
	* The first argument is the file path of the first source file
	* The second argument is the file path of the second source file
	* The third argument is the file path of the destination

```bash
$ ./102-concat.js fileA fileB fileC
$ cat fileC
C is fun!
Python is Cool!!!
$ 
```
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
