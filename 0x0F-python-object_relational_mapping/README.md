<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Emacs-purple.svg"/>	
<img src="https://img.shields.io/badge/SQL-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>
</p>

---

# 0x0F. Python - Object-relational mapping

This project contains some tasks for continue learning about how *`object-relational mapping`* is used for database scripting, with using *`MySQLdb`* and *`SQLAlchemy`* to `query`, `create`, `edit`, and `delete` tables in *`MySQL`*.

<div style="text-align: justify">

<p align="center">
  <img width="400"  
        src="https://res.cloudinary.com/practicaldev/image/fetch/s--SJ7oLQP---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://storage.googleapis.com/hackersandslackers-cdn/2019/07/sqlalchemy-relationships.jpg"
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

The project contains some tasks for continue learning about how object-relational mapping is used for database scripting.

## Background Context
In this project, you will link two amazing worlds: Databases and Python!
In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.
In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. 
With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? 
when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. 
You will be able to change your storage easily without re-writing your entire project.

***Without ORM:***

```bash
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

***With an ORM:***

```bash
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right? 
The biggest difficulty with ORM is: The syntax!
Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire 
documentation before starting, just jump on it if you don’t get something.	
	
## Resources :books:
Read or watch:

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=sqlalchemy&source=lmns&bih=614&biw=1338&hl=en&sa=X&ved=2ahUKEwiW8Pn0ltX3AhWecDABHfRwDusQ_AUoAHoECAEQAA)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=sqlalchemy)

- [Object-relational mappers](https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA) 
- [mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw) 
 (please don’t pay attention to  ` _mysql ` )
