<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>
<img src="https://img.shields.io/badge/JavaScript-yellow.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x15. JavaScript - Web jQuery

This project contains some tasks for learning how to *`manipulate`* the *`DOM`* with **`jQuery`**.

<p align="center">
  <img width="400"  
        src="https://mir-s3-cdn-cf.behance.net/project_modules/disp/f57f6625860387.5634bde766c04.gif"
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
	
The project contains some tasks for learning how to use `jQuery` in *`JavaScript`* to manipulate the *`DOM`*.

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=Web+jQuery&oq=Web+jQuery&aqs=chrome..69i57j0i22i30l9.2503j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=Web+jQuery)

- [What is JavaScript?](https://intranet.hbtn.io/rltoken/FBd59d6M-Bal5PiSJbhw9g) 
- [Selector](https://intranet.hbtn.io/rltoken/RtFB5Ycdvvk5OYv79zgr6A) 
- [Get and set content](https://intranet.hbtn.io/rltoken/JAC2vdSj1pbH6y_9OwQrAw) 
- [Manipulate CSS classes](https://intranet.hbtn.io/rltoken/Pvl_U4kdmxtHrZAHoFh_qw) 
- [Manipulate DOM elements](https://intranet.hbtn.io/rltoken/fA1R3S7dNUX4lj68z6qMyw) 
- [API](https://intranet.hbtn.io/rltoken/w_Y67Y3UlGQ6nluZx9KJyQ) 
- [Introduction](https://intranet.hbtn.io/rltoken/LOMQvsml-4ttg2Y2TVNbqQ) 
- [GET & POST request](https://intranet.hbtn.io/rltoken/xN81Z76ZeNgB42tyJOgXjA) 
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.hbtn.io/rltoken/Rq2Ob5rhN-N458YBxxaRXQ) 
- [What went wrong? Troubleshooting JavaScript](https://intranet.hbtn.io/rltoken/ZpjZXl5AxHmurQFuxQfB4A) 
- [JQuery](https://intranet.hbtn.io/rltoken/L5nA7F44DBhrCAdlEvxrqQ) 
- [JQuery API](https://intranet.hbtn.io/rltoken/U3XGm3WaMxON5c-NkBFS6Q) 
- [JQuery Ajax](https://intranet.hbtn.io/rltoken/pZmSwUxd65dxIrX7D4n1pg)  
 
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs` 
- All files will be interpreted on **Chrome** *`(version 57.0)`*
- All files should end with a new line 
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should be **`semistandard`** compliant with the flag *`--global $` : `semistandard *.js --global $`*. 
- Use *`jQuery`* version 3.x
- Not allowed to use `var`
- *`HTML`* should not reload for each action: *`DOM`* **manipulation**, `update values`, `fetch data…`

## More Info
### Import JQuery
```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```	
### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-higher_level_programming.git`	
- Access to directory: `cd 0x15-javascript-web_jquery`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:
### Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. Provided by Holberton School.
		
---

## Tasks
	
+ [x] 0\. **No JQuery**

+ **[0-script.js](./0-script.js)**

* Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
	* Use `document.querySelector` to select the HTML tag
	* Don’t use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
$ 
```
---

+ [x] 1\. **With JQuery**

+ **[1-script.js](./1-script.js)**

* Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
$ 
```
---

+ [x] 2\. **Click and turn red**

+ **[2-script.js](./2-script.js)**

* Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) 
	when the user clicks on the tag `DIV#red_header`:
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
$ 
```
---

+ [x] 3\. **Add `.red` class**

+ **[3-script.js](./3-script.js)**

* Write a JavaScript script that adds the class `red` to the `<header>` element 
	when the user clicks on the tag `DIV#red_header` 
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
$ 
```
---
 
+ [x] 4\. **Toggle classes**

+ **[4-script.js](./4-script.js)**

* Write a JavaScript script that toggles the class of the `<header>` element 
	when the user clicks on the tag `DIV#toggle_header`:
	* The `<header>` element must always have one class: `red` or `green`, 
	never both in the same time and never empty.
	* If the current class is `red`, when the user click on `DIV#toggle_header`, 
	the class must be updated to `green`; and the reverse.
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
$ 
```
---
 
+ [x] 5\. **List of elements**

+ **[5-script.js](./5-script.js)**

* Write a JavaScript script that adds a `<li>` element to a list when the user 
	clicks on the tag `DIV#add_item`:
	* The new element must be: `<li>Item</li>` 
	* The new element must be added to `UL.my_list` 
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
$ 
```
---

+ [x] 6\. **Change the text**

+ **[6-script.js](./6-script.js)**

* Write a JavaScript script that updates the text of the `<header>` element to 
	`New Header!!!` when the user clicks on `DIV#update_header` 
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
$ 
```
---

+ [x] 7\. **Star wars character**

+ **[7-script.js](./7-script.js)**

* Write a JavaScript script that fetches the character `name` from 
	this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json` 
	* The name must be displayed in the HTML tag `DIV#character` 
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
$ 
```
---

+ [x] 8\. **Star Wars movies**

+ **[8-script.js](./8-script.js)**

* Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: 
	
	`https://swapi-api.hbtn.io/api/films/?format=json` 
	
	* All movie titles must be list in the HTML tag `UL#list_movies` 
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`

* Please test with this HTML file in your browser:

```bash
$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
$ 
```
---
 
+ [x] 9\. **Say Hello!**

+ **[9-script.js](./9-script.js)**

* Write a JavaScript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` 
	and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.
	* The translation of “hello” must be displayed in the HTML tag `DIV#hello` 
		* Don’t use `document.querySelector` to select the HTML tag
		* Use the `JQuery API`
		* The script must work when it is imported from the `<head>` tag

* Please test with this HTML file in your browser:

```bash
$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
$ 
```
---

+ [x] 10\. **No jQuery - document loaded**

+ **[100-script.js](./100-script.js)**

* Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
	* Use `document.querySelector` to select the HTML tag
	* Don’t use the `jQuery API`
	* Note: The script must be imported from the `<head>` tag, not at the end of the HTML

* Please test with this HTML file in your browser:

```bash
$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
$ 
```
---
 
+ [x] 11\. **List, add, remove**

+ **[101-script.js](./101-script.js)**

* Write a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks:
	
	* The new element must be: `<li>Item</li>` 
	* The new element must be added to `UL.my_list` 
	* When the user clicks on `DIV#add_item`: a new element is added to the list
	* When the user clicks on `DIV#remove_item`: the last element is removed from the list
	* When the user clicks on `DIV#clear_list`: all elements of the list are removed
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`
	* The script must work when it imported from the `HEAD` tag
* Please test with this HTML file in your browser:

```bash
$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
$ 
```
---
 
+ [x] 12\. **Say hello to everybody!**

+ **[102-script.js](./102-script.js)**

* Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
	* Use this API service: `https://www.fourtonfish.com/hellosalut/hello/` 
	* The language code will be the value entered in the tag `INPUT#language_code` (ex:`es`,`fr`,`en` etc.)
	* The translation must be fetched when the user clicks on `INPUT#btn_translate` 
	* The translation of “Hello” must be displayed in the HTML tag `DIV#hello` 
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`
	* The script must work when imported from the `<head>` tag

* Please test with this HTML file in your browser:

```bash
$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
$ 
```
---

+ [x] 13\. **And press ENTER**

+ **[103-script.js](./103-script.js)**

* Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
	* You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/` 
	* The language code will be the value entered in the tag `INPUT#language_code` (ex:`es`, `fr`, `en` etc.)
	* The translation must be fetched when the user clicks on `INPUT#btn_translate` 
	OR presses `ENTER` when the focus is on `INPUT#language_code` 
	* The translation of “Hello” must be displayed in the HTML tag `DIV#hello` 
	* Don’t use `document.querySelector` to select the HTML tag
	* Use the `JQuery API`
	* The script must work when imported from the `<head>` tag

* Please test with this HTML file in your browser:

```bash
$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
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
