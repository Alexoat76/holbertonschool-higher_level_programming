<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>
<img src="https://img.shields.io/badge/JavaScript-yellow.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x12. JavaScript - Warm up

This project contains some tasks for learning the basics of **JavaScript**.

<p align="center">
  <img width="180"  
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/2048px-Unofficial_JavaScript_logo_2.svg.png"
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
	
The project contains some tasks for learning the basics topics of **JavaScript**.

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=javascript&oq=javascript&aqs=chrome..69i57j0i512l9.2986j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=javaScript)

- [Writing JavaScript Code](https://intranet.hbtn.io/rltoken/OdMLtl6Y9mpQkaoEqJCRSg) 
- [Variables](https://intranet.hbtn.io/rltoken/iE6zaLw7pybp648IfRmk5Q) 
- [Data Types](https://intranet.hbtn.io/rltoken/4td1BbZAYn4Dldi6k0CY7A) 
- [Operators](https://intranet.hbtn.io/rltoken/OdMLtl6Y9mpQkaoEqJCRSg) 
- [Operator Precedence](https://intranet.hbtn.io/rltoken/ALCoiVRvxmsjdqCUdWC_lg) 
- [Controlling Program Flow](https://intranet.hbtn.io/rltoken/Nlfhdy6Thyu_WgtBSqoAUw) 
- [Functions](https://intranet.hbtn.io/rltoken/Ta66PZ6_16K3q99oELvjkQ) 
- [Objects and Arrays](https://intranet.hbtn.io/rltoken/osu583B5jskDVwmcm50-NQ) 
- [Intrinsic Objects](https://intranet.hbtn.io/rltoken/osu583B5jskDVwmcm50-NQ) 
- [Module patterns](https://intranet.hbtn.io/rltoken/mduSK-WOoRe6WohU1p2zZQ) 
- [var, let and const](https://intranet.hbtn.io/rltoken/kNWuHjyUvjr74wU2hBqd_A) 
- [JavaScript Tutorial](https://intranet.hbtn.io/rltoken/qkp1hdLiI8DJje88bxcL6w) 
- [Modern JS](https://intranet.hbtn.io/rltoken/ieSajamJQ-Nv3XzcS_d5lA) 
 
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs` 
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly  ` #!/usr/bin/node ` 
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be **`semistandard`** compliant (version 16.x.x). **[Rules of Standard](https://intranet.hbtn.io/rltoken/EK3q1S4Ouo08kTMI42cSig)** + **[semicolons on top](https://intranet.hbtn.io/rltoken/FuXjfOYe18hUXCDoyMxBSg)**. 
- Also as reference: **[AirBnB style](https://intranet.hbtn.io/rltoken/iIDdBVB4HNhPpb_5e5L-Qg)**
- All your files must be executable
- The length of your files will be tested using `wc`

## More Info
### Install Node 14
 `$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs`
### Install semi-standard
**[Documentation](https://intranet.hbtn.io/rltoken/FuXjfOYe18hUXCDoyMxBSg)**

 `$ sudo npm install semistandard --global` 

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-higher_level_programming.git`	
- Access to directory: `cd 0x12-javascript-warm_up
`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

+ **Prototypes** for all functions written for the project.
	
| File                  | Prototype                        |
| ----------------------| ---------------------------------|
| `9-add.js`            | `function add(a, b)`             | 
| `13-add.js`           | `exports.add = (a, b)`           |
| `101-call_me_moby.js` | `function (x, theFunction)`      |
| `102-add_me_maybe.js` | `function (number, theFunction)` |

### Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. Provided by Holberton School.
		
---

## Tasks

+ [x] 0\. **First constant, first print**

+ **[0-javascript_is_amazing.js](./0-javascript_is_amazing.js)**

* Write a script that prints “JavaScript is amazing”:
	* Create a constant variable called `myVar` with the value “JavaScript is amazing”
	* Use `console.log(...) `to print all output
	* Not allowed to use `var` 

```bash
$ ./0-javascript_is_amazing.js 
JavaScript is amazing
$ 
$ semistandard ./0-javascript_is_amazing.js 
$ 
```
---

+ [x] 1\. **3 languages**

+ **[1-multi_languages.js](./1-multi_languages.js)**

* Write a script that prints 3 lines:
	* The first line: “C is fun”
	* The second line: “Python is cool”
	* The third line: “JavaScript is amazing”
	* Use `console.log(...)` to print all output
	* Not allowed to use `var`

```bash
$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
$ 
```
---

+ [x] 2\. **Arguments**

+ **[2-arguments.js](./2-arguments.js)**

* Write a script that prints a message depending of the number of arguments passed:
	* If no arguments are passed to the script, print “No argument”
	* If only one argument is passed to the script, print “Argument found”
	* Otherwise, print “Arguments found”
	* Use `console.log(...)` to print all output
	* Not allowed to use `var` 
	- Reference:  **[process.argv](https://intranet.hbtn.io/rltoken/E5x0rMmgii1g_Da9R7DUag)**

```bash
$ ./2-arguments.js 
No argument
$ ./2-arguments.js Best
Argument found
$ ./2-arguments.js Best School
Arguments found
$ 
```
---

+ [x] 3\. **Value of my argument**

+ **[3-value_argument.js](./3-value_argument.js)**

* Write a script that prints the first argument passed to it:
	* If no arguments are passed to the script, print “No argument”
	* Use `console.log(...)` to print all output
	* Not allowed to use `var` 
	* Not allowed to use `length`

```bash
$ ./3-value_argument.js 
No argument
$ ./3-value_argument.js School
School
$ 
```
---
 
+ [x] 4\. **Create a sentence**

+ **[4-concat.js](./4-concat.js)**

* Write a script that prints two arguments passed to it, in the following format: “ is ”
	* Use `console.log(...)` to print all output
	* Not allowed to use `var`
 
```bash
$ ./4-concat.js c cool
c is cool
$ ./4-concat.js c 
c is undefined
$ ./4-concat.js
undefined is undefined
$ 
```
---
 
+ [x] 5\. **An Integer**

+ **[5-to_integer.js](./5-to_integer.js)**

* Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
	* If the argument can’t be converted to an integer, print “Not a number”
	* Use `console.log(...)` to print all output
	* Not allowed to use `var` 
	* Not allowed to use `try/catch`

```bash

$ ./5-to_integer.js 
Not a number
$ ./5-to_integer.js 89
My number: 89
$ ./5-to_integer.js "89"
My number: 89
$ ./5-to_integer.js 89.89
My number: 89
$ ./5-to_integer.js School
Not a number
$ 
```
---

+ [x] 6\. **Loop to languages**

+ **[6-multi_languages_loop.js](./6-multi_languages_loop.js)**

* Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop
	* The first line: “C is fun”
	* The second line: “Python is cool”
	* The third line: “JavaScript is amazing”
	* Use `console.log(...)`  to print all output
	* Not allowed to use `var` 
	* Not allowed to use any `if/else` statement
	* Use only one `console.log` 
	* Use a loop (`while`, `for`, etc.)

```bash
$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
$ 
```
---
 
+ [x] 7\. **I love C**

+ **[7-multi_c.js](./7-multi_c.js)**

* Write a script that prints `x` times “C is fun”
	* Where `x` is the first argument of the script
	* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
	* Use `console.log(...)` to print all output
	* Not allowed to use `var` 
	* Use only two `console.log` 
	* Use a loop (`while`, `for`, etc.)

```bash
$ ./7-multi_c.js 2
C is fun
C is fun
$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ ./7-multi_c.js 
Missing number of occurrences
$ ./7-multi_c.js -3
$ 
```
---

+ [x] 8\. **Square**

+ **[8-square.js](./8-square.js)**

* Write a script that prints a square
	* The first argument is the size of the square
	* If the first argument can’t be converted to an integer, print “Missing size”
	* Use the character `X`  to print the square
	* Use `console.log(...)`  to print all output
	* Not allowed to use `var` 
	* Use a loop (`while`, `for`, etc.)

```bash
$ ./8-square.js
Missing size
$ ./8-square.js School
Missing size
$ ./8-square.js 2
XX
XX
$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ ./8-square.js -3
$ 
```
---
 
+ [x] 9\. **Add**

+ **[9-add.js](./9-add.js)**

* Write a script that prints the addition of 2 integers
	* The first argument is the first integer
	* The second argument is the second integer
	* You have to define a function with this prototype: `function add(a, b)` 
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
 
```bash
$ ./9-add.js 
NaN
$ ./9-add.js 1
NaN
2$ ./9-add.js 1 7
8
$ ./9-add.js 13 89
102
$ 
```
---

+ [x] 10\. **Factorial**

+ **[10-factorial.js](./10-factorial.js)**

* Write a script that computes and prints a factorial
	* The first argument is integer (argument can be cast as integer) used for computing the factorial
	* Factorial of `NaN` is `1` 
	* Do it recursively
	* Use a function
	* Use `console.log(...)` to print all output
	* Not allowed to use `var`
 
```bash
$ ./10-factorial.js 
1
$ ./10-factorial.js 3
6
$ ./10-factorial.js 89
1.6507955160908452e+136
$ ./10-factorial.js 333
Infinity
$ 
```
---
 
+ [x] 11\. **Second biggest!**

+ **[11-second_biggest.js](./11-second_biggest.js)**

* Write a script that searches the second biggest integer in the list of arguments.
	* You can assume all arguments can be converted to integer
	* If no argument passed, print `0` 
	* If the number of arguments is 1, print `0` 
	* Use `console.log(...)` to print all output
	* Not allowed to use `var`
 
```bash
$ ./11-second_biggest.js 
0
$ ./11-second_biggest.js 1
0
$ ./11-second_biggest.js 4 2 5 3 0 -3
4
$ 
```
---
 
+ [x] 12\. **Object**

+ **[12-object.js](./12-object.js)**

* Update this script to replace the value `12` with `89`:
	* You are not allowed to use `var`
 
```bash
$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
$ 
```
---

+ [x] 13\. **Add file**

+ **[13-add.js](./13-add.js)**

* Write a function that returns the addition of 2 integers.
	* The function must be visible from outside
	* The name of the function must be `add` 
	* You are not allowed to use `var`
 
+ **[Tip](https://intranet.hbtn.io/rltoken/M3uMoMlngAtefSYF1c7PNQ)**

```bash
$ ./13-main.js
8
$ 
```
---
 
+ [x] 14\. **Const or not const**

+ **[100-let_me_const.js](./100-let_me_const.js)**

* Write a file that modifies the value of `myVar` to `333`
 
```bash
$ ./100-main.js
333
$ 
```
+ **Hint**: Scope
+ This exercise doesn’t pass `semistandard` so don’t worry about it.

---

+ [x] 15\. **Call me Moby**

+ **[101-call_me_moby.js](./101-call_me_moby.js)**

Write a function that executes `x` times a function.
	* The function must be visible from outside
	* Prototype: `function (x, theFunction)` 
	* Not allowed to use `var` 

```bash
$ ./101-main.js
C is fun
C is fun
C is fun
$ 
```
---

+ [x] 16\. **Add me maybe**

+ **[102-add_me_maybe.js](./102-add_me_maybe.js)**

* Write a function that increments and calls a function.
	* The function must be visible from outside
	* Prototype: `function (number, theFunction)` 
	* Not allowed to use `var`
 
```bash
$ ./102-main.js
New value: 5
$ 
```
---
 
+ [x] 17\. **Increment object**

+ **[103-object_fct.js](./103-object_fct.js)**

* Update this script by adding a new function `incr` that increments the integer `value`.
* Not allowed to use `var`
 
```bash
$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
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




