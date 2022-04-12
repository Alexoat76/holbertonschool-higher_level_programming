<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>
<img src="https://img.shields.io/badge/JavaScript-yellow.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x14. JavaScript - Web scraping

This project contains some tasks for learning how to use  *`file I/O`*  on  **`Node.js`**  and using the  **NPM**  request
framework to interact with the  **[Star Wars](https://swapi.co/)**,  **[JSONplaceholder](https://jsonplaceholder.typicode.com)**,  and
**[Twitter](https://developer.twitter.com/en/docs/api-reference-index)** API's in *`JavaScript`*.

<p align="center">
  <img width="500"  
        src="https://soyhorizonte.com/wp-content/uploads/2020/10/JS-by-SoyHorizonte.gif"
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
	
The project shows how to use *`Javascript`* and the request module to `read` url text content and gather data from `API's`.

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=JavaScript+Web+scraping&bih=682&biw=1274&hl=en&ei=O0tUYpa3IOLrxgHa66mIBA&ved=0ahUKEwjWwNTHq4z3AhXitTEKHdp1CkEQ4dUDCA4&uact=5&oq=JavaScript+Web+scraping&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoGCAAQBxAeSgQIQRgASgQIRhgAUNgGWPgKYJIeaAFwAXgAgAGEAYgB4AKSAQMwLjOYAQCgAQHIAQjAAQE&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=JavaScript+Web+scraping)

- [Working with JSON data](https://intranet.hbtn.io/rltoken/RmDpb2gJfPrMar05QdxYvw) 
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.hbtn.io/rltoken/ibqGcS_YNbtWO8nPIlM2Ug) 
- [request module](https://intranet.hbtn.io/rltoken/9L4UYvlIwDVDoObD7zpJZQ) 
- [Modern JS](https://intranet.hbtn.io/rltoken/Zf5LCjoTEuIXWWxoH_dGVQ)  
 
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

### Install request module and use it
**[Documentation](https://intranet.hbtn.io/rltoken/9L4UYvlIwDVDoObD7zpJZQ)** 

 ` $ sudo npm install request --global `
	
 ` $ export NODE_PATH=/usr/lib/node_modules`	
	
### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-higher_level_programming.git`	
- Access to directory: `cd 0x14-javascript-web_scraping`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:
### Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. Provided by Holberton School.
		
---

## Tasks
	
+ [x] 0\. **Readme**

+ **[0-readme.js](./0-readme.js)**

* Write a script that reads and prints the content of a file.
	* The first argument is the file path
	* The content of the file must be read in `utf-8` 
	* If an error occurred during the reading, print the error object

```bash
$ ./0-readme.js cisfun
C is super fun!

$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
$ 
```
---

+ [x] 1\. **Write me**

+ **[1-writeme.js](./1-writeme.js)**

* Write a script that writes a string to a file.
	* The first argument is the file path
	* The second argument is the string to write
	* The content of the file must be written in `utf-8` 
	* If an error occurred during while writing, print the error object

```bash
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool
$ 
```
---

+ [x] 2\. **Status code**

+ **[2-statuscode.js](./2-statuscode.js)**

* Write a script that display the status code of a `GET` request.
	* The first argument is the URL to request (`GET`)
	* The status code must be printed like this: `code: <status code>` 
	* Use the module `request`
 
```bash
$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
$ 
```
---

+ [x] 3\. **Star wars movie title**

+ **[3-starwars_title.js](./3-starwars_title.js)**

* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
	* The first argument is the movie ID
	* Use the [Star wars API](https://intranet.hbtn.io/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q) 
 	with the endpoint `https://swapi-api.hbtn.io/api/films/:id` 
	* Use the module `request`

```bash
$ ./3-starwars_title.js 1
A New Hope
$ ./3-starwars_title.js 5
Attack of the Clones
$ 
```
---

+ [x] 4\. **Star wars Wedge Antilles**

+ **[4-starwars_count.js](./4-starwars_count.js)**

* Write a script that prints the number of movies where the character “Wedge Antilles” is present.
	* The first argument is the API URL of the [Star wars API](https://intranet.hbtn.io/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q) 
	:  ` https://swapi-api.hbtn.io/api/films/ ` 
	* Wedge Antilles is character ID `18` - your script must use this ID for filtering the result of the API
	* Use the module `request`
```bash
$ ./4-starwars_count.js https://swapi-api.hbtn.io/api/films
3
$ 
```
---

+ [x] 5\. **Loripsum**

+ **[5-request_store.js](./5-request_store.js)**

* Write a script that gets the contents of a webpage and stores it in a file.
	* The first argument is the URL to request
	* The second argument the file path to store the body response
	* The file must be UTF-8 encoded
	* Use the module `request`

```bash

$ ./5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane 
intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, 
modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima 
illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, 
tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane 
commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio 
Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut 
incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse 
beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, 
quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, 
ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet 
sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala 
sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, 
non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae 
actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea 
adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto 
in philosophia constituta sunt omnia. </p>
$ 
```
---

+ [x] 6\. **How many completed?**

+ **[6-completed_tasks.js](./6-completed_tasks.js)**

* Write a script that computes the number of tasks completed by user id.
	* The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos` 
	* Only print users with completed task
	* Use the module `request`
 
```bash
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
$
```
---
 
+ [x] 7\. **Who was playing in this movie?**

+ **[100-starwars_characters.js](./100-starwars_characters.js)**

* Write a script that prints all characters of a Star Wars movie:
	* The first argument is the Movie ID - example: `3` = “Return of the Jedi” 
	* Display one character name by line
	* Use the [Star wars API](https://intranet.hbtn.io/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q) 
	* Use the module `request`

```bash
$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
guillaume@ubuntu:~/0x14$ 
```
---

+ [x] 8\. **Right order**

+ **[101-starwars_characters.js](./101-starwars_characters.js)**

* Write a script that prints all characters of a Star Wars movie:
	* The first argument is the Movie ID - example: `3` = “Return of the Jedi” 
	* Display one character name by line in the same order of the list “characters” in the `/films/` response
	* Use the [Star wars API](https://intranet.hbtn.io/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q) 
	* Use the module `request`

```bash

$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
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