- [MySQLdb tutorial](https://intranet.hbtn.io/rltoken/DJz5W6Y13-6qUSTPTGrHYw) 
- [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ) 
- [SQLAlchemy](https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA) 
- [mysqlclient/MySQLdb](https://intranet.hbtn.io/rltoken/QFgtVxz2w-C1y1OB8uls1g) 
- [Introduction to SQLAlchemy](https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg) 
- [Flask SQLAlchemy](https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A) 
- [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw) 
- [Python SQLAlchemy Cheatsheet](https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw) 
- [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw) 
 ***(Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)***
- [SQLAlchemy Tutorial](https://intranet.hbtn.io/rltoken/cmfi9C_nRXrmnwaJfCPyxA) 
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script 
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements
### General

- Allowed editors:`vi`, `vim`, `emacs` 
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Your files will be executed with `MySQLdb` version `2.0.x` 
- Your files will be executed with `SQLAlchemy` version `1.4.x` 
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3` 
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All files must be executable
- The length of files will be tested using `wc` 
- All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have a documentation 
	(`python3 -c 'print(__import__("my_module").my_function.__doc__)'` 
	and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or 
	method (the length of it will be verified)
- You are not allowed to use `execute` with sqlalchemy


[![sqlstyle.guide](https://img.shields.io/badge/style-sqlstyle.guide-purple.svg)](https://www.sqlstyle.guide/)

## More Info
### Install MySQLdb module version 2.0.x
For installing `MySQLdb`, you need to have `MySQL` installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://intranet.hbtn.io/rltoken/mqTU28SAIfz_-9w7rZipMw) 

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x

```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
Also, you can have this warning message:

```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: 
Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
	cursor.execute(statement, parameters)  
```
You can ignore it.	
	
	
### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-higher_level_programming.git`	
- Access to directory: `cd 0x0F-python-object_relational_mapping`

	
## Files :file_folder:
## Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. Provided by Holberton School.

## Tasks

+ [x] 0\. **Get all states**

+ **[0-select_states.py](./0-select_states.py)**

Write a script that lists all `states` from the database `hbtn_0e_0_usa`: 
* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
	(no argument validation needed)
* Use the module `MySQLdb` (`import MySQLdb`)
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Results must be sorted in ascending order by `states.id` 
* Results must be displayed as they are in the example below
* The code should not be executed when imported

```bash
$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
$ 
```
No test cases needed
---
 
+ [x] 1\. **Filter states**

+ **[1-filter_states.py](./1-filter_states.py)**

Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`: 
* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
	(no argument validation needed)
* Use the module `MySQLdb` (`import MySQLdb`)
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Results must be sorted in ascending order by `states.id` 
* Results must be displayed as they are in the example below
* The code should not be executed when imported

```bash
$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
$ 
```
No test cases needed
---

+ [x] 2\. **Filter states by user input**

+ **[2-my_filter_states.py](./2-my_filter_states.py)**

Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` 
	where `name` matches the argument.
* The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` 
	(no argument validation needed)
* Use the module `MySQLdb` (`import MySQLdb`)
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Use `format` to create the SQL query with the user input
* Results must be sorted in ascending order by `states.id` 
* Results must be displayed as they are in the example below
* The code should not be executed when imported

```bash
$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
$ 
```
No test cases needed
---
 
+ [x] 3\. **SQL Injection...**

+ **[3-my_safe_filter_states.py](./3-my_safe_filter_states.py)**

Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"`
	as an input?

```bash
$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
$ ./0-select_states.py root root hbtn_0e_0_usa
$ 
```
What? Empty?
Yes, it’s an  [SQL injection](https://intranet.hbtn.io/rltoken/f6dtded2o4a09_WEQpLypw) 
  to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` 
	where `name` matches the argument. But this time, write one that is safe from MySQL injections!

* The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and 
	`state name searched` (safe from MySQL injection)
* Use the module `MySQLdb` (`import MySQLdb`)
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Results must be sorted in ascending order by `states.id` 
* Results must be displayed as they are in the example below
* The code should not be executed when imported

```bash
$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
$ 
```
No test cases needed
---

+ [x] 4\. **Cities by states**

+ **[4-cities_by_state.py](./4-cities_by_state.py)**

Write a script that lists all `cities` from the database `hbtn_0e_4_usa` 
* Script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `MySQLdb` (`import MySQLdb`)
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Results must be sorted in ascending order by `cities.id` 
* Use only `execute()` once
* Results must be displayed as they are in the example below
* The code should not be executed when imported

```bash
$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), 
	(1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
$ 
```
No test cases needed
---
 
+ [x] 5\. **All cities by state**

+ **[5-filter_cities.py](./5-filter_cities.py)**

Write a script that takes in the name of a state as an argument and lists all `cities` of that state, 
	using the database `hbtn_0e_4_usa` 
* The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and 
	`state name` (SQL injection free!)
* Use the module `MySQLdb` (`import MySQLdb`)
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Results must be sorted in ascending order by `cities.id` 
* Use only `execute()` once
* The results must be displayed as they are in the example below
* The code should not be executed when imported

```bash
$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), 
	(1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

$  
```
No test cases needed
---

+ [x] 6\. **First state model**

+ **[model_state.py](./model_state.py)**

Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

* `State` class:* 
	* inherits from `Base` [Tips](https://intranet.hbtn.io/rltoken/mafY8fCi8Jav6M8OvCfYvQ) 
	* links to the MySQL table `states` 
	* class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null 
		and is a primary key
	* class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null

* Use the module `SQLAlchemy` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* **WARNING**: all classes who inherit from `Base` must be imported before 
	calling `Base.metadata.create_all(engine)`
 
```bash
$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), 
				pool_pre_ping=True)
    Base.metadata.create_all(engine)

$ ./6-model_state.py root root hbtn_0e_6_usa
$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  
				PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
$ 

```
No test cases needed
---

+ [x] 7\. **All states via SQLAlchemy**

+ **[7-model_state_fetch_all.py](./7-model_state_fetch_all.py)**

Write a script that lists all `State` objects from the database  `hbtn_0e_6_usa`
 
* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* Import `State` and `Base` from `model_state` - `from model_state import Base, State` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Results must be sorted in ascending order by `states.id` 
* The results must be displayed as they are in the example below
* The code should not be executed when imported

```bash
$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
$ 
```
No test cases needed
---

+ [x] 8\. **First state**

+ **[8-model_state_fetch_first.py](./8-model_state_fetch_first.py)**

Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* Import `State` and `Base` from `model_state` - `from model_state import Base, State` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* The state you display must be the first in `states.id` 
* Not allowed to fetch all states from the database before displaying the result
* The results must be displayed as they are in the example below
* If the table `states` is empty, print `Nothing` followed by a new line
* The code should not be executed when imported

```bash
$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
$ 
```
No test cases needed
---

+ [x] 9\. **Contains `a` **

+ **[9-model_state_filter_a.py](./9-model_state_filter_a.py)**

Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* Import `State` and `Base` from `model_state` - `from model_state import Base, State` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Results must be sorted in ascending order by `states.id` 
* The results must be displayed as they are in the example below
* The code should not be executed when imported

```bash
$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
$ 
```
No test cases needed
---

+ [x] 10\. **Get a state**

+ **[10-model_state_my_get.py](./10-model_state_my_get.py)**

Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

* The script should take 4 arguments: `mysql username`, `mysql password`, `database name` and 
	`state name to search` (SQL injection free)
* Use the module `SQLAlchemy` 
* Import `State` and `Base` from `model_state` - `from model_state import Base, State` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Can assume to have one record with the state name to search
* Results must display the `states.id` 
* If no state has the name you searched for, display `Not found` 
* The code should not be executed when imported

```bash
$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
$ 
```
No test cases needed
---
 
+ [x] 11\. **Add a new state**

+ **[11-model_state_insert.py](./11-model_state_insert.py)**

Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`

* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* Import `State` and `Base` from `model_state` - `from model_state import Base, State` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Print the new `states.id` after creation
* The code should not be executed when imported

```bash
$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
$ 
```
No test cases needed
---

+ [x] 12\. **Update a state**

+ **[12-model_state_update_id_2.py](./12-model_state_update_id_2.py)**

Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* Import `State` and `Base` from `model_state` - `from model_state import Base, State` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Change the name of the `State`  where `id = 2` to `New Mexico` 
* The code should not be executed when imported

```bash
$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
$ 
```
No test cases needed
---

+ [x] 13\. **Delete states**

+ **[13-model_state_delete_a.py](./13-model_state_delete_a.py)**

Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`

* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* Import `State` and `Base` from `model_state` - `from model_state import Base, State` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* The code should not be executed when imported

```bash
$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
$ 
```
No test cases needed
---

+ [x] 14\. **Cities in state**

+ **[model_city.py](./model_city.py)**
+ **[14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py)**

Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

* `City` class:
	* inherits from `Base` (imported from `model_state`)
	* links to the MySQL table `cities` 
	* class attribute `id` that represents a column of an auto-generated, unique integer, 
		can’t be null and is a primary key
	* class attribute `name` that represents a column of a string of 128 characters and can’t be null
	* class attribute `state_id` that represents a column of an integer, can’t be null and is a 
		foreign key to `states.id` 

* Use the module `SQLAlchemy`

Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:

* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* Import `State` and `Base` from `model_state` - `from model_state import Base, State` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Results must be sorted in ascending order by `cities.id` 
* Results must be display as they are in the example below (`<state name>: (<city id>) <city name>`)
* The code should not be executed when imported

```bash
$ cat 14-model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), 
	(1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
$ 
```
No test cases needed
---

+ [x] 15\. **City relationship**

+ **[relationship_city.py](./relationship_city.py)**
+ **[relationship_state.py](./relationship_state.py)**
+ **[100-relationship_states_cities.py](./100-relationship_states_cities.py)**

Improve the files `model_city.py` and `model_state.py`, and save them as `relationship_city.py` and `relationship_state.py`:

* `City` class:
	* No change

* `State` class:
	* In addition to previous requirements, the class attribute `cities` must represent a relationship with 
	the class `City`. If the `State` object is deleted, all linked `City` objects must be automatically deleted. 
	Also, the reference  from a `City` object to his `State` should be named `state` 
* Use the module `SQLAlchemy`
 
Write a script that creates the `State` “California” with the `City` “San Francisco” from the database `hbtn_0e_100_usa`: 
	(`100-relationship_states_cities.py`)

* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Use the `cities` relationship for all `State` objects
* The code should not be executed when imported

```bash
$ cat 100-relationship_states_cities.sql
-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

SELECT * FROM states;
SELECT * FROM cities;

$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 5: Table 'hbtn_0e_100_usa.states' doesn't exist
$ ./100-relationship_states_cities.py root root hbtn_0e_100_usa
$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password: 
id  name
1   California
id  name    state_id
1   San Francisco   1
$ 
```
No test cases needed
---

+ [x] 16\. **List relationship**

+ **[101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py)**

Write a script that lists all `State` objects, and corresponding `City` objects, contained in the database `hbtn_0e_101_usa`
 
* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* Use the module `SQLAlchemy` 
* The connection to your MySQL server must be to `localhost` on port `3306` 
* Only use one query to the database
* Use the `cities` relationship for all `State` objects
* Results must be sorted in ascending order by `states.id` and `cities.id` 
* Results must be displayed as they are in the example below
* The code should not be executed when imported

``` 
<state id>: <state name>
<tabulation><city id>: <city name>
``` 

```bash
$ cat 101-relationship_states_cities_list.sql
-- Create states table in hbtn_0e_101_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_101_usa;
USE hbtn_0e_101_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), 
	(1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

$ cat 101-relationship_states_cities_list.sql | mysql -uroot -p
$ ./101-relationship_states_cities_list.py root root hbtn_0e_101_usa
1: California
    1: San Francisco
    2: San Jose
    3: Los Angeles
    4: Fremont
    5: Livermore
2: Arizona
    6: Page
    7: Phoenix
3: Texas
    8: Dallas
    9: Houston
    10: Austin
4: New York
    11: New York
5: Nevada
    12: Las Vegas
    13: Reno
    14: Henderson
    15: Carson City
$ 
```
No test cases needed
---

+ [x] 17\. **From city**

+ **[102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py)**

Write a script that lists all `City` objects from the database `hbtn_0e_101_usa`

* The script should take 3 arguments: `mysql username`, `mysql password` and `database name` 
* The must use the module `SQLAlchemy` 
* The script should connect to a MySQL server running on `localhost` at port `3306` 
* Use only one query to the database
* You must use the `state` relationship to access to the `State` object linked to the `City` object
* Results must be sorted in ascending order by `cities.id` 
* Results must be displayed as they are in the example below
* Your code should not be executed when imported

```
<city id>: <city name> -> <state name>
```

```bash
$ ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
1: San Francisco -> California
2: San Jose -> California
3: Los Angeles -> California
4: Fremont -> California
5: Livermore -> California
6: Page -> Arizona
7: Phoenix -> Arizona
8: Dallas -> Texas
9: Houston -> Texas
10: Austin -> Texas
11: New York -> New York
12: Las Vegas -> Nevada
13: Reno -> Nevada
14: Henderson -> Nevada
15: Carson City -> Nevada
$ 
```
No test cases needed

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

