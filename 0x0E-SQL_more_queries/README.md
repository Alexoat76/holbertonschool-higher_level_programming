<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>	
<img src="https://img.shields.io/badge/SQL-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>
</p>

---

# 0x0E. SQL - More queries

Thank you for visiting this repository. Each file in this repository holds code that illustrates an essential concept of programming, specific to the `SQL programming` language. Like Basic query operation: **`the join`**.

<div style="text-align: justify">

<p align="center">
  <img width="250"  
        src="https://github.com/Alexoat76/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/assets/sql.png"
  >
	
[![sqlstyle.guide](https://img.shields.io/badge/style-sqlstyle.guide-purple.svg)](https://www.sqlstyle.guide/)

</p>	
	
  
# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents
* [About](#about)
* [Requirements](#requirements)
* [Tasks](#tasks)
* [Credits](#credits)

## About
	
This project contains some tasks for learning more about the basics of **`SQL`** using the **`MySQL`** DBMS.
  
## Resources :books:

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=sql&oq=sql&aqs=chrome..69i57j0i512l9.1309j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=sql)

- [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/u4h2MXcCQfadszlRMQy-gw) 
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/ztrEKQexfEDtZ-8EUsG70Q) 
- [MySQL constraints](https://intranet.hbtn.io/rltoken/LBrFqCMm9N9woTX7sS7e0g) 
- [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/YYpPtkqFeKSCsAU4Y_y3Og) 
- [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A) 
- [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg) 
- [SQL technique: join types](https://intranet.hbtn.io/rltoken/ryjyRRN7696rJV0maP03Xw) 
- [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/L7Fi5w8GZG5MSdQZ19e88g) 
- [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/V9vpLbtkFwV4EZYoiz2NBA) 
- [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/ySKSdhFeMDddea07XrDzeQ) 
- [MySQL Tutorial](https://intranet.hbtn.io/rltoken/-uqP0a89xUl3SsmV_ZtxRA) 
- [SQL Style Guide](https://intranet.hbtn.io/rltoken/jn4SHgwVtOJF0LQYPEIs-g) 
- [MySQL 8.0 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/v1VjRjcgXmGeGq8ojvOPnA) 

Extra resources around relational database model design:
- [Design](https://intranet.hbtn.io/rltoken/9ppVdXqFMn-v1eKuxsOvaQ) 
- [Normalization](https://intranet.hbtn.io/rltoken/zo6dqYxsXby3S3uON5JfOg) 
- [ER Modeling](https://intranet.hbtn.io/rltoken/ZaMMezT-GdpgHB9pmM78iw) 

### General
* How to create a new MySQL user.
* How to manage privileges for a user to a database or table.
* What???s a  `PRIMARY KEY`. 
* What???s a  `FOREIGN KEY`. 
* How to use  `NOT NULL`  and  `UNIQUE`  constraints.
* How to retrieve datas from multiple tables in one request.
* What are subqueries.
* What are `JOIN` and `UNION`.

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs` 
* All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0`  (version 8.0.25).
* All your files should end with a new line.
* All your SQL queries should have a comment just before (i.e. syntax above).
* All your files should start by a comment describing the task.
* All SQL keywords should be in uppercase (`SELECT`, `WHERE`???)
* A `README.md` file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using `wc`.

# Tasks

+ [x] 0\. **My privileges!**
+ **[0-privileges.sql](0-privileges.sql)**
	
* Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the MySQL server.
---
	
+ [x] 1\. **Root user**
+ **[1-create_user.sql](1-create_user.sql)**
	
* Script that creates the MySQL server user `user_0d_1` with all privileges and the password `user_0d_1_pwd` in the MySQL server (if it doesn't exist).
---
	
+ [x] 2\. **Read user**
+ **[2-create_read_user.sql](2-create_read_user.sql)**

* Script that creates the database `hbtn_0d_`,2 and the user `user_0d_2` with only SELECT privileges and the password `user_0d_2_pwd` in the MySQL server (if they don't exist).
---
	
+ [x] 3\. **Always a name**
+ **[3-force_name.sql](3-force_name.sql)**
	
* Script that creates the table `force_name` in the MySQL server (if it doesn't exist).
  + The description of `force_name`:
  ```python
  class force_name:
      id: INT
      name: VARCHAR(256)
  ```
  `name` cannot be null.
---
	
+ [x] 4\. **ID can't be null**
+ **[4-never_empty.sql](4-never_empty.sql)**
	
* Script that creates the table `id_not_null` in the MySQL server (if it doesn't exist).
  + The description of `id_not_null`:
  ```python
  class id_not_null:
      id: INT
      name: VARCHAR(256)
  ```
  `id` has a default value of 1 and `name` cannot be null.
---
	
+ [x] 5\. **Unique ID**
+ **[5-unique_id.sql](5-unique_id.sql)**
	
* Script that creates the table `unique_id` in the MySQL server (if it doesn't exist).
  + The description of `unique_id`:
  ```python
  class unique_id:
      id: INT
      name: VARCHAR(256)
  ```
  `id` has a default value of 1 and must be unique. `name` cannot be null.
---
	
+ [x] 6\. **States table**
+ **[6-states.sql](6-states.sql)**
	
* Script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) in the MySQL server (if they don't exist).
  + The description of `states`:
  ```python
  class states:
      id: INT
      name: VARCHAR(256)
  ```
  `id` has a to be unique, auto generated, not null and must be the primary key. `name` cannot be null.
---
	
+ [x] 7\. **Cities table**
+ **[7-cities.sql](7-cities.sql)**
	
* Script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) in the MySQL server (if they don't exist).
  + The description of `cities`:
  ```python
  class cities:
      id: INT
      state_id: INT
      name: VARCHAR(256)
  ```
  `id` has a to be unique, auto generated, not null and must be the primary key. `state_id` must be a `FOREIGN KEY` that references to `id` of the `states` table and cannot be null. `name` cannot be null.
---
	
+ [x] 8\. **Cities of California**
+ **[8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql)**
	
* Script that lists all the cities of California that can be found in the database `hbtn_0d_usa` in the MySQL server. 
	* The results must be sorted in ascending order by `cities.id` and the **JOIN** keyword should not be used.
---
	
+ [x] 9\. **Cities by States**
+ **[9-cities_by_state_join.sql](9-cities_by_state_join.sql)**
	
* Script that lists all cities contained in the database `hbtn_0d_usa`. 
	* Each record should display: `cities.id` - `cities.name` - `states.name` (in that order). 
	* The results must be sorted in ascending order by `cities.id` and only one **SELECT** statement can be used.
---
	
+ [x] 10\. **Genre ID by show**	
+ **[10-genre_id_by_show.sql](10-genre_id_by_show.sql)**
	
* Script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. 
	* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id` (in that order). 
	* The results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. 
	* Only one **SELECT** statement can be used. 
	* The script in [hbtn_0d_tvshows.sql](hbtn_0d_tvshows.sql) should be executed using the database `hbtn_0d_tvshows`, which should be created for testing tasks 		10 to 18.
---

+ [x] 11\. **Genre ID for all shows**
+ **[11-genre_id_all_shows.sql](11-genre_id_all_shows.sql)**
	
* Script that lists all shows contained in the database `hbtn_0d_tvshows`. 
	* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id` (in that order). 
	* The results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. 
	* If a show doesn???t have a `genre`, display `NULL`. 
	* Only one **SELECT** statement can be used.
---
	
+ [x] 12\. **No genre**
+ **[12-no_genre.sql](12-no_genre.sql)**
	
* Script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked. 
	* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id` (in that order). 
	* The results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. 
	* Only one **SELECT** statement can be used.
---
	
+ [x] 13\. **Number of shows by genre**
+ **[13-count_shows_by_genre.sql](13-count_shows_by_genre.sql)**

* Script that  lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each. 
	* Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>` (in that order). 
	* The first column must be called `genre`. 
	* The second column must be called `number_of_shows`. 
	* A genre that doesn???t have any shows linked shouldn't be displayed. 
	* The results must be sorted in descending order by the number of shows linked. 
	* Only one **SELECT** statement can be used.
---
	
+ [x] 14\. **My genres**	
+ **[14-my_genres.sql](14-my_genres.sql)**

* Script that uses the `hbtn_0d_tvshows` database to list all genres of the show `Dexter`. 
	* Each record should display: `tv_genres.name`. 
	* The results must be sorted in ascending order by the genre name. 
	* Only one **SELECT** statement can be used.
---
	
+ [x] 15\. **Only Comedy**	
+ **[15-comedy_only.sql](15-comedy_only.sql)**
	
* Script that lists all `Comedy` shows in the database `hbtn_0d_tvshows`. 
	* Each record should display: `tv_shows.title`. 
	* The results must be sorted in ascending order by the show title. 
	* Only one **SELECT** statement can be used.
---
	
+ [x] 16\. **List shows and genres**
+ **[16-shows_by_genre.sql](16-shows_by_genre.sql)**

* Script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`. 
	* If a show doesn???t have a `genre`, display `NULL` in the `genre` column. 
	* Each record should display: `tv_shows.title` - `tv_genres.name` (in that order). 
	* The results must be sorted in ascending order by the show title and genre name. 
	* Only one **SELECT** statement can be used.
	
---

## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Alex Orland Ar??valo Tribaldos`**  and credits for `group projects` are displayed in the respective `README.md` files.

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

