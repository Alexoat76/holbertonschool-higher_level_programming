<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>	
<img src="https://img.shields.io/badge/SQL-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>
</p>
	
---
	
# 0x0D. SQL - Introduction
<div style="text-align: justify">

Thank you for visiting this repository. Each file in this repository holds code that illustrates an essential concept of programming, specific to the SQL programming language. 
<div style="text-align: justify">

<p align="center">
  <img width="250"  
        src="https://github.com/Alexoat76/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/assets/sql.png"
  >
</p>	
	

# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents
* [About](#about)
* [Requirements](#requirements)
* [Tasks](#tasks)
* [Credits](#credits)
	
## About
	
This project contains some tasks for learning the basics about **`SQL`** using the **`MySQL`** DBMS.
	
[Databases](https://intranet.hbtn.io/concepts/556)
	
## Resources :books:

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=sql&oq=sql&aqs=chrome..69i57j0i512l9.1309j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=sql)
	
	
- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php) **`(no need to read the chapter “Privileges”)`**
- [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
- [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
	
## Requirements
	
## General :page_with_curl:
	
- Allowed editors: `vi`, `vim`, `emacs`.
- All your files will be executed on `Ubuntu 20.04` LTS using `MySQL 8.0` (version 8.0.25).
- All your files should end with a new line.
- All your **`SQL`** queries should have a comment just before (i.e. syntax above).
- All your files should start by a comment describing the task.
- All `SQL keywords` should be in **`uppercase`** (SELECT, WHERE…).
- A `README.md` file, at the root of the folder of the project, is mandatory.
- The length of your files will be tested using `wc`.

	
## Tasks

+ [x] 0\. **List databases**
	
+ **[0-list_databases.sql](0-list_databases.sql)**
* Script that lists all databases of the MySQL server.
---
	
+ [x] 1\. **Create a database**
	
+ **[1-create_database_if_missing.sql](1-create_database_if_missing.sql)**	
* Script that creates the database ``hbtn_0c_0`` in the MySQL server (if it doesn't exist).
---
	
+ [x] 2\. **Delete a database**
	
+ **[2-remove_database.sql](2-remove_database.sql)**
* Script that deletes the database `hbtn_0c_0` in the MySQL server (if it exists).
---
	
+ [x] 3\. **List tables**

+ **[3-list_tables.sql](3-list_tables.sql)**
* Script that lists all the tables of a database in the MySQL server.
---
	
+ [x] 4\. **First table**
	
+ **[4-first_table.sql](4-first_table.sql)**
* Script that creates a table called first_table in the current database in your MySQL server.
  + The description of `first_table`:
	
  ```python
  class first_table:
      id: INT
      name: VARCHAR(256)
  ```
---
	
+ [x] 5\. **Full description**
	
+ **[5-full_table.sql](5-full_table.sql)**	
* Script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in the MySQL server.
---
	
+ [x] 6\. **List all in table**
	
+ **[6-list_values.sql](6-list_values.sql)**
* Script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in the MySQL server.
---
	
+ [x] 7\. **First add**
	
+ **[7-insert_value.sql](7-insert_value.sql)**
* Script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in the MySQL server.
  + The row:
  ```json
  {"id": 89, "name": "Best School"}
  ```
---
	
+ [x] 8\. **Count 89**
+ **[8-count_89.sql](8-count_89.sql)**
	
* Script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in the MySQL server.
---
	
+ [x] 9\. **Full creation**
+ **[9-full_creation.sql](9-full_creation.sql)**
	
* Script that creates a table `second_table` in the database `hbtn_0c_0` in the MySQL server (if it doesn't exist), and adds multiples rows.
  + The description of `second_table`:
	
  ```python
  class second_table:
      id: INT
      name: VARCHAR(256)
      score: INT
  ```
  + The script should create these records:
  ```json
  [
    {"id": 1, "name": "John", "score": 10},
    {"id": 2, "name": "Alex", "score": 3},
    {"id": 3, "name": "Bob", "score": 14},
    {"id": 4, "name": "George", "score": 8}
  ]
  ```
---
	
+ [x] 10\. **List by best**	
+ **[10-top_score.sql](10-top_score.sql)**
	
* Script that lists all records of the table `second_table` of the database `hbtn_0c_0` in the MySQL server. 
	* The records should be ordered by `score` (top first) and the results should display the `score` first then the `name`.
---
	
+ [x] 11\. **Select the best**
+ **[11-best_score.sql](11-best_score.sql)**
	
* Script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in the MySQL server. 
	* The records should be ordered by `score` (top first) and the results should display the `score` first then the `name`.
---
	
+ [x] 12\. **Cheating is bad**
+ **[12-no_cheating.sql](12-no_cheating.sql)**
	
* Script that updates the score of _Bob_ to _10_ in the table `second_table`.
---
	
+ [x] 13\. **Score too low**
+ **[13-change_class.sql](13-change_class.sql)**
	
* Script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in the MySQL server.
---
						    
+ [x] 14\. **Average**
+ **[14-average.sql](14-average.sql)**
						    
* Script that computes the `score` average of all records in the table `second_table` of the database `hbtn_0c_0` in the MySQL server. 
	* The result column name should be `average`.
---
						    
+ [x] 15\. **Number by score**
+ **[15-groups.sql](15-groups.sql)**
						    
* Script that lists the number of records with the same `score` in the table `second_table` of the database `hbtn_0c_0` in the MySQL server. 
	* The list should be sorted by the number of records (descending). 
	* The result should display the `score` first then the number of records for this `score` with the label `number`.
---
						    
+ [x] 16\. **Say my name**
+ **[16-square.sql](16-square.sql)**
						    
* Script that lists all records of the table `second_table` of the database `hbtn_0c_0` in the MySQL server. 
	* The results should display the `score` and the `name` (in this order) and they should be listed by descending `score` but rows without a `name` value 	shouldn't be included.
---
	
+ [x] 17\. **Go to UTF8**
+ **[100-move_to_utf8.sql](100-move_to_utf8.sql)**
	
* Script that converts the following to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in the MySQL server:
  + Database `hbtn_0c_0`
  + Table `first_table` in database `hbtn_0c_0`
  + Field `name` in `first_table`
---
	
+ [x] 18\. **Temperatures #0**
+ **[101-avg_temperatures.sql](101-avg_temperatures.sql)**
	
* Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending). 
	* The table in **[temperatures.sql](temperatures.sql)** is used for this task. 
	* The script in **[temperatures.sql](temperatures.sql)** should be executed using the database `hbtn_0c_0`, which should have been during the previous tasks, 		for testing tasks 18 to 20.
---
	
+ [x] 19\. **Temperatures #1**
+ **[102-top_city.sql](102-top_city.sql)**
	
* Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).
---
	
+ [x] 20\. **Temperatures #2**
+ **[103-max_state.sql](103-max_state.sql)**
	
+ Script that displays the max temperature of each state (ordered by State name).
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
